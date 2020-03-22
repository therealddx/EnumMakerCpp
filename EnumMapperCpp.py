# import.
from EnumEntryCpp import *
from EnumCpp import *
from EnumCppFactory import *
from SwitchCaseCpp import *

# 
# purpose:
#   generate mapping functions between flattened and coordinate enums.
# 
class EnumMapperCpp:
  
  # 
  # ctor. assigns members.
  #   arg_flattenedEnum   : flattened Enum object, representing composite of constituent values.
  #   arg_coordinateEnums : list of coordinate Enum's that only represent one constituent value.
  # 
  def __init__(self, arg_flattenedEnum):

    # make factory.
    enumCppFactory = EnumCppFactory()

    # assign.
    flattenedEnum = arg_flattenedEnum

    # produce coordinate enums.
    self.MakeCoordinateEnums()

  def Map_Flattened_To_Coordinate():
    pass

  def Map_Coordinate_To_Flattened():
    pass 

  def MakeCoordinateEnums():
   
    # vars.
    debug = True
    
    # grab prototype EnumEntryCpp.
    prototypeEntry = flattenedEnum.Get_enumEntries()[0]
    if debug:
      print("EnumMapperCpp.MakeCoordinateEnums: prototypeEntry.ToString():")
      print(prototypeEntry.ToString())

    # for each coordinate in the prototype entry:
    for eachKey in prototypeEntry.Get_privateData().keys():

      # 
      # 1) get the range of possible values for that coordinate.
      # 
      # for each EnumEntryCpp in this flattenedEnum.
      keyRange = []
      for eachEntry in self.flattenedEnum:

        # get the value of that entry, for the target key ('eachKey').
        valueAtKey = keyRange.count(eachEntry.Get_privateData()[eachKey])

        # if that value has not-yet been logged as part of that coordinate's range:
        if keyRange.count(valueAtKey) == 0:
	  # then log it.
          keyRange.append(valueAtKey)

      if debug:
        print("EnumMapperCpp.MakeCoordinateEnums: keyRange:")
        print(str(keyRange))

      # 2) make up a long namespace.
      longNs = "EnumCoordinate_" + str(eachKey)

      # 3) make up a short namespace.
      shortNs = "EC" + eachKey[0]

      # can now make the new enum.
      newEnumCpp = self.enumCppFactory.CreateEnumCpp \
        ( shortNs     # short name for namespace.
	, longNs      # full name.
	, [ eachKey ] # intentionally a single-coordinate enum.
	, keyRange    # empirically-determined range-of-values for this coordinate.
	)

      # ret.
      if debug:
        print("EnumMapperCpp.MakeCoordinateEnums: newEnumCpp:")
        print(newEnumCpp.ToString())

      return newEnumCpp

  # 
  # members: data.
  # 
  flattenedEnum = None # of type EnumCpp.
  coordinateEnums = [] # list of type EnumCpp.
  enumCppFactory = None # Factory for objects of type: EnumCpp, EnumEntryCpp.

