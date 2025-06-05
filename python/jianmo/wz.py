import pulp as lp
from itertools import combinations, product

# ========== 数据初始化 ==========
tasks = list(range(1,11))
R = {1:15,2:11,3:4,4:11,5:18,6:8,7:19,8:5,9:9,10:13}
parking = ['P1','P2','P3','P4']
cranes = ['C1','C2']

transport_time = {
    ('P1','C1'):17, ('P2','C1'):15, ('P3','C1'):13, ('P4','C1'):11,
    ('P1','C2'):15, ('P2','C2'):13, ('P3','C2'):11, ('P4','C2'):9
}

# ========== 模型构建 ==========
model = lp.LpProblem("AGV_Scheduling_with_Conflict", lp.LpMinimize)

# ========== 变量定义 ==========
X = lp.LpVariable.dicts("X", [(i,p,c) for i in tasks for p in parking for c in cranes], cat='Binary')
D = lp.LpVariable.dicts("D", tasks, lowBound=0)
B = lp.LpVariable.dicts("B", tasks, lowBound=0)
C = lp.LpVariable.dicts("C", tasks, lowBound=0)
E = lp.LpVariable.dicts("E", tasks, lowBound=0)
C_max = lp.LpVariable("C_max", lowBound=0)
M = 1e5

# ========== 辅助变量定义（对应图片中的A_{i,t}） ==========
max_time = 200
time_points = range(max_time)
a = lp.LpVariable.dicts("occ", [(i,t) for i in tasks for t in time_points], cat='Binary')

# ========== 目标函数 ==========
model += C_max

# ========== 基础约束 ==========
for i in tasks:
    model += lp.lpSum(X[i,p,c] for p,c in product(parking,cranes)) == 1  # 公式1
    model += B[i] == D[i] + 13  # 公式2 B_i = D_i+13
    model += C[i] == B[i] + lp.lpSum(transport_time[(p,c)]*X[i,p,c] for p,c in product(parking,cranes))
    model += E[i] == C[i] + 20
    model += D[i] >= R[i]
    model += C_max >= E[i]

# ========== 图片公式3的行车区容量约束 ==========
for i in tasks:
    for t in time_points:
        # 定义逻辑与约束（替代原来的&运算符）
        model += a[i,t] <= (D[i] <= t)          # D_i <= t 时a[i,t]可能为1
        model += a[i,t] <= (t <= B[i]-1)        # t < B_i 时a[i,t]可能为1
        model += a[i,t] >= (D[i] <= t) + (t <= B[i]-1) - 1  # 两者满足时a[i,t]必须为1

for t in time_points:
    model += lp.lpSum(a[i,t] for i in tasks) <= 4  # ΣA_{i,t} ≤4

# ========== 图片公式4的停车位冲突约束 ==========
for p in parking:
    for i,j in combinations(tasks, 2):
        # 二元选择约束（大M法线性化）
        model += B[i] <= D[j] + M*(2 - X[i,p,cranes[0]] - X[j,p,cranes[0]])
        model += B[j] <= D[i] + M*(2 - X[i,p,cranes[1]] - X[j,p,cranes[1]])

# ========== 图片公式5的岸桥冲突约束 ==========
for c in cranes:
    for i,j in combinations(tasks, 2):
        # 时间间隔强制约束
        model += C[i] + 20 <= C[j] + M*(2 - X[i,parking[0],c] - X[j,parking[0],c])
        model += C[j] + 20 <= C[i] + M*(2 - X[i,parking[1],c] - X[j,parking[1],c])

# ========== 求解与输出 ==========
model.solve()
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