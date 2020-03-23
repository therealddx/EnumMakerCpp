# imports.
from EnumEntryCpp import *

# 
# EnumCpp: One entire valid Cpp enumeration.
# 
class EnumCpp:

  # 
  # ctor.
  #   self                : 'this' pointer.
  #   arg_longNamespace   : long string to describe namespace
  #   arg_shortNamespace  : abbreviated string to describe namespace.
  #   arg_allEnumEntryCpp : list [] of enum entries.
  # 
  def __init__( self
    , arg_longNamespace
    , arg_shortNamespace
    , arg_allEnumEntryCpp
    ):

    # 
    # assign characteristic vars.
    # 
    self.longNs = arg_longNamespace
    self.shortNs = arg_shortNamespace

    # 
    # only admit enum entries that are in this Enum's ns.
    # 
    self.enumEntries = []
    for eachEntry in arg_allEnumEntryCpp:
      if (self.longNs == eachEntry.longNs):
        self.enumEntries.append(eachEntry)
    # 
    # the ns of an EnumEntryCpp implicitly defines its...
    #   ...Dictionary structure.
    # 

  # 
  # displays a full enumeration.
  # 
  def ToString(self, arg_baseIndent = ""):
    
    # vars.
    toReturn = ""
  
    # write enum header line.
    toReturn += arg_baseIndent + "enum" + " " + self.longNs + "\n"
  
    # write enum opening brace.
    toReturn += arg_baseIndent + "{" + "\n"
  
    # print all enum entries.
    for eachEnum in self.enumEntries:
      toReturn += ( arg_baseIndent + "  " + 
      eachEnum.ToString() + "," + "\n" )

    # write enum closing brace.
    toReturn += arg_baseIndent + "}" + ";" + "\n"

    # return.
    return toReturn

  #  
  # accessor: get member enumEntries.
  # 
  def Get_enumEntries(self):
    return self.enumEntries.copy()

  # vars.
  longNs = ""
  shortNs = ""
  enumEntries = [] # list of type EnumEntryCpp.


