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

  # 
  # make Factory.
  # 
  ecf = EnumCppFactory()

  # 
  # make EnumCpp.
  # 
  bigList = ["1", "2" ]
  littleList = ["L1", "L2", "L3" ]
  minorList = ["M1", "M2", "M3", "M4" ]
  tweakList = ["T1", "T2", "T3", "T4" ]
  myFlattenedEnum = ecf.CreateEnumCpp \
    ( "BLMT"
    , "BigLittleMinorTweak"
    , [ "BIG", "LITTLE", "MINOR", "TWEAK" ]
    , [ bigList, littleList, minorList, tweakList ]
    )

  # 
  # make Mapper.
  # 
  emc = EnumMapperCpp(myFlattenedEnum, ecf)

  # 
  # remind us what the original flattened was.
  # 
  print(myFlattenedEnum.ToString())

