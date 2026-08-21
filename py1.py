# # student_name = 'du'
# # student_age = '17'
# # print(student_name,student_age)
#
# # 三目表达式
# #结果1 if 条件判断 else 结果2
#
# # 给定一个整数 `x`，用三目表达式判断：如果`x`大于等于0，返回字符串"非负数"，否则返回"负数"
# # x = 1
# # print("非负数") if x>=0 else print("负数")
# # 给定两个数值 `a` 和 `b`，用三目表达式直接返回两者中较大的那个数。
# # a = float(input("请输入a的值："))
# # b = float(input("请输入b的值："))
# # max_num = a if a>b else b
# # print("最大的值为:%f" %max_num)
# # 给定一个字符串 `s`，用三目表达式判断：如果字符串长度大于 5，返回"长字符串"，否则返回"短字符串"
# # s = input("请输入一个字符串：")
# # print("长字符串") if len(s) > 5 else print("短字符串")
# # 给定一个年份 `year`，用三目表达式判断是否为闰年，返回 `"闰年"` 或 `"平年"`。
# # 闰年规则：能被 4 整除但不能被 100 整除，或者能被 400 整除。
# # year = int(input("请输入一个年份："))
# # print("闰年") if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0) else print("平年")
# # 给定一个整数 `num`，用三目表达式判断：如果是偶数返回布尔值 `True`，奇数返回 `False`。
# # num = int(input("请输入一个整数："))
# # print("True") if num % 2 == 0 else print("False")
# # 给定学生分数 `score`（0~100 区间），用**嵌套三目表达式**划分等级： 90 分及以上为 `"优秀"`，60~89 分为 `"及格"`，60 分以下为 `"不及格"`。
# # score = int(input("请输入学生分数："))
# # if (score > 100 or score < 0) :
# #     print("分数有问题")
# # elif score >= 90 :
# #     print("优秀")
# # elif score >= 60 :
# #     print("及格")
# # else:
# #     print("不及格")
# # 1. 给定三个数 `x, y, z`，只用三目表达式返回三个数中的最大值。
# # a = float(input("请输入a的值："))
# # b = float(input("请输入b的值："))
# # c = float(input("请输入c的值："))
# # max = a if a > b and a > c else b if b > c else c
# # print("最大的值为：",max)
# # 2. 结合列表推导式：给定列表 `nums = [3, 7, 12, 5, 18, 20]`，用三目表达式配合列表推导，将列表中大于 10 的数字替换为 `"大"`，小于等于 10 的替换为 `"小"`。
# # s = 0
# # for i in range(1,101):
# #     s += i
# # print(s)
# # sum = 0
# # i = 1
# # while i<=100:
# #     sum += i
# #     i += 1
# # print(sum)
#
# # i = 0
# # while i < 10:
# #     print(i)
# #     if i == 3:
# #         i += 1
# #         continue
# #     i += 1
#
# # for i in range(10):
# #     if i== 3:
# #         continue
# #     print(i)
#
# # name = "jiangwangwen"
# # print("ag" in name)
# #
# # a = "jiang"
# # b = "jiang"
# # print(id(a))
# # print(id(b))
# # print(a is b)
#
# # s = {1,2,3,5}
# # # s.discard(2)
# # s.pop()
# # print(s)
#
# # list = [1,2,"a"]
# # list.append(1)
# # print(list)
# # list.pop()
# # print(list)
# # list.pop(1)
# # print(list)
#
# import ortools
# # print("可用")
#
# import requests
# import time
# from bs4 import BeautifulSoup
# import pandas as pd
#
# # print("爬虫环境就绪")
#
# url = "https://books.toscrape.com/"
# response = requests.get(url)
# # print("状态码：",response.status_code)
# # print(response.text[:500])
# html = response.text
# soup = BeautifulSoup(html, "html.parser")
# books = soup.find_all("article",class_="product_pod")
#
# data_list = []
# for book in books:
#     book_name = book.find("h3").find("a")["title"]
#     book_price = book.find("p",class_="price_color").text
#     data_list.append({
#         "书名":book_name,
#         "价格":book_price
#     })
# df = pd.DataFrame(data_list)
# df.to_csv("图书数据.csv",index=False,encoding="utf-8-sig")
# print("保存完成！共爬取",len(data_list),"本书")
# time.sleep(10)
import pandas as pd
print(pd.__version__)