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
  # ctor.
  #   Construct instance. (flattened EnumCpp) => (coordinate EnumCpp's).
  #   arg_flattenedEnum  : EnumCpp. flattened Enum as exploded coordinates.
  #   arg_enumCppFactory : reference to instantiated EnumCppFactory.
  # 
  def __init__(self, arg_flattenedEnum, arg_enumCppFactory):

    # vars.
    debug = True

    # assign factory handle.
    self.enumCppFactory = arg_enumCppFactory

    # assign flattened enum.
    self.flattenedEnum = arg_flattenedEnum

    # produce coordinate enums.
    self.MakeCoordinateEnums()
    
    if debug:
      print("EnumMapperCpp.__init__: self.coordinateEnums:")
      for eachCoordinateEnum in self.coordinateEnums:
        print(eachCoordinateEnum.ToString())
  
  # 
  # MakeCoordinateEnums.
  #   Given flattened EnumCpp, derive coordinate EnumCpp's.
  # 
  def MakeCoordinateEnums(self):
   
    # vars.
    debug = True
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
      # 
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
  # MakeCoordinateMapping.
  #   Make SwitchCaseCpp instances such that:
  #   Elements of flattenedEnums map to elements of coordinateEnums.
  # 
  def MakeCoordinateMapping(self):

    # 
    # one mapping function for each coordinate enum.
    # 

    # 
    # difference b/w writing a function, vs. a switch/case structure.
    # 

    # for each EnumCpp in your available coordinate keys.
    #   get the prototype key (EnumEntryCpp, w/e its key is).
    #   write the function prototype.
    #   make a switch/case.
    #     key: the input flattened value, function argument
    #     one case for each flattened value.
    #     for the case consequence:
    #       get the flattened argument's value for the prototype key.
    # 
    # yawn... boring.
    # 

    pass

  # 
  # MakeFlattenedMapping.
  #   Make SwitchCaseCpp structure such that:
  #   Elements of coordinateEnums map to the correct flattenedEnum element.
  # 
  def MakeFlattenedMapping(self):
    # 
    # nesting of switch / case structures.
    # 
    pass

  # 
  # members: data.
  # 
  flattenedEnum = None # of type EnumCpp.
  coordinateEnums = [] # list of type EnumCpp.
  enumCppFactory = None # Factory for objects of type: EnumCpp, EnumEntryCpp.

#  def Map_Coordinate_To_Flattened():
#    pass 
#
#  def MakeFlattenedEnum(self):
#    pass
# 
