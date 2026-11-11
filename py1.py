# # # # student_name = 'du'
# # # # student_age = '17'
# # # # print(student_name,student_age)
# # #
# # # # 三目表达式
# # # #结果1 if 条件判断 else 结果2
# # #
# # # # 给定一个整数 `x`，用三目表达式判断：如果`x`大于等于0，返回字符串"非负数"，否则返回"负数"
# # # # x = 1
# # # # print("非负数") if x>=0 else print("负数")
# # # # 给定两个数值 `a` 和 `b`，用三目表达式直接返回两者中较大的那个数。
# # # # a = float(input("请输入a的值："))
# # # # b = float(input("请输入b的值："))
# # # # max_num = a if a>b else b
# # # # print("最大的值为:%f" %max_num)
# # # # 给定一个字符串 `s`，用三目表达式判断：如果字符串长度大于 5，返回"长字符串"，否则返回"短字符串"
# # # # s = input("请输入一个字符串：")
# # # # print("长字符串") if len(s) > 5 else print("短字符串")
# # # # 给定一个年份 `year`，用三目表达式判断是否为闰年，返回 `"闰年"` 或 `"平年"`。
# # # # 闰年规则：能被 4 整除但不能被 100 整除，或者能被 400 整除。
# # # # year = int(input("请输入一个年份："))
# # # # print("闰年") if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0) else print("平年")
# # # # 给定一个整数 `num`，用三目表达式判断：如果是偶数返回布尔值 `True`，奇数返回 `False`。
# # # # num = int(input("请输入一个整数："))
# # # # print("True") if num % 2 == 0 else print("False")
# # # # 给定学生分数 `score`（0~100 区间），用**嵌套三目表达式**划分等级： 90 分及以上为 `"优秀"`，60~89 分为 `"及格"`，60 分以下为 `"不及格"`。
# # # # score = int(input("请输入学生分数："))
# # # # if (score > 100 or score < 0) :
# # # #     print("分数有问题")
# # # # elif score >= 90 :
# # # #     print("优秀")
# # # # elif score >= 60 :
# # # #     print("及格")
# # # # else:
# # # #     print("不及格")
# # # # 1. 给定三个数 `x, y, z`，只用三目表达式返回三个数中的最大值。
# # # # a = float(input("请输入a的值："))
# # # # b = float(input("请输入b的值："))
# # # # c = float(input("请输入c的值："))
# # # # max = a if a > b and a > c else b if b > c else c
# # # # print("最大的值为：",max)
# # # # 2. 结合列表推导式：给定列表 `nums = [3, 7, 12, 5, 18, 20]`，用三目表达式配合列表推导，将列表中大于 10 的数字替换为 `"大"`，小于等于 10 的替换为 `"小"`。
# # # # s = 0
# # # # for i in range(1,101):
# # # #     s += i
# # # # print(s)
# # # # sum = 0
# # # # i = 1
# # # # while i<=100:
# # # #     sum += i
# # # #     i += 1
# # # # print(sum)
# # #
# # # # i = 0
# # # # while i < 10:
# # # #     print(i)
# # # #     if i == 3:
# # # #         i += 1
# # # #         continue
# # # #     i += 1
# # #
# # # # for i in range(10):
# # # #     if i== 3:
# # # #         continue
# # # #     print(i)
# # #
# # # # name = "jiangwangwen"
# # # # print("ag" in name)
# # # #
# # # # a = "jiang"
# # # # b = "jiang"
# # # # print(id(a))
# # # # print(id(b))
# # # # print(a is b)
# # #
# # # # s = {1,2,3,5}
# # # # # s.discard(2)
# # # # s.pop()
# # # # print(s)
# # #
# # # # list = [1,2,"a"]
# # # # list.append(1)
# # # # print(list)
# # # # list.pop()
# # # # print(list)
# # # # list.pop(1)
# # # # print(list)
# # #
# # # import ortools
# # # # print("可用")
# # #
# # # import requests
# # # import time
# # # from bs4 import BeautifulSoup
# # # import pandas as pd
# # #
# # # # print("爬虫环境就绪")
# # #
# # # url = "https://books.toscrape.com/"
# # # response = requests.get(url)
# # # # print("状态码：",response.status_code)
# # # # print(response.text[:500])
# # # html = response.text
# # # soup = BeautifulSoup(html, "html.parser")
# # # books = soup.find_all("article",class_="product_pod")
# # #
# # # data_list = []
# # # for book in books:
# # #     book_name = book.find("h3").find("a")["title"]
# # #     book_price = book.find("p",class_="price_color").text
# # #     data_list.append({
# # #         "书名":book_name,
# # #         "价格":book_price
# # #     })
# # # df = pd.DataFrame(data_list)
# # # df.to_csv("图书数据.csv",index=False,encoding="utf-8-sig")
# # # print("保存完成！共爬取",len(data_list),"本书")
# # # time.sleep(10)
# # # import pandas as pd
# # # print(pd.__version__)
# # # from sympy import symbols, diff, solve, simplify, sqrt, latex
# # #
# # # # 定义全部符号变量
# # # a, b, w, lambda_, e, q, c, v, s, k, u, p = symbols(
# # #     'a b w lambda e q c v s k u p', real=True
# # # )
# # #
# # # # 1. 零售商最优定价 p(e)
# # # Pi_R = (p - w) * (a - b * p + lambda_ * e)
# # # dp = diff(Pi_R, p)
# # # p_opt = solve(dp, p)[0]
# # # p_opt = simplify(p_opt)
# # #
# # # print("=" * 50)
# # # print("零售商最优零售价 p(e)：")
# # # print(p_opt)
# # #
# # # # 2. 代入制造商期望利润函数
# # # d = a - b * p_opt + lambda_ * e
# # # Pi_M = w * d / 2 - v * d**2 / (8 * w * q) - c * q - (1 - s) * k * e**2 / 2
# # #
# # # #3. 对 q 求一阶条件，解 q(e)
# # # dq = diff(Pi_M, q)
# # # q_sol = solve(dq, q)
# # # # 【修正】纯符号无法自动判正负，二次方程两个根：先负后正，手动取第2个正根
# # # q_of_e = q_sol[1]
# # # q_of_e = simplify(q_of_e)
# # #
# # # print("=" * 50)
# # # print("最优投入量 q(e)：")
# # # print(q_of_e)
# # #
# # # # 4. 代入 q(e)，对 e 求导，解最优 e1
# # # Pi_M_e = Pi_M.subs(q, q_of_e)
# # # de = diff(Pi_M_e, e)
# # # e_sol = solve(de, e)
# # # # 【修正】同样手动取第2个正根（经济可行解）
# # # e1 = e_sol[1]
# # # e1 = simplify(e1)
# # #
# # # print("=" * 50)
# # # print("命题1 最优碳减排水平 e1：")
# # # print(e1)
# # #
# # # # 5. 回代求 q1、p1
# # # q1 = simplify(q_of_e.subs(e, e1))
# # # p1 = simplify(p_opt.subs(e, e1))
# # #
# # # print("=" * 50)
# # # print("命题1 最优投入量 q1：")
# # # print(q1)
# # # print("命题1 最优零售价格 p1：")
# # # print(p1)
# # #
# # # #  6. 双方最优期望利润
# # # Pi_M1 = simplify(Pi_M.subs({q: q1, e: e1}))
# # # Pi_R1 = simplify(Pi_R.subs({p: p1, e: e1}))
# # #
# # # print("=" * 50)
# # # print("制造商最优期望利润 Π_M1：")
# # # print(Pi_M1)
# # # print("零售商最优期望利润 Π_R1：")
# # # print(Pi_R1)
# # #
# # # #  7. 中间变量 t1
# # # t1 = simplify(sqrt(u * v / (8 * c)))
# # # print("=" * 50)
# # # print("中间变量 t1：")
# # # print(t1)
# #
# # # import sympy as sp
# # #
# # # # 1. 定义符号变量
# # # # 决策变量
# # # e, q, p = sp.symbols('e q p', real=True, positive=True)
# # # # 外生参数
# # # a, b, w, v, c, k, s, lam, u = sp.symbols('a b w v c k s lam u', real=True, positive=True)
# # #
# # # # 2. 需求函数（代入零售商最优定价前）
# # # d = a - b * p + lam * e
# # #
# # # # 3. 零售商利润函数
# # # Pi_R = (p - w) * d
# # # # 对 p 求一阶导，令其为0
# # # dPi_R_dp = sp.diff(Pi_R, p)
# # # # 解出 p*(e)
# # # p_star = sp.solve(sp.Eq(dPi_R_dp, 0), p)[0]
# # # print("零售商最优反应函数 p*(e) =", p_star)
# # #
# # # # 4. 把 p*(e) 代入需求函数，得到 d 关于 e 的表达式
# # # d_sub = d.subs(p, p_star)
# # # d_sub = sp.simplify(d_sub)  # 化简，得到 (a - bw + lam*e)/2
# # # print("代入后的需求 d(e) =", d_sub)
# # #
# # # # 5. 写出制造商利润函数（直接按论文式2的形式）
# # # d_paper = (a - b * w + lam * e) / 2
# # # Pi_M = w * d_paper - v * d_paper**2 / (2*u*q) - c*q - (1-s)*k*e**2 / 2
# # #
# # # # 6. 对 e 和 q 求偏导，解方程组
# # # dPi_M_de = sp.diff(Pi_M, e)
# # # dPi_M_dq = sp.diff(Pi_M, q)
# # #
# # # # 解方程组 dPi_M/de = 0, dPi_M/dq = 0
# # # sol = sp.solve([dPi_M_de, dPi_M_dq], [e, q], dict=True)
# # # print("方程组的解：")
# # # for sol_i in sol:
# # #     print("e* =", sp.simplify(sol_i[e]))
# # #     print("q* =", sp.simplify(sol_i[q]))
# # #
# # # # 7. 引入 t1 = sqrt(u*v/(8*c))，验证是否与论文一致
# # # t1 = sp.sqrt(u*v/(8*c))
# # # # 提取出 e* 和 q* 的表达式
# # # e_star = sol[0][e]
# # # q_star = sol[0][q]
# # #
# # # # 用 t1 替换掉 sqrt(u*v/(8*c))，看看化简后的结果
# # # e_paper = lam*(2*w*t1 - v) / (4*(1-s)*k*t1)
# # # q_paper = (a - b*w)*t1/u + lam**2*(2*w*t1 - v) / (4*(1-s)*u*k)
# # #
# # # # 计算 e* 和论文 e_paper 的差值，如果为0说明完全一致
# # # diff_e = sp.simplify(e_star - e_paper)
# # # print("e* 与论文公式的差值（应为0）：", diff_e)
# # #
# # # # 随便取一组满足假设的数值
# # # vals = {a: 300, b: 4, w: 66, v: 40, c: 5, k: 6, s: 0.5, lam: 3, u: 1}
# # # print("数值验证 e*：", sp.N(e_star.subs(vals)))
# # # print("数值验证 e_paper：", sp.N(e_paper.subs(vals)))
# # #
# # # import sympy as sp
# # # import matplotlib.pyplot as plt
# # # plt.rcParams['font.sans-serif'] = ['SimHei']
# # # plt.rcParams['axes.unicode_minus'] = False
# # # # 定义符号
# # # e, q, p = sp.symbols('e q p', real=True, positive=True)
# # # a, b, w, v, c, k, s, lam, u = sp.symbols('a b w v c k s lam u', real=True, positive=True)
# # #
# # # # 定义 t1
# # # t1 = sp.sqrt(u * v / (8 * c))
# # #
# # # # 论文里的最优解
# # # e_paper = lam * (2 * w * t1 - v) / (4 * (1 - s) * k * t1)
# # # q_paper = (a - b * w) * t1 / u + lam**2 * (2 * w * t1 - v) / (4 * (1 - s) * u * k)
# # # p_paper = (a + b * w) / (2 * b) + lam**2 * (2 * w * t1 - v) / (8 * b * k * (1 - s) * t1)
# # #
# # # # 数值代入
# # # vals = {a: 300, b: 4, w: 66, v: 40, c: 5, k: 6, s: 0.5, lam: 3, u: 1}
# # #
# # # print("论文 e_paper =", sp.N(e_paper.subs(vals)))  # 应该输出 23
# # # print("论文 q_paper =", sp.N(q_paper.subs(vals)))  # 应该输出 105
# # # print("论文 p_paper =", sp.N(p_paper.subs(vals)))  # 应该输出对应的值
# # #
# # # # 验证利润函数
# # # d_paper = (a - b * w + lam * e_paper) / 2
# # # Pi_M_paper = w * d_paper - v * d_paper**2 / (2 * u * q_paper) - c * q_paper - (1 - s) * k * e_paper**2 / 2
# # # print("论文 Pi_M =", sp.N(Pi_M_paper.subs(vals)))
# # #
# # # import numpy as np
# # # import matplotlib.pyplot as plt
# # #
# # # def compute_decisions(u, v, s, lam, a, b, w, c, k):
# # #     """
# # #     计算分散决策下（基本模型）的最优决策 e1, q1, p1
# # #     """
# # #     t1 = np.sqrt(u * v / (8 * c))
# # #     e1 = lam * (2 * w * t1 - v) / (4 * (1 - s) * k * t1)
# # #     q1 = (a - b * w) * t1 / u + lam**2 * (2 * w * t1 - v) / (4 * (1 - s) * u * k)
# # #     p1 = (a + b * w) / (2 * b) + lam**2 * (2 * w * t1 - v) / (8 * b * k * (1 - s) * t1)
# # #     return e1, q1, p1
# # #
# # # a = 300
# # # b = 4
# # # w = 66
# # # c = 5
# # # k = 6
# # # s = 0.5     # 图1设定 s = 0.5
# # # lam = 3     # 图1设定 lambda = 3
# # # v = 40
# # #
# # #
# # # u_vals = np.linspace(0.25, 1.0, 100)  # u 从 0.25 到 1.0
# # #
# # # # 计算不同 u 下的 e1, q1, p1
# # # e1_list, q1_list, p1_list = [], [], []
# # # for u in u_vals:
# # #     e1, q1, p1 = compute_decisions(u, v, s, lam, a, b, w, c, k)
# # #     e1_list.append(e1)
# # #     q1_list.append(q1)
# # #     p1_list.append(p1)
# # #
# # #
# # # fig, axes = plt.subplots(1, 3, figsize=(15, 4))
# # #
# # # # 图1(a): u 对碳减排水平 e1 的影响
# # # axes[0].plot(u_vals, e1_list, 'b-', linewidth=2)
# # # axes[0].set_xlabel('产出水平 u', fontsize=12)
# # # axes[0].set_ylabel('碳减排水平 e1', fontsize=12)
# # # axes[0].set_title('(a) 产出水平对碳减排水平的影响', fontsize=12)
# # # axes[0].grid(True, linestyle='--', alpha=0.6)
# # #
# # # # 图1(b): u 对投入量 q1 的影响
# # # axes[1].plot(u_vals, q1_list, 'r-', linewidth=2)
# # # axes[1].set_xlabel('产出水平 u', fontsize=12)
# # # axes[1].set_ylabel('投入量 q1', fontsize=12)
# # # axes[1].set_title('(b) 产出水平对投入量的影响', fontsize=12)
# # # axes[1].grid(True, linestyle='--', alpha=0.6)
# # #
# # # # 图1(c): u 对零售价格 p1 的影响
# # # axes[2].plot(u_vals, p1_list, 'g-', linewidth=2)
# # # axes[2].set_xlabel('产出水平 u', fontsize=12)
# # # axes[2].set_ylabel('零售价格 p1', fontsize=12)
# # # axes[2].set_title('(c) 产出水平对零售价格的影响', fontsize=12)
# # # axes[2].grid(True, linestyle='--', alpha=0.6)
# # #
# # # plt.tight_layout()
# # # plt.show()
# # import sympy as sp
# #
# # w, p, e, g, r, phi, t, gamma = sp.symbols('w p e g r phi t gamma', real=True, positive=True)
# #
# # def solve_noncooperative(subsidy_type):
# #     """
# #     求解非合作广告 (N) 下的三种补贴情况
# #     subsidy_type: 'N' (无补贴), 'A' (广告补贴), 'P' (消费补贴)
# #     """
# #     # 1. 需求函数
# #     if subsidy_type == 'P':
# #         # 消费补贴：消费者实际支付 p - r
# #         D = 1 + e * g - (p - r)
# #     else:
# #         # 无补贴 或 广告补贴
# #         D = 1 + e * g - p
# #
# #     # 2. 利润函数
# #     pi_M = w * D
# #     if subsidy_type == 'A':
# #         # 广告补贴：政府分担 phi 比例的广告成本
# #         pi_R = (p - w) * D - (1 - phi) * e ** 2
# #     else:
# #         pi_R = (p - w) * D - e ** 2
# #
# #     # 3. 零售商决策 (求 p 和 e)
# #     dpi_R_dp = sp.diff(pi_R, p)
# #     dpi_R_de = sp.diff(pi_R, e)
# #     sol_R = sp.solve([dpi_R_dp, dpi_R_de], [p, e], dict=True)[0]
# #     p_star, e_star = sol_R[p], sol_R[e]
# #
# #     # 4. 制造商决策 (求 w)
# #     pi_M_sub = pi_M.subs({p: p_star, e: e_star})
# #     dpi_M_dw = sp.diff(pi_M_sub, w)
# #     w_opt = sp.solve(dpi_M_dw, w)[0]
# #
# #     # 5. 回代求 p, e, D
# #     p_opt = sp.simplify(p_star.subs(w, w_opt))
# #     e_opt = sp.simplify(e_star.subs(w, w_opt))
# #     D_opt = sp.simplify(D.subs({p: p_opt, e: e_opt, w: w_opt}))
# #
# #     # 6. 政府决策 (如果有补贴)
# #     if subsidy_type == 'A':
# #         # 政府选择 phi 最大化 SW (SW = pD - e^2 + D^2/2)
# #         SW = p * D - e ** 2 + D ** 2 / 2
# #         SW_sub = SW.subs({p: p_opt, e: e_opt, w: w_opt})
# #         phi_opt = sp.solve(sp.diff(SW_sub, phi), phi)[0]
# #
# #         # 最终回代
# #         p_final = sp.simplify(p_opt.subs(phi, phi_opt))
# #         e_final = sp.simplify(e_opt.subs(phi, phi_opt))
# #         w_final = sp.simplify(w_opt.subs(phi, phi_opt))
# #         D_final = sp.simplify(D_opt.subs(phi, phi_opt))
# #         print(f"最优广告补贴比例 phi* = {sp.simplify(phi_opt)}")
# #
# #     elif subsidy_type == 'P':
# #         # 政府选择 r 最大化 SW (SW = pD - e^2 + D^2/2 - rD)
# #         SW = p * D - e ** 2 + D ** 2 / 2 - r * D
# #         SW_sub = SW.subs({p: p_opt, e: e_opt, w: w_opt})
# #         r_opt = sp.solve(sp.diff(SW_sub, r), r)[0]
# #
# #         # 最终回代
# #         p_final = sp.simplify(p_opt.subs(r, r_opt))
# #         e_final = sp.simplify(e_opt.subs(r, r_opt))
# #         w_final = sp.simplify(w_opt.subs(r, r_opt))
# #         D_final = sp.simplify(D_opt.subs(r, r_opt))
# #         print(f"最优消费补贴 r* = {sp.simplify(r_opt)}")
# #
# #     else:  # 无补贴
# #         p_final, e_final, w_final, D_final = p_opt, e_opt, w_opt, D_opt
# #
# #     # 7. 计算最终结果
# #     pi_M_final = sp.simplify(pi_M.subs({p: p_final, e: e_final, w: w_final}))
# #     pi_R_final = sp.simplify(pi_R.subs({p: p_final, e: e_final, w: w_final}))
# #     CS_final = sp.simplify(D_final ** 2 / 2)
# #
# #     if subsidy_type == 'A':
# #         SW_final = sp.simplify(pi_M_final + pi_R_final + CS_final)
# #     elif subsidy_type == 'P':
# #         SW_final = sp.simplify(pi_M_final + pi_R_final + CS_final - r_opt * D_final)
# #     else:
# #         SW_final = sp.simplify(pi_M_final + pi_R_final + CS_final)
# #
# #     print(f"最优批发价 w* = {w_final}")
# #     print(f"最优零售价 p* = {p_final}")
# #     print(f"最优广告水平 e* = {e_final}")
# #     print(f"制造商利润 π_M* = {pi_M_final}")
# #     print(f"零售商利润 π_R* = {pi_R_final}")
# #     print(f"消费者剩余 CS* = {CS_final}")
# #     print(f"社会福利 SW* = {SW_final}")
# #     print(" ")
# #
# #
# # def solve_cooperative(subsidy_type):
# #     """
# #     求解合作广告 (C) 下的三种补贴情况
# #     subsidy_type: 'N' (无补贴), 'A' (广告补贴), 'P' (消费补贴)
# #     """
# #
# #     # 1. 需求函数 (合作广告引入负面影响)
# #     if subsidy_type == 'P':
# #         D = 1 + gamma * e * g - (p - r)
# #     else:
# #         D = 1 + gamma * e * g - p
# #
# #     # 2. 利润函数 (合作广告制造商分担 t 比例，政府可能分担 phi)
# #     pi_M = w * D - t * e ** 2
# #     if subsidy_type == 'A':
# #         pi_R = (p - w) * D - (1 - t - phi) * e ** 2
# #     else:
# #         pi_R = (p - w) * D - (1 - t) * e ** 2
# #
# #     # 3. 零售商决策 (求 p 和 e)
# #     dpi_R_dp = sp.diff(pi_R, p)
# #     dpi_R_de = sp.diff(pi_R, e)
# #     sol_R = sp.solve([dpi_R_dp, dpi_R_de], [p, e], dict=True)[0]
# #     p_star, e_star = sol_R[p], sol_R[e]
# #
# #     # 4. 制造商决策 (求 w 和 t)
# #     pi_M_sub = pi_M.subs({p: p_star, e: e_star})
# #     dpi_M_dw = sp.diff(pi_M_sub, w)
# #     dpi_M_dt = sp.diff(pi_M_sub, t)
# #     sol_M = sp.solve([dpi_M_dw, dpi_M_dt], [w, t], dict=True)[0]
# #     w_opt, t_opt = sol_M[w], sol_M[t]
# #
# #     # 5. 回代求 p, e, D
# #     p_opt = sp.simplify(p_star.subs({w: w_opt, t: t_opt}))
# #     e_opt = sp.simplify(e_star.subs({w: w_opt, t: t_opt}))
# #     D_opt = sp.simplify(D.subs({p: p_opt, e: e_opt, w: w_opt, t: t_opt}))
# #
# #     # 6. 政府决策
# #     if subsidy_type == 'A':
# #         SW = p * D - e ** 2 + D ** 2 / 2
# #         SW_sub = SW.subs({p: p_opt, e: e_opt, w: w_opt, t: t_opt})
# #         phi_opt = sp.solve(sp.diff(SW_sub, phi), phi)[0]
# #
# #         p_final = sp.simplify(p_opt.subs(phi, phi_opt))
# #         e_final = sp.simplify(e_opt.subs(phi, phi_opt))
# #         w_final = sp.simplify(w_opt.subs(phi, phi_opt))
# #         t_final = sp.simplify(t_opt.subs(phi, phi_opt))
# #         D_final = sp.simplify(D_opt.subs(phi, phi_opt))
# #         print(f"最优广告补贴比例 phi* = {sp.simplify(phi_opt)}")
# #         print(f"最优合作参与率 t* = {t_final}")
# #
# #     elif subsidy_type == 'P':
# #         SW = p * D - e ** 2 + D ** 2 / 2 - r * D
# #         SW_sub = SW.subs({p: p_opt, e: e_opt, w: w_opt, t: t_opt})
# #         r_opt = sp.solve(sp.diff(SW_sub, r), r)[0]
# #
# #         p_final = sp.simplify(p_opt.subs(r, r_opt))
# #         e_final = sp.simplify(e_opt.subs(r, r_opt))
# #         w_final = sp.simplify(w_opt.subs(r, r_opt))
# #         t_final = sp.simplify(t_opt.subs(r, r_opt))
# #         D_final = sp.simplify(D_opt.subs(r, r_opt))
# #         print(f"最优消费补贴 r* = {sp.simplify(r_opt)}")
# #         print(f"最优合作参与率 t* = {t_final}")
# #
# #     else:
# #         p_final, e_final, w_final, t_final, D_final = p_opt, e_opt, w_opt, t_opt, D_opt
# #         print(f"最优合作参与率 t* = {t_final}")
# #
# #     # 7. 最终结果
# #     pi_M_final = sp.simplify(pi_M.subs({p: p_final, e: e_final, w: w_final, t: t_final}))
# #     pi_R_final = sp.simplify(pi_R.subs({p: p_final, e: e_final, w: w_final, t: t_final}))
# #     CS_final = sp.simplify(D_final ** 2 / 2)
# #
# #     if subsidy_type == 'A':
# #         SW_final = sp.simplify(pi_M_final + pi_R_final + CS_final)
# #     elif subsidy_type == 'P':
# #         SW_final = sp.simplify(pi_M_final + pi_R_final + CS_final - r_opt * D_final)
# #     else:
# #         SW_final = sp.simplify(pi_M_final + pi_R_final + CS_final)
# #
# #     print(f"最优批发价 w* = {w_final}")
# #     print(f"最优零售价 p* = {p_final}")
# #     print(f"最优广告水平 e* = {e_final}")
# #     print(f"制造商利润 π_M* = {pi_M_final}")
# #     print(f"零售商利润 π_R* = {pi_R_final}")
# #     print(f"消费者剩余 CS* = {CS_final}")
# #     print(f"社会福利 SW* = {SW_final}")
# #     print(" ")
# #
# #
# # if __name__ == '__main__':
# #     # 运行全部 6 种情况
# #     solve_noncooperative('N')
# #     solve_noncooperative('A')
# #     solve_noncooperative('P')
# #
# #     solve_cooperative('N')
# #     solve_cooperative('A')
# #     solve_cooperative('P')
# #
# # import sympy as sp
# # import numpy as np
# # import matplotlib.pyplot as plt
# # plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows黑体
# # plt.rcParams['axes.unicode_minus'] = False    # 解决负号变成方框
# #
# # # ==========================================
# # # 定义全局符号
# # # ==========================================
# # w, p, e, g, r, phi, t, gamma = sp.symbols('w p e g r phi t gamma', real=True, positive=True)
# #
# #
# # # ==========================================
# # # 第一部分：符号推导 (SymPy)
# # # ==========================================
# # def derive_all_cases():
# #     """推导 6 种情况下的所有均衡结果，并返回一个包含公式的字典"""
# #     results = {}
# #
# #     # ---------- 非合作广告 (N) ----------
# #     def solve_N(subsidy_type):
# #         D = 1 + e * g - (p - r) if subsidy_type == 'P' else 1 + e * g - p
# #         pi_M = w * D
# #         pi_R = (p - w) * D - (1 - phi) * e ** 2 if subsidy_type == 'A' else (p - w) * D - e ** 2
# #
# #         # 零售商决策
# #         sol_R = sp.solve([sp.diff(pi_R, p), sp.diff(pi_R, e)], [p, e], dict=True)[0]
# #         p_star, e_star = sol_R[p], sol_R[e]
# #
# #         # 制造商决策
# #         pi_M_sub = pi_M.subs({p: p_star, e: e_star})
# #         w_opt = sp.solve(sp.diff(pi_M_sub, w), w)[0]
# #
# #         # 回代
# #         p_opt = sp.simplify(p_star.subs(w, w_opt))
# #         e_opt = sp.simplify(e_star.subs(w, w_opt))
# #         D_opt = sp.simplify(D.subs({p: p_opt, e: e_opt, w: w_opt}))
# #
# #         # 政府决策
# #         if subsidy_type == 'A':
# #             SW = p * D - e ** 2 + D ** 2 / 2
# #             phi_opt = sp.solve(sp.diff(SW.subs({p: p_opt, e: e_opt, w: w_opt}), phi), phi)[0]
# #             p_opt, e_opt, w_opt, D_opt = [sp.simplify(x.subs(phi, phi_opt)) for x in [p_opt, e_opt, w_opt, D_opt]]
# #             return {'w': w_opt, 'p': p_opt, 'e': e_opt, 'D': D_opt, 'phi': phi_opt, 'r': 0, 't': 0}
# #         elif subsidy_type == 'P':
# #             SW = p * D - e ** 2 + D ** 2 / 2 - r * D
# #             r_opt = sp.solve(sp.diff(SW.subs({p: p_opt, e: e_opt, w: w_opt}), r), r)[0]
# #             p_opt, e_opt, w_opt, D_opt = [sp.simplify(x.subs(r, r_opt)) for x in [p_opt, e_opt, w_opt, D_opt]]
# #             return {'w': w_opt, 'p': p_opt, 'e': e_opt, 'D': D_opt, 'phi': 0, 'r': r_opt, 't': 0}
# #         else:
# #             return {'w': w_opt, 'p': p_opt, 'e': e_opt, 'D': D_opt, 'phi': 0, 'r': 0, 't': 0}
# #
# #     # ---------- 合作广告 (C) ----------
# #     def solve_C(subsidy_type):
# #         D = 1 + gamma * e * g - (p - r) if subsidy_type == 'P' else 1 + gamma * e * g - p
# #         pi_M = w * D - t * e ** 2
# #         pi_R = (p - w) * D - (1 - t - phi) * e ** 2 if subsidy_type == 'A' else (p - w) * D - (1 - t) * e ** 2
# #
# #         # 零售商决策
# #         sol_R = sp.solve([sp.diff(pi_R, p), sp.diff(pi_R, e)], [p, e], dict=True)[0]
# #         p_star, e_star = sol_R[p], sol_R[e]
# #
# #         # 制造商决策
# #         pi_M_sub = pi_M.subs({p: p_star, e: e_star})
# #         sol_M = sp.solve([sp.diff(pi_M_sub, w), sp.diff(pi_M_sub, t)], [w, t], dict=True)[0]
# #         w_opt, t_opt = sol_M[w], sol_M[t]
# #
# #         # 回代
# #         p_opt = sp.simplify(p_star.subs({w: w_opt, t: t_opt}))
# #         e_opt = sp.simplify(e_star.subs({w: w_opt, t: t_opt}))
# #         D_opt = sp.simplify(D.subs({p: p_opt, e: e_opt, w: w_opt, t: t_opt}))
# #
# #         # 政府决策
# #         if subsidy_type == 'A':
# #             SW = p * D - e ** 2 + D ** 2 / 2
# #             phi_opt = sp.solve(sp.diff(SW.subs({p: p_opt, e: e_opt, w: w_opt, t: t_opt}), phi), phi)[0]
# #             p_opt, e_opt, w_opt, t_opt, D_opt = [sp.simplify(x.subs(phi, phi_opt)) for x in
# #                                                  [p_opt, e_opt, w_opt, t_opt, D_opt]]
# #             return {'w': w_opt, 'p': p_opt, 'e': e_opt, 'D': D_opt, 'phi': phi_opt, 'r': 0, 't': t_opt}
# #         elif subsidy_type == 'P':
# #             SW = p * D - e ** 2 + D ** 2 / 2 - r * D
# #             r_opt = sp.solve(sp.diff(SW.subs({p: p_opt, e: e_opt, w: w_opt, t: t_opt}), r), r)[0]
# #             p_opt, e_opt, w_opt, t_opt, D_opt = [sp.simplify(x.subs(r, r_opt)) for x in
# #                                                  [p_opt, e_opt, w_opt, t_opt, D_opt]]
# #             return {'w': w_opt, 'p': p_opt, 'e': e_opt, 'D': D_opt, 'phi': 0, 'r': r_opt, 't': t_opt}
# #         else:
# #             return {'w': w_opt, 'p': p_opt, 'e': e_opt, 'D': D_opt, 'phi': 0, 'r': 0, 't': t_opt}
# #
# #     # 运行所有 6 种情况
# #     print("正在推导公式，请稍候...")
# #     results['NN'] = solve_N('N')
# #     results['NA'] = solve_N('A')
# #     results['NP'] = solve_N('P')
# #     results['CN'] = solve_C('N')
# #     results['CA'] = solve_C('A')
# #     results['CP'] = solve_C('P')
# #     print("公式推导完成！\n")
# #     return results
# #
# #
# # # ==========================================
# # # 第二部分：数值转换与可视化 (NumPy + Matplotlib)
# # # ==========================================
# # def plot_results(results):
# #     """将符号公式转换为数值，并绘制图像"""
# #
# #     # 固定 gamma（合作广告负面效应）为 0.8，观察 g 变化的影响
# #     gamma_val = 0.8
# #     g_vals = np.linspace(0.01, 0.99, 100)  # 绿色水平从 0 到 1
# #
# #     # 将 SymPy 公式转换为 NumPy 可以计算的函数
# #     def expr_to_func(expr):
# #         return sp.lambdify((g, gamma), expr, 'numpy')
# #
# #     # 提取我们要画图的指标（这里以广告水平 e 和 消费者剩余 CS 为例）
# #     metrics = {
# #         '广告水平 e': {},
# #         '消费者剩余 CS': {}
# #     }
# #
# #     for case_name, case_data in results.items():
# #         # 计算 e
# #         e_func = expr_to_func(case_data['e'])
# #         metrics['广告水平 e'][case_name] = e_func(g_vals, gamma_val)
# #
# #         # 计算 CS = D^2 / 2
# #         D_func = expr_to_func(case_data['D'])
# #         D_vals = D_func(g_vals, gamma_val)
# #         metrics['消费者剩余 CS'][case_name] = D_vals ** 2 / 2
# #
# #     # ---- 开始绘图 ----
# #     fig, axes = plt.subplots(1, 2, figsize=(14, 6))
# #     colors = {'NN': 'blue', 'NA': 'orange', 'NP': 'green',
# #               'CN': 'red', 'CA': 'purple', 'CP': 'brown'}
# #     linestyles = {'NN': '-', 'NA': '--', 'NP': '-.',
# #                   'CN': '-', 'CA': '--', 'CP': '-.'}
# #
# #     # 子图 1: 广告水平 e 随 g 的变化
# #     ax1 = axes[0]
# #     for case_name, vals in metrics['广告水平 e'].items():
# #         ax1.plot(g_vals, vals, label=case_name, color=colors[case_name],
# #                  linestyle=linestyles[case_name], linewidth=2)
# #     ax1.set_xlabel('产品绿色水平 (g)', fontsize=12)
# #     ax1.set_ylabel('最优广告水平 (e*)', fontsize=12)
# #     ax1.set_title(f'广告水平随 g 的变化 (γ = {gamma_val})', fontsize=14)
# #     ax1.legend()
# #     ax1.grid(True, alpha=0.3)
# #
# #     # 子图 2: 消费者剩余 CS 随 g 的变化
# #     ax2 = axes[1]
# #     for case_name, vals in metrics['消费者剩余 CS'].items():
# #         ax2.plot(g_vals, vals, label=case_name, color=colors[case_name],
# #                  linestyle=linestyles[case_name], linewidth=2)
# #     ax2.set_xlabel('产品绿色水平 (g)', fontsize=12)
# #     ax2.set_ylabel('消费者剩余 (CS*)', fontsize=12)
# #     ax2.set_title(f'消费者剩余随 g 的变化 (γ = {gamma_val})', fontsize=14)
# #     ax2.legend()
# #     ax2.grid(True, alpha=0.3)
# #
# #     plt.tight_layout()
# #     plt.show()
# #
# #
# # if __name__ == '__main__':
# #     # 1. 推导公式
# #     results = derive_all_cases()
# #
# #     # 2. 打印部分关键结果供核对
# #     print("=" * 60)
# #     print("部分关键结果核对 (Case NN):")
# #     print(f"最优批发价 w* = {results['NN']['w']}")
# #     print(f"最优广告水平 e* = {results['NN']['e']}")
# #     print(f"最优零售价 p* = {results['NN']['p']}")
# #     print("=" * 60)
# #
# #     # 3. 可视化
# #     print("\n正在生成图像，请稍候...")
# #     plot_results(results)
#
# import torch
# import torch.nn as nn
# import torch.optim as optim
# from torch.utils.data import DataLoader, TensorDataset, random_split
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.datasets import load_digits
# from sklearn.preprocessing import StandardScaler
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# class MLP(nn.Module):
#     def __init__(self, input_dim, hidden_dims, output_dim):
#         super(MLP, self).__init__()
#         layers = []
#         prev = input_dim
#         for i in hidden_dims:
#             layers.append(nn.Linear(prev, i))
#             layers.append(nn.ReLU())
#             layers.append(nn.Dropout(0.2))
#             prev = i
#         layers.append(nn.Linear(prev, output_dim))
#         self.net = nn.Sequential(*layers)
#
#     def forward(self, x):
#         return self.net(x)
#
# digits = load_digits()
# X = digits.data
# y = digits.target
#
# scaler = StandardScaler()
# X = scaler.fit_transform(X)
#
# # 将标签转为 tensor
# X_tensor = torch.tensor(X, dtype=torch.float32)
# y_tensor = torch.tensor(y, dtype=torch.long)
#
# dataset = TensorDataset(X_tensor, y_tensor)
# # 划分训练集、测试集
# train_size = int(0.8 * len(dataset))
# test_size = len(dataset) - train_size
# train_set, test_set = random_split(dataset, [train_size, test_size])
#
# train_loader = DataLoader(train_set, batch_size=32, shuffle=True)
# test_loader = DataLoader(test_set, batch_size=32, shuffle=False)
#
# model = MLP(64, [128, 64], 10)
# criterion = nn.CrossEntropyLoss()
# optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-4)
#
# train_loss_list = []
# test_loss_list = []
# train_acc_list = []
# test_acc_list = []
#
# def calculate_loss_acc(loader):
#     model.eval()
#     total_loss = 0.0
#     correct = 0
#     total = 0
#     with torch.no_grad():
#         for bx, by in loader:
#             logits = model(bx)
#             loss = criterion(logits, by)
#             total_loss += loss.item() * bx.shape[0]
#             pred = torch.argmax(logits, dim=1)
#             correct += (pred == by).sum().item()
#             total += bx.shape[0]
#     return total_loss / total, correct / total
#
# epochs = 100
# for epoch in range(epochs):
#     model.train()
#     train_total_loss = 0.0
#     for batch_x, batch_y in train_loader:
#         optimizer.zero_grad()
#         output = model(batch_x)
#         loss = criterion(output, batch_y)
#         loss.backward()
#         optimizer.step()
#         train_total_loss += loss.item() * batch_x.shape[0]
#     train_avg_loss = train_total_loss / len(train_set)
#
#     test_avg_loss, test_acc = calculate_loss_acc(test_loader)
#     _, train_acc = calculate_loss_acc(train_loader)
#
#     train_loss_list.append(train_avg_loss)
#     test_loss_list.append(test_avg_loss)
#     train_acc_list.append(train_acc)
#     test_acc_list.append(test_acc)
#
#     if (epoch + 1) % 10 == 0:
#         print(f"Epoch {epoch+1:3d} | TrainLoss:{train_avg_loss:.4f} | TestLoss:{test_avg_loss:.4f} | TrainAcc:{train_acc:.3f} | TestAcc:{test_acc:.3f}")
#
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
# ax1.plot(train_loss_list, label="训练损失", color="red")
# ax1.plot(test_loss_list, label="测试损失", color="blue")
# ax1.set_xlabel("Epoch")
# ax1.set_ylabel("Loss")
# ax1.set_title("损失曲线")
# ax1.legend()
# ax1.grid(alpha=0.3)
#
# ax2.plot(train_acc_list, label="训练准确率", color="red")
# ax2.plot(test_acc_list, label="测试准确率", color="blue")
# ax2.set_xlabel("Epoch")
# ax2.set_ylabel("Accuracy")
# ax2.set_title("准确率曲线")
# ax2.legend()
# ax2.grid(alpha=0.3)
#
# plt.tight_layout()
# plt.savefig("mlp_loss_acc.png", dpi=200)
# plt.show()
import pickle
import numpy as np
import matplotlib.pyplot as plt

# 你的数据集根目录
root = r"D:\数据集"
batch_path = f"{root}/cifar-10-batches-py/data_batch_1"
meta_path = f"{root}/cifar-10-batches-py/batches.meta"

# 读取类别名字
with open(meta_path, "rb") as f:
    meta = pickle.load(f, encoding="bytes")
label_names = [name.decode("utf-8") for name in meta[b"label_names"]]
print("10个类别：", label_names)

# 读取一个batch
with open(batch_path, "rb") as f:
    batch_data = pickle.load(f, encoding="bytes")

imgs_raw = batch_data[b"data"]       # shape: (10000, 3072)
labels = batch_data[b"labels"]       # 标签列表，0~9

print(f"\n当前batch图片数量：{len(labels)}")
print(f"原始数据形状：{imgs_raw.shape}")

# 把一维像素转为 RGB 图片 (3,32,32)
img_idx = 0  # 随便选第0张
img = imgs_raw[img_idx].reshape(3, 32, 32)
img = np.transpose(img, (1, 2, 0))  # 转为 (32,32,3) 给plt显示

plt.figure()
plt.imshow(img)
plt.title(f"label: {labels[img_idx]} -> {label_names[labels[img_idx]]}")
plt.axis("off")
plt.show()