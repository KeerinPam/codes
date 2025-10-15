'''工资结算系统'''
'''部门经理的月薪是固定 15000 元；
程序员按工作时间（以小时为单位）支付月薪，每小时 200 元；
销售员的月薪由 1800 元底薪加上销售额 5% 的提成两部分构成。
'''

from abc import ABCMeta, abstractmethod
import random

class Employee:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass #占位符语句 保持程序结构的完整性，避免语法错误

class Manager(Employee):
    def get_salary(self):
        self.salary = 15000
        print(f'{self.name}的工资为{self.salary}')
    
class Coder(Employee):
    def __init__(self, name, work_duration = 0):
        super().__init__(name)
        self.work_duration = work_duration

    def get_work_duration(self):
        print(f'{self.name}的工作时长为{self.work_duration}')
     
    def get_salary(self):
        self.salary = self.work_duration * 200
        print(f'{self.name}的工资为{self.salary}')

class Salesman(Employee):
    def __init__(self, name, sales = 0):
        super().__init__(name)
        self.sales = sales

    def get_sales(self):
        print(f'{self.name}的销售额为{self.sales}')
    
    def get_salary(self):
        self.salary = int(self.sales * 0.05) + 1800
        print(f'{self.name}的工资为{self.salary}')

manager = Manager('张三')
coder = Coder('李四', 240)
salesman = Salesman('王五', 10000)

manager.get_salary()
coder.get_salary()
salesman.get_salary()