# # Python 构造函数练习题（适合新手）
# ### 题目1
# 定义一个学生类 `Student`：
# 1. 包含属性：姓名、年龄、学号
# 2. 使用构造函数 `__init__` 初始化三个属性
# 3. 写一个 `show_info()` 方法，打印学生所有信息
class Student:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
    def show_info(self):
        print(f"姓名:{self.name}")
        print(f"{self.name}的年龄；{self.age}")
        print(f"{self.name}的学号：{self.id}")
student1 = Student("小蒋",18,22)
student1.show_info()

# ### 题目2
# 定义一个电脑类 `Computer`：
# 1. 属性：品牌、价格
# 2. 构造函数默认价格为 `5000`（默认参数）
# 3. 写方法输出电脑信息
class Computer:
    def __init__(self,brand,price=5000):
        self.brand = brand
        self.price = price
    def show_computer(self):
        print(f"电脑的品牌：{self.brand}")
        print(f"{self.brand}的价格：{self.price}")
computer1 = Computer("联想")
computer1.show_computer()

# ## 中级题（考试常考）
# ### 题目3
# 定义一个图书类 `Book`：
# 1. 属性：书名、作者、价格
# 2. 构造函数初始化全部属性
# 3. 写一个方法，可以**打折**（传入折扣，修改价格）
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def discount_price(self,discount):
        self.price = self.price * (discount / 10)
    def show_book(self):
        print(f"书名：{self.title}")
        print(f"{self.title}的作者：{self.author}")
        print(f"{self.title}的价格：{self.price}元")
book1 = Book("老人与海","海明威",150)
book1.discount_price(5)
book1.show_book()

# ### 题目4
# 定义一个 `Dog` 类：
# 1. 属性：名字、品种、年龄
# 2. 禁止年龄负数（构造函数内部判断）
#    - 如果负数，自动改为 0
# 3. 写一个 bark() 方法输出：`xx 在汪汪叫`
class Dog:
    def __init__(self,dog_name,breed,age):
        self.dog_name = dog_name
        self.breed = breed
        if age < 0:
            self.age = 0
        else:
            self.age = age
    def bark(self):
        print(f"{self.dog_name}在汪汪叫")
    def show_dog(self):
        print(f"小狗的名字：{self.dog_name}")
        print(f"{self.dog_name}的品种：{self.breed}")
        print(f"{self.dog_name}的年龄：{self.age}")
dog1 = Dog("大黄","拉布拉多",3)
dog1.show_dog()
dog1.bark()

# ## 进阶题（面向对象核心）
# ### 题目5
# 创建一个 `Rectangle` 矩形类：
# 1. 构造函数初始化 长、宽
# 2. 写方法：求面积、求周长
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def calculate(self):
        self.area = self.length * self.width
        self.perimeter = 2 * (self.length + self.width)
    def show_rectangle(self):
        self.calculate()
        print(f"面积为:{self.area}",f"周长为：{self.perimeter}")
rectangle1 = Rectangle(10,20)
rectangle1.show_rectangle()

# ### 题目6
# 创建一个 `BankAccount` 账户类：
# 1. 属性：账号、余额（默认0）
# 2. 方法：存钱、取钱、查询余额
# 3. 取钱不能超过余额（判断）
class BankAccount:
    def __init__(self,account,balance=0):
        self.account = account
        self.balance = balance
    def save_money(self,money):
        if money > 0:
            self.balance += money
            print(f"成功存入{money}元")
        else:
            print(f"存入失败")
    def take_money(self,money):
        if money <= 0:
            print("取出失败")
        elif money > self.balance:
            print("余额不足")
        else:
            self.balance -= money
            print(f"成功取出{money}元")
    def show_balance(self):
        print(f"账号：{self.account},当前余额：{self.balance}")
bankaccount1 = BankAccount("jiang",10)
bankaccount1.save_money(100)
bankaccount1.show_balance()
bankaccount1.take_money(120)
bankaccount1.show_balance()

# ## 拔高题（期末/面试常考）
# ### 题目7
# 设计一个 `Employee` 员工类：
# 1. 属性：姓名、部门、基本工资、绩效工资
# 2. 构造函数初始化所有数据
# 3. 写方法：计算总工资 = 基本工资 + 绩效工资
class Employee:
    def __init__(self,name,department,base_salary,merit_pay):
        self.name = name
        self.department = department
        self.base_salary = base_salary
        self.merit_pay = merit_pay
    def show_employee(self):
        self.total_salary = self.base_salary + self.merit_pay
        print(f"{self.department}部门的{self.name}总工资：{self.total_salary}")
employee1 = Employee("小蒋","研发",1000000,400000)
employee1.show_employee()

# ### 题目8
# 设计一个 `Car` 类：
# 1. 属性：车名、颜色、速度（初始0）
# 2. 方法：加速（速度+10）、减速（速度-10，最低0）
# 3. 输出当前速度
class Car:
    def __init__(self,car_name,color,speed=0):
        self.car_name = car_name
        self.color = color
        self.speed = speed
    def speed_up(self,acceleration=10):
        if acceleration > 0:
            self.speed += acceleration
        else:
            print("不是加速")
    def speed_reduction(self,deceleration=10):
        if  deceleration >= 0:
            self.speed -= deceleration
            if self.speed < 0:
                self.speed = 0
        else:
            print("不是减速")
    def show_car(self):
        print(f"当前速度：{self.speed}")
car1 = Car("奔驰","黑色")
car1.speed_up()
car1.show_car()
car1.speed_reduction()
car1.speed_reduction()
car1.show_car()