# import.
from EnumEntryCpp import *
from EnumCpp import *

# 
# EnumCppFactory:
#   Factory class for making instances of EnumEntryCpp and EnumCpp.
# 
class EnumCppFactory:

  # 
  # ctor.
  # 
  def __init__(self):
    pass

  def CreateEnumCpp(self, arg_shortNs, arg_longNs, arg_names, arg_lists):
    
    # vars.
    createEnum = None # EnumCpp instance.
    listEnumEntrys = [] # all enum entries from CreateEnumEntryCpps.

    # generate EnumEntryCpp's.
    listEnumEntrys = self.CreateEnumEntryCpps(arg_shortNs, arg_longNs, arg_names, arg_lists)

    # generate the EnumCpp.
    createEnum = EnumCpp(arg_longNs, arg_shortNs, listEnumEntrys)

    # ret.
    return createEnum

  def CreateEnumEntryCpps(self, arg_shortNs, arg_longNs, arg_names, arg_lists):

    # vars.
    listEnumEntrys = [] # type: EnumEntryCpp
    debug = False

    # create the constituent dicts.
    enumEntryDicts = self.CreateDicts(arg_names, arg_lists)

    # create the resultant EnumEntrys.
    for eachDict in enumEntryDicts:
      listEnumEntrys.append(EnumEntryCpp(arg_longNs, arg_shortNs, eachDict))

    # ret.
    if debug:
      for eachEntry in listEnumEntrys:
        print(eachEntry.ToString())

    return listEnumEntrys 


