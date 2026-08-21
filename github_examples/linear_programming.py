# 某工厂生产甲、乙、丙三种产品，生产过程需消耗 A、B 两种原材料，
# 同时受生产线总产能限制。已知生产与收益相关数据如下：
# 单位产品利润：甲产品每件获利 10 元，乙产品每件获利 6 元，丙产品每件获利 4 元；
# 单位产品原材料消耗：
# 生产 1 件甲产品，消耗原材料 A 10 单位、原材料 B 2 单位；
# 生产 1 件乙产品，消耗原材料 A 4 单位、原材料 B 2 单位；
# 生产 1 件丙产品，消耗原材料 A 5 单位、原材料 B 6 单位；
# 资源总量限制：工厂当期可用原材料 A 总量为 600 单位，可用原材料 B 总量为 300 单位；
# 受生产线工时限制，三种产品的总产量不能超过 100 件；所有产品的产量均不能为负数。

# 作答要求：
# 1.建立该问题的线性规划数学模型，明确决策变量、目标函数和全部约束条件；
# 2.求解该线性规划问题，计算总利润最大化时，甲、乙、丙三种产品的最优产量，以及可获得的最大总利润；
# 3.计算各约束条件的对偶值（影子价格），并分别说明其经济含义；
# 4.计算各变量的检验数（简约成本），并分析丙产品未被纳入最优生产计划的原因。

#线性规划 Github 示例代码，用于演示 OR-Tools API 的使用方法。
from ortools.linear_solver import pywraplp  #从 ortools 这个大库的子模块 linear_solver 中取出 pywraplp 去使用

def Announce(solver, api_type):
    print(
        "---- Linear programming example with " + solver + " (" + api_type + ") -----"
    )


def RunLinearExampleNaturalLanguageAPI(optimization_problem_type):
    """Example of simple linear program with natural language API."""
    solver = pywraplp.Solver.CreateSolver(optimization_problem_type)
#pywraplp 是模块名，Solver 是其模块中的类名，CreateSolver 是这个类中的一个静态方法

    if not solver:
        return

    Announce(optimization_problem_type, "natural language API")
    # x1 , x2, x3 分别为甲乙丙的个数
    infinity = solver.infinity()    #这个是solver类中的固定方法，定义无穷大
    x1 = solver.NumVar(0.0, infinity, "x1")
    #这个也是solver类中的固定方法，用来定义范围，定义了 x1 的范围，下限为0，上限为无穷大，即 x1 >= 0
    x2 = solver.NumVar(0.0, infinity, "x2")
    x3 = solver.NumVar(0.0, infinity, "x3")

    #定义目标函数，solver.Maximize()告诉求解器，我们要最大化这个式子的值，后续会调用solver.Solver()去求出结果
    solver.Maximize(10 * x1 + 6 * x2 + 4 * x3)
    #定义约束条件，solver.Add()是定义约束条件的，属于固定用法
    c0 = solver.Add(10 * x1 + 4 * x2 + 5 * x3 <= 600)
    c1 = solver.Add(2 * x1 + 2 * x2 + 6 * x3 <= 300)
    sum_of_vars = sum([x1, x2, x3])
    c2 = solver.Add(sum_of_vars <= 100.0)

    SolveAndPrint(
        solver,
        [x1, x2, x3],
        [c0, c1, c2],
        optimization_problem_type != "PDLP"
    )
    # Print a linear expression's solution value.
    print("Sum of vars: %s = %s" % (sum_of_vars, sum_of_vars.solution_value()))


def RunLinearExampleCppStyleAPI(optimization_problem_type):
    """Example of simple linear program with the C++ style API."""
    solver = pywraplp.Solver.CreateSolver(optimization_problem_type)
    if not solver:
        return

    Announce(optimization_problem_type, "C++ style API")

    infinity = solver.infinity()
    # x1, x2 and x3 are continuous non-negative variables.
    x1 = solver.NumVar(0.0, infinity, "x1")
    x2 = solver.NumVar(0.0, infinity, "x2")
    x3 = solver.NumVar(0.0, infinity, "x3")

    # Maximize 10 * x1 + 6 * x2 + 4 * x3.
    objective = solver.Objective()
    objective.SetCoefficient(x1, 10)
    objective.SetCoefficient(x2, 6)
    objective.SetCoefficient(x3, 4)
    objective.SetMaximization()

    # x1 + x2 + x3 <= 100.
    c0 = solver.Constraint(-infinity, 100.0, "c0")
    c0.SetCoefficient(x1, 1)
    c0.SetCoefficient(x2, 1)
    c0.SetCoefficient(x3, 1)

    # 10 * x1 + 4 * x2 + 5 * x3 <= 600.
    c1 = solver.Constraint(-infinity, 600.0, "c1")
    c1.SetCoefficient(x1, 10)
    c1.SetCoefficient(x2, 4)
    c1.SetCoefficient(x3, 5)

    # 2 * x1 + 2 * x2 + 6 * x3 <= 300.
    c2 = solver.Constraint(-infinity, 300.0, "c2")
    c2.SetCoefficient(x1, 2)
    c2.SetCoefficient(x2, 2)
    c2.SetCoefficient(x3, 6)

    SolveAndPrint(
        solver, [x1, x2, x3], [c0, c1, c2], optimization_problem_type != "PDLP"
    )


def SolveAndPrint(solver, variable_list, constraint_list, is_precise):
    """Solve the problem and print the solution."""
    print("模型变量总数量 = %d" % solver.NumVariables())
    print("模型约束总条数 = %d" % solver.NumConstraints())

    result_status = solver.Solve()

    # The problem has an optimal solution.
    assert result_status == pywraplp.Solver.OPTIMAL

    # The solution looks legit (when using solvers others than
    # GLOP_LINEAR_PROGRAMMING, verifying the solution is highly recommended!).
    if is_precise:
        assert solver.VerifySolution(1e-7, True)

    print("求解耗时（毫秒）：%f" % solver.wall_time())

    # The objective value of the solution.
    print("目标函数最优值 = %f" % solver.Objective().Value())

    # The value of each variable in the solution.
    for variable in variable_list:
        print("变量%s 最优值 = %f" % (variable.name(), variable.solution_value()))

    print("Advanced usage:")
    print("单纯形迭代计算次数：%d" % solver.iterations())
    for variable in variable_list:
        print("变量%s: 缩减成本 = %f" % (variable.name(), variable.reduced_cost()))
    activities = solver.ComputeConstraintActivities()
    for i, constraint in enumerate(constraint_list):
        print(
            (
                "约束 %d: 影子价格 = %f\n               资源实际消耗量 = %f"
                % (i, constraint.dual_value(), activities[constraint.index()])
            )
        )


def main():
    RunLinearExampleNaturalLanguageAPI("GLOP")
    # RunLinearExampleNaturalLanguageAPI("GLPK_LP")
    RunLinearExampleNaturalLanguageAPI("CLP")
    RunLinearExampleNaturalLanguageAPI("PDLP")
    # RunLinearExampleNaturalLanguageAPI("XPRESS_LP")

    RunLinearExampleCppStyleAPI("GLOP")
    # RunLinearExampleCppStyleAPI("GLPK_LP")
    RunLinearExampleCppStyleAPI("CLP")
    RunLinearExampleCppStyleAPI("PDLP")
    # RunLinearExampleCppStyleAPI("XPRESS_LP")


if __name__ == "__main__":
    main()
