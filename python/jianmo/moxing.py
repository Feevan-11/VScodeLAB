import pulp as lp

# ========== 数据初始化 ==========
tasks = [1,2,3,4,5,6,7,8,9,10]
R = {1:15,2:11,3:4,4:11,5:18,6:8,7:19,8:5,9:9,10:13}
parking = ['P1','P2','P3','P4']
cranes = ['C1','C2']

transport_time = {
    ('P1','C1'):17, ('P2','C1'):15, ('P3','C1'):13, ('P4','C1'):11,
    ('P1','C2'):15, ('P2','C2'):13, ('P3','C2'):11, ('P4','C2'):9
}

# ========== 模型重建 ==========
model = lp.LpProblem("AGV_Scheduling_Fixed", lp.LpMinimize)

# ========== 变量定义 ==========
X = lp.LpVariable.dicts("X", [(i,p,c) for i in tasks for p in parking for c in cranes], cat='Binary')
D = lp.LpVariable.dicts("D", tasks, lowBound=0)  # 进入行车区时间
B = lp.LpVariable.dicts("B", tasks, lowBound=0)  # 进入缓冲区时间
C = lp.LpVariable.dicts("C", tasks, lowBound=0)  # 岸桥开始时间
E = lp.LpVariable.dicts("E", tasks, lowBound=0)  # 任务完成时间
C_max = lp.LpVariable("C_max")  # 最大完成时间

# ========== 目标函数 ==========
model += C_max

# ========== 基础约束 ==========
for i in tasks:
    # 分配约束
    model += lp.lpSum(X[i,p,c] for p in parking for c in cranes) == 1
    
    # 时间线关系
    model += B[i] == D[i] + 13
    model += C[i] == B[i] + lp.lpSum(transport_time[(p,c)]*X[i,p,c] for p in parking for c in cranes)
    model += E[i] == C[i] + 20
    
    # 准备时间约束
    model += D[i] >= R[i]
    
    # 完工时间
    model += C_max >= E[i]

# ========== 关键修复：行车区容量约束 ==========
# 方法1：时间离散化
max_time = 200
time_points = range(max_time)
a = lp.LpVariable.dicts("occ", [(i,t) for i in tasks for t in time_points], cat='Binary')

for i in tasks:
    for t in time_points:
        model += a[i,t] <= (D[i] <= t)          # t >= D[i]
        model += a[i,t] <= (t <= B[i] - 1)      # t < B[i]
        model += a[i,t] >= (D[i] <= t) + (t <= B[i] - 1) - 1

for t in time_points:
    model += lp.lpSum(a[i,t] for i in tasks) <= 4

# ========== 求解与验证 ==========
model.solve()

# 输出结果
print("Status:", lp.LpStatus[model.status])
print("Optimal C_max:", lp.value(C_max))

# 验证变量值
for i in tasks:
    print(f"Task {i}: D={lp.value(D[i])}, B={lp.value(B[i])}, C={lp.value(C[i])}, E={lp.value(E[i])}")