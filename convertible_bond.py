

import datetime
import time
#当前年月日
current_date = datetime.datetime.today()
#个人所得税
tax_rate = 0.2

string_input_type=['']
#输入类型
string_input_type.extend(['1:已知可转债价格，求到期收益率（YTM）'])
string_input_type.extend(['2:已知可转债价格，求回购收益率'])
string_input_type.extend(['3:已知可转债价格，求到期收益率和回购收益率'])
string_input_type.extend(['4:已知期望到期收益率，求相应可转债价格'])
string_input_type.extend(['5:已知期望回购收益率，求相应可转债价格'])
#输入类型总数
string_input_type_total = 5

#输入操作类型
#1：输入现在价格
#2：输入到期信息
#3：输入回购信息
#4：输入直到到期利率
#5：输入直到回购利率
#6：输入期望到期收益率
#7：输入期望回购收益率
#输入类型--操作类型矩阵

operation_input = [[],[1,2,4],[1,3,5],[1,2,3,4],[2,4,6],[3,5,7]]


class convertible_bond(object):
  """ """
  #初始化和其他函数-----------------------------------------------------

  def __init__(self):
    self.current_price = 0
    self.maturity_price = 0
    self.maturity_date = datetime.date(2000, 1, 1)
    self.maturity_annul = 0
    self.buyback_price = 0
    self.buyback_date = datetime.date(2000, 1, 1)
    self.buyback_annul = 0
    self.rates=[0]*3000

  def transfer_date(year, month, day):
    '''将数字转换为合规日期'''
    if (year < 2000) or (month not in range(1,13)) or (day not in range (1,32)):
      print("年份必须2000年以后，月份为1至12，日为1-31")
      time.sleep(100)
    return datetime.date(year, month, day)

  #-------------------------------------------------------------
  #输入部分-----------------------------------------------------
  #-------------------------------------------------------------
  #input_current_price 输入现在价格
  #input_maturity 输入到期信息
  #input_buyback 输入回购信息
  #input_current_date（可以实现改变初始日期）
  #input_rate 输入利率（可能是直到到期或回购）

  def input_current_price(self):
    self.current_price=float(input('输入当前票面价格：'))

  def input_maturity(self):
    year, month, day = map(int, input("输入债券到期年月日，用空格分开：").split())
    self.maturity_date = convertible_bond.transfer_date(year, month, day)
    self.maturity_price = float(input("输入债券到期价格"))

  def input_buyback(self):
    year, month, day = map(int, input("输入债券回购年月日，用空格分开：").split())
    self.buyback_date = convertible_bond.transfer_date(year, month, day)
    self.buyback_price = float(input("输入债券回购价格"))

  def input_current_date(self):
    pass

  def input_rate(self,year_begin,year_end):
    """ 要求输入每年利率，参数为起始年份 year_begin and year_end  """
    for year in range(year_begin,year_end+1):
        self.rates[year]=float(input(f'输入{year}年的利率：'))

  #-------------------------------------------------------------
  #转换部分-----------------------------------------------------
  #-------------------------------------------------------------

  def calculate_annual_to_current_profit(self,annul,date_end,price_end):
    """计算利息和结束日收入，在给定年化收益率下，计算折现后现在收入。输入：年化收益率，结束日期，结束价格"""
    profit=float(0)
    #中间相隔天数
    delta_days=date_end-current_date

  def convert_current_to_maturity(self):
    """从现价求到期收益率"""
    pass

  def convert_current_to_buyback(self):
    pass

  #-------------------------------------------------------------
  #输出部分-----------------------------------------------------
  #-------------------------------------------------------------

  def print_price(self):
    print('票面价格为%.3f' % (self.current_price))



def input_type():
  for i in range(1,string_input_type_total+1):
    print(string_input_type[i])
  print('输入要计算的类型（数字1至%d）：'% (string_input_type_total))
  type = int(input())
  if type not in range(1,string_input_type_total+1):
    print("输入超出范围")
  return type

def input_data(type):

  if 1 in operation_input[type]: #1：输入现在价格
    bond.input_current_price()

  if 2 in operation_input[type]: #2：输入到期信息
    bond.input_maturity()

  if 3 in operation_input[type]: #3：输入回购信息
    bond.input_buyback()

  if 4 in operation_input[type]: #4：输入直到到期利率
    print(bond.maturity_date.year,current_date.year)
    bond.input_rate(current_date.year,bond.maturity_date.year)

  if 5 in operation_input[type]: #5：输入直到回购利率
    pass

  if 6 in operation_input[type]: #6：输入期望到期收益率
    pass

  if 7 in operation_input[type]: #7：输入期望回购收益率
    pass

bond = convertible_bond()
type = 1
#type = input_type()
input_data(type)
