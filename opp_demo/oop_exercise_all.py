#object oriented programming 面向对象编程
#类、构造函数、封装、继承、多态

# # 第一部分：封装（侧重私有属性、访问控制，带易错坑）
# ## 题1
# 创建 `GameAccount` 游戏账号类
# 1. 属性：账号名，`__hp`（血量，私有）
# 2. 构造方法初始化账号名、初始血量（初始血量范围 0~100）
# 3. 提供方法 `set_hp(num)` 修改血量：
#    - 血量不能小于0，不能大于100；非法数值提示，不修改
# 4. `get_hp()` 获取当前血量
# 5. 思考：能不能在类外面直接写 `对象.__hp = 99` 修改血量？为什么？
class GameAccount:

    def __init__(self,account,hp):
        self.account = account
        if 0 <= hp <=100:
            self.__hp = hp
        else:
            print("血量非法，自动设置为0")
            self.__hp = 0
    def set_hp(self,num):
        if 0 <= num <= 100:
            self.__hp = num
            print(f"当前血量：{self.__hp}")
        else:
            print("血量不合法！血量范围为0~100")
    def get_hp(self):
        return self.__hp
    def show_info(self):
        print(f"账号：{self.account},当前血量：{self.__hp}")
player1 = GameAccount("小蒋",110)
player1.show_info()
#不能在类的外面直接写“对象.__hp = 99”去修改血量，因为双下划线是私有属性，在类外部不能去访问


# ## 题2（进阶封装，属性拦截）
# 商品类 `Goods`
# 1. 属性：名称，`__cost`（成本私有），售价
# 2. 规则：售价**不能低于成本价**
# 3. 写 `set_sell_price()` 设置售价，自动校验价格规则；
# 4. 外部禁止直接访问成本，只能通过方法查看成本。
class Goods:
    def __init__(self,name,cost,sell_price):
        self.name = name
        self.__cost = cost
        if sell_price >= self.__cost:
            self.sell_price = sell_price
        else:
            print(f"商品{self.name}的售价不能低于成本价，自动将售价定为成本价{self.__cost}元")
            self.sell_price = self.__cost
    def set_sell_price(self,new_price):
        if new_price >= self.__cost:
            self.sell_price = new_price
        else:
            print("设置失败（注意：售价不能低于成本价）")
    def get_cost(self):
        return self.__cost
    def get_sell_price(self):
        return self.sell_price
    def show_info(self):
        print(f"商品名称：{self.name}")
        print(f"成本价：{self.__cost}元")
        print(f"当前售价：{self.sell_price}")
book = Goods("西游记",1000,100)
book.get_sell_price()
book.show_info()

# # 第二部分：继承（重点考察 super()、构造函数传参、重写）
# ## 题3（基础单继承）
# 父类 `Vehicle`（交通工具）
# 属性：品牌
# 方法：`run()` 输出：交通工具在路上行驶
# 子类 `Motorcycle(Vehicle)`（摩托车）
# 重写 `run()`：输出：摩托车轰隆隆向前骑行
# 创建对象调用测试。
class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    def run(self):
        print("交通工具在路上行驶")
class Motorcycle(Vehicle):
    def run(self):
        print(f"{self.brand}摩托车轰隆隆向前骑行")
v1 = Vehicle("宝马")
v1.run()
v2 = Motorcycle("保时捷")
v2.run()

# ## 题4【高频难点：super()传参，必考】
# 父类 `User`
# ```python
# def __init__(self,name,age):
#     self.name = name
#     self.age = age
# ```
# 子类 `VipUser(User)`
# 扩展属性：积分 point
# 要求：
# 使用 `super()` 调用父类构造初始化 name、age；子类额外初始化积分。
# 编写 `show_info()` 打印姓名、年龄、积分。
# > 坑点：很多初学者super忘记传参，直接报错。
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class VipUser(User):
    def __init__(self,name,age,point):
        super().__init__(name,age)
        self.point = point
    def show_info(self):
        print(f"姓名：{self.name},年龄：{self.age},积分：{self.point}")
vipuser = VipUser("小蒋",18,1000000)
vipuser.show_info()

# ## 题5 多层继承
# 爷爷类 `Device` → 父类 `Electronic(Device)` → 子类 `Phone(Electronic)`
# 父类拥有 `power_on()` 方法，子类可以选择重写开机方法，观察继承传递特性。
class Device:
    def power_on(self):
        print("设备开机")
class Electronic(Device):
    pass
class Phone(Electronic):
    def power_on(self):
        print("设备断电，重启")

# # 第三部分：多态（区分：单纯重写 ≠ 多态！重点考察统一函数接收不同对象）
# ## 题6（经典多态，和之前动物题场景不同）
# 父类 `Payment`（支付方式）
# 方法：`pay(money)`，预留空方法
# 子类 `WeChatPay(Payment)`：实现pay，输出“微信支付xx元”
# 子类 `AliPay(Payment)`：实现pay，输出“支付宝支付xx元”
# 定义通用函数：
# ```python
# def checkout(pay_obj,money):
#     pay_obj.pay(money)
# ```
# 分别传入微信、支付宝对象完成支付，体现多态。
# class Payment:
#     def pay(self,money):
#         pass
# class WeChatPay(Payment):
#     def pay(self,money):
#         print(f"微信支付{money}元")
# class AliPay(Payment):
    # def pay(self,money):
        # print(f"支付宝支付{money}元")
# def checkout(pay_obj,money):
    # pay_obj.pay(money)
# wechatpay = WeChatPay()
# alipay = AliPay()
# checkout(wechatpay,10)
# checkout(alipay,100)

class Payment:
    def pay(self,money):
        self.money = money
class WeChatPay(Payment):
    def pay(self,money):
        super().pay(money)
        print(f"微信支付{self.money}元")
class AliPay(Payment):
    def pay(self,money):
        super().pay(money)
        print(f"支付宝支付{self.money}元")
def checkout(pay_obj,money):
    pay_obj.pay(money)
wechatpay = WeChatPay()
alipay = AliPay()
checkout(wechatpay,100)




# ## 题7
# 图形父类 `Graphic`，方法 `calculate()`
# 子类 `Triangle`（底、高）、子类 `Square`（边长）
# 各自重写 calculate 计算面积；
# 写统一函数打印任意图形面积。
class Graphic:
    def calculate(self):
        pass
class Triangle(Graphic):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def calculate(self):
        area = self.base * self.height / 2
        print(f"三角形面积为{area}")
class Square(Graphic):
    def __init__(self,side):
        self.side = side
    def calculate(self):
        area = self.side * self.side
        print(f"正方形面积为{area}")
def checkout(graphic_obj):
    graphic_obj.calculate()
triangle = Triangle(10,5)
square = Square(10)
checkout(triangle)
checkout(square)

# # 第四部分：综合大题【封装+继承+多态三合一，期末大题难度】
# ## 题8
# 父类：`Staff`
# 1. 属性：姓名，`__base` 基础工资（私有化封装）
# 2. 方法 `get_income()`：返回基础工资
# 子类1：`SalesStaff(Staff)`
# 扩展属性：销售额、提成比例
# 重写 `get_income()`：总收入 = 基本工资 + 销售额×提成
# 子类2：`TechStaff(Staff)`
# 扩展属性：项目奖金
# 重写 `get_income()`：总收入 = 基本工资 + 项目奖金
# 1. 外部不能直接修改基础工资；
# 2. 编写统一函数 `print_salary(staff)`，打印员工收入；
# 3. 创建两种员工对象传入函数，实现多态。
class Staff:
    def __init__(self,name,base_salary):
        self.name = name
        self.__base_salary = base_salary
    def get_base(self):
        return self.__base_salary
    def get_income(self):
        return self.__base_salary
class SalesStaff(Staff):
    def __init__(self,name,base_salary,sales_amount,commission_rate):
        super().__init__(name,base_salary)
        self.sales_amount = sales_amount
        self.commission_rate = commission_rate
    def get_income(self):
        total_income = self.get_base() + self.sales_amount * self.commission_rate
        return total_income
class TechStaff(Staff):
    def __init__(self,name,base_salary,project_bonus):
        super().__init__(name,base_salary)
        self.project_bonus = project_bonus
    def get_income(self):
        total_income = self.get_base() + self.project_bonus
        return total_income
def print_salary(staff_obj):
    income = staff_obj.get_income()
    print(f"员工{staff_obj.name},本月收入为{income}元")
staff1 = SalesStaff("小蒋",1000000,10000000,0.2)
staff2 = TechStaff("小华",10000,2000000)
print_salary(staff1)
print_salary(staff2)