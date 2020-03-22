# 
# EnumEntryCpp: one enum entry.
#   represents one enum entry as a flattened composite of all coordinates
#   in its Dict.
# 
class EnumEntryCpp:
  
  # 
  # ctor.
  #   self               : 'this' pointer.
  #   arg_longNamespace  : long string to describe namespace
  #   arg_shortNamespace : abbreviated string to describe namespace.
  #   arg_fromDict       : coordinate values that comprise this entry.
  # 
  def __init__(self, arg_longNamespace, arg_shortNamespace, arg_fromDict):
    self.longNs      = arg_longNamespace
    self.shortNs     = arg_shortNamespace
    self.privateData = arg_fromDict.copy()

  # 
  # ToString. Serializes this.
  # 
  def ToString(self):

    # 
    # vars.
    # 
    toReturn = self.shortNs + "_"

    # 
    # for each key:
    #   print it next to its value.
    #   delimit with '_'.
    # 
    for eachKey in self.privateData.keys():
      toReturn += str(eachKey) + str(self.privateData[eachKey]) + "_"

    # cut off last '_'.
    return toReturn[:-1]

  def Get_privateData():
    return self.privateData.copy()

  # 
  # private data.
  # 
  longNs = ""
  shortNs = ""
  privateData = {} # dictionary mapping constituent options.


