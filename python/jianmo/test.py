import pulp as lp
from itertools import combinations, product

# ========== 数据初始化（新增运输时间筛选） ==========
tasks = list(range(1,11))
R = {1:15,2:11,3:4,4:11,5:18,6:8,7:19,8:5,9:9,10:13}
parking = ['P1','P2','P3','P4']
cranes = ['C1','C2']

# 预筛选有效停车位-岸桥组合（运输时间≤15分钟）[5](@ref)
transport_time = {
    ('P1','C1'):17, ('P2','C1'):15, ('P3','C1'):13, ('P4','C1'):11,
    ('P1','C2'):15, ('P2','C2'):13, ('P3','C2'):11, ('P4','C2'):9
}
valid_pairs = [(p,c) for p,c in product(parking,cranes) if transport_time[(p,c)] <= 15]

# ========== 模型构建 ==========
model = lp.LpProblem("AGV_Scheduling_Optimized", lp.LpMinimize)

# ========== 变量定义优化 ==========
# 1. 仅定义有效组合变量
X = lp.LpVariable.dicts("X", [(i,p,c) for i in tasks for (p,c) in valid_pairs], cat='Binary')
# 2. 时间变量离散化（5单位聚合）
D = lp.LpVariable.dicts("D", tasks, lowBound=0, cat='Integer')  # 整数化时间变量
B = {i: D[i] + 13 for i in tasks}  # 公式2直接计算，无需变量
C = lp.LpVariable.dicts("C", tasks, lowBound=0)
E = {i: C[i] + 20 for i in tasks}  # 直接计算结束时间
C_max = lp.LpVariable("C_max", lowBound=0)

# 动态计算M值（基于任务特征）[6](@ref)
max_R = max(R.values())                # 19
max_transport = max(transport_time.values())  # 15
M = max_R + max_transport + 20*len(tasks)  # 19+15+200=234

# ========== 目标函数优化（多目标加权） ==========
transport_cost = lp.lpSum(transport_time[(p,c)]*X[i,p,c] for i,p,c in X)
model += 0.7*C_max + 0.3*transport_cost  # 平衡时间与成本[3,4](@ref)

# ========== 约束优化 ==========
# 1. 任务分配约束（仅有效组合）
for i in tasks:
    model += lp.lpSum(X[i,p,c] for (p,c) in valid_pairs) == 1  # 公式1
    model += D[i] >= R[i]  # 就绪时间约束
    model += C[i] == B[i] + lp.lpSum(transport_time[(p,c)]*X[i,p,c] for (p,c) in valid_pairs)
    model += C_max >= E[i]

# 2. 时间窗口约束（离散化到5单位块）[5,7](@ref)
max_time_block = 40
for t_block in range(max_time_block):
    for i in tasks:
        # 定义辅助变量a_block[i,t_block]
        a_block = lp.LpVariable(f"a_block_{i}_{t_block}", cat='Binary')
        # D[i] <= 5*t_block → a_block=1
        model += 5*t_block >= D[i] - M*(1 - a_block)
        # 5*t_block < B[i] → 5*(t_block+1) <= B[i] + M*(1 - a_block)
        model += 5*(t_block + 1) <= B[i] + M*(1 - a_block)
        # 累加占用状态
    model += lp.lpSum(a_block[i,t_block] for i in tasks) <= 4

# 3. 冲突约束合并（同一停车位不同岸桥合并检查）[1,6](@ref)
for p in parking:
    for i,j in combinations(tasks, 2):
        same_parking = lp.lpSum(X[i,p,c] + X[j,p,c] for c in cranes if (p,c) in valid_pairs)
        model += (B[i] <= D[j] + M*(2 - same_parking)) | (B[j] <= D[i] + M*(2 - same_parking))

# 4. 岸桥冲突约束（仅检查岸桥维度）[1](@ref)
for c in cranes:
    for i,j in combinations(tasks, 2):
        same_crane = lp.lpSum(X[i,p,c] + X[j,p,c] for p in parking if (p,c) in valid_pairs)
        model += (C[i] + 20 <= C[j] + M*(2 - same_crane)) | (C[j] + 20 <= C[i] + M*(2 - same_crane))

# ========== 求解参数调优 ==========
model.solve(
    solver=lp.GUROBI(
        msg=True,
        threads=8,
        timeLimit=300,
        MIPGap=0.02,   # 允许2%最优间隙[5](@ref)
        Heuristics=0.5 # 增强启发式搜索
    )
)

# ========== 结果解析（略，同原代码） ==========
print(f"求解状态: {lp.LpStatus[model.status]}")
print(f"最大完工时间: {lp.value(C_max):.1f}")

# 输出解析
schedule = []
for i in tasks:
    for p,c in product(parking,cranes):
        if lp.value(X[i,p,c]) > 0.5:
            schedule.append({
                '任务':i,
                '行车开始':lp.value(D[i]),
                '缓冲开始':lp.value(B[i]),
                '岸桥开始':lp.value(C[i]),
                '完成时间':lp.value(E[i]),
                '停车位':p,
                '岸桥':c
            })

# 按时间排序并输出
schedule.sort(key=lambda x:x['行车开始'])
print("\n详细调度方案：")
for job in schedule:
    print(f"任务{job['任务']}: 行车区[{job['行车开始']}-{job['缓冲开始']}]"
          f" → {job['停车位']}→{job['岸桥']}"
          f" 岸桥作业[{job['岸桥开始']}-{job['完成时间']}]")