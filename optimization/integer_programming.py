# import ortools
# print("ortools 可用")

from ortools.linear_solver import pywraplp

# 1. 创建求解器，使用默认的线性规划求解器
solver = pywraplp.Solver.CreateSolver('GLOP')

# 2. 定义变量 x、y，取值范围 ≥0
x = solver.NumVar(0, solver.infinity(), 'x')
y = solver.NumVar(0, solver.infinity(), 'y')

# 3. 添加约束条件
# 约束1：x + 2y ≤ 14
solver.Add(x + 2 * y <= 14)
# 约束2：3x - y ≥ 0
solver.Add(3 * x - y >= 0)
# 约束3：x - y ≤ 2
solver.Add(x - y <= 2)

# 4. 定义目标函数：最大化 3x + 4y
solver.Maximize(3 * x + 4 * y)

# 5. 求解并输出结果
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print('找到最优解：')
    print(f'目标函数最大值 = {solver.Objective().Value()}')
    print(f'x = {x.solution_value()}')
    print(f'y = {y.solution_value()}')
else:
    print('未找到最优解')
