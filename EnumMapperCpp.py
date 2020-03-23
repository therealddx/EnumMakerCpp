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
  #   arg_flattenedEnum   : flattened Enum object, representing composite of coordinate values.
  #   arg_coordinateEnums : list of coordinate Enum's that only represent one coordinate value.
  # 
  def __init__(self, arg_flattenedEnum, arg_EnumCppFactory):

    # vars.
    debug = False

    # assign factory handle.
    self.enumCppFactory = arg_EnumCppFactory

    # assign.
    self.flattenedEnum = arg_flattenedEnum

    # produce coordinate enums.
    self.MakeCoordinateEnums()
    
    if debug:
      print("EnumMapperCpp.__init__: self.coordinateEnums:")
      for eachCoordinateEnum in self.coordinateEnums:
        print(eachCoordinateEnum.ToString())

  def Map_Flattened_To_Coordinate():
    pass

  def Map_Coordinate_To_Flattened():
    pass 

  # 
  # MakeCoordinateEnums.
  #   Given flattened EnumCpp, derive coordinate EnumCpp's.
  # 
  def MakeCoordinateEnums(self):
   
    # vars.
    debug = False
    self.coordinateEnums = []
    
    # grab prototype EnumEntryCpp.
    prototypeEntry = self.flattenedEnum.Get_enumEntries()[0]
    if debug:
      print("EnumMapperCpp.MakeCoordinateEnums: prototypeEntry.ToString():")
      print(prototypeEntry.ToString())

    # for each coordinate in the prototype entry:
    for eachKey in prototypeEntry.Get_privateData().keys():

      # 
      # 1) get the range of possible values for that coordinate.
      # 
      # for each EnumEntryCpp in this flattenedEnum.
      # todo:efficiency: we know that a flattened enum repeats for each key.
      #   so - when you find the same key twice, you can break.
      keyRange = []
      for eachEntry in self.flattenedEnum.Get_enumEntries():

        # get the value of that entry, for the target key ('eachKey').
        valueAtKey = eachEntry.Get_privateData()[eachKey]

        if debug:
          print("EnumMapperCpp.MakeCoordinateEnums: Key:")
          print(eachKey)
          print("")
          print("EnumMapperCpp.MakeCoordinateEnums: Value:")
          print(valueAtKey)
          print("")

        # if that value is not-yet-logged in that coordinate's range:
        if keyRange.count(valueAtKey) == 0:
          # then log it.
          keyRange.append(valueAtKey)

      if debug:
        print("EnumMapperCpp.MakeCoordinateEnums: keyRange:")
        print(str(keyRange))
        print("")

      # 2) make up a long namespace.
      longNs = "EnumCoordinate_" + str(eachKey)

      # 3) make up a short namespace.
      shortNs = "EC" + eachKey[0]

      # can now make the new enum.
      newEnumCpp = self.enumCppFactory.CreateEnumCpp(shortNs, longNs, 
        [ eachKey ], [ keyRange ] )

      # ret.
      if debug:
        print("EnumMapperCpp.MakeCoordinateEnums: newEnumCpp:")
        print(newEnumCpp.ToString())
      
      self.coordinateEnums.append(newEnumCpp)

  # 
  # members: data.
  # 
  flattenedEnum = None # of type EnumCpp.
  coordinateEnums = [] # list of type EnumCpp.
  enumCppFactory = None # Factory for objects of type: EnumCpp, EnumEntryCpp.

