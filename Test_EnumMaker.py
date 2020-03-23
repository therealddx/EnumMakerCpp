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
#  enumCppFactory = EnumCppFactory()
#
#  newEnumCpp = enumCppFactory.CreateEnumCpp("S", "EnumSetting",
#    [ "SETTING" ], [ [ "1", "2", "3", "4", "5", "6", "7", "8" ] ] )
#
#  print(newEnumCpp.ToString())

  # 
  # make Factory.
  # 
  ecf = EnumCppFactory()

  # 
  # make EnumCpp.
  # 
  settingList = ["1", "2", "3", "4", "5"]
  optionList = ["1", "2"]
  myFlattenedEnum = ecf.CreateEnumCpp \
    ( "SO"
    , "SettingOption"
    , [ "SETTING", "OPTION" ]
    , [ settingList, optionList ]
    )

  print("Test_EnumMaker: myFlattenedEnum:")
  print(myFlattenedEnum.ToString())
  print("")

  # 
  # make Mapper.
  # 
  emc = EnumMapperCpp(myFlattenedEnum, ecf)

# 
# 
# 
# 
# 

def Test_SwitchCaseCpp():
  scc = SwitchCaseCpp("myVar", \
  { "31" : "function1();"
  , "22" : "function2();"
  , "13" : "function3();"
  },
  "return \"WrongErrorError\";"
  )
  
  print("Switch Case Looks like:")
  print(scc.ToString())


