# import.
from EnumEntryCpp import *
from EnumCpp import *
from EnumCppFactory import *
from SwitchCaseCpp import *
from EnumMapperCpp import *

# 
# Test application.
# 
def Test_EnumMaker():
  # scc = SwitchCaseCpp("myVar", \
  # { "31" : "function1();"
  # , "22" : "function2();"
  # , "13" : "function3();"
  # },
  # "return \"WrongErrorError\";"
  # )

  # print("Switch Case Looks like:")
  # print(scc.ToString())

  ecf = EnumCppFactory()
  settingList = ["1", "2", "3", "4", "5"]
  optionList = ["6", "7"]
  myFlattenedEnum = ecf.CreateEnumCpp("SO", "SettingOption", [ "SETTING", "OPTION" ], [ settingList, optionList ])

  emc = EnumMapperCpp(myFlattenedEnum)

