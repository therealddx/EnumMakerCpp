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

  # 
  # CreateEnumCpp.
  # 
  def CreateEnumCpp(self, arg_shortNs, arg_longNs, arg_names, arg_lists):
    
    # vars.
    createEnum = None # EnumCpp instance.
    listEnumEntrys = [] # all enum entries from CreateEnumEntryCpps.
    debug = False

    # generate EnumEntryCpp's.
    listEnumEntrys = self.CreateEnumEntryCpps(
      arg_shortNs, arg_longNs,
      arg_names, arg_lists)

    # generate the EnumCpp.
    createEnum = EnumCpp(arg_longNs, arg_shortNs, listEnumEntrys)

    # ret.
    return createEnum

  # 
  # CreateEnumEntryCpps.
  # 
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
      print("EnumCppFactory.CreateEnumEntryCpps: listEnumEntrys:")
      for eachEntry in listEnumEntrys:
        print(eachEntry.ToString())
      print("")

    return listEnumEntrys 

  # 
  # CreateDicts.
  #   Collates named lists into a collection of enum entries.
  #   arg_names : list of names that will define coordinate keys.
  #   arg_lists : list of lists, defining possible values for each coordinate keys.
  # 
  def CreateDicts(self, arg_names, arg_lists):
    
    # vars.
    debug = False

    # totalLengthProduct:
    #   product of length for all lists.
    totalLengthProduct = 1
    for eachList in arg_lists:
      totalLengthProduct *= len(eachList)

    # allEntries:
    #   list of coordinate Dictionarys that define every possible EnumEntryCpp.
    allEntries = [{} for eachInteger in range(totalLengthProduct)]

    # nModulo:
    #   maps each name to its nModulo.
    #   the nModulo for a name is defined as the amount of entries
    #   that are to be filled out before incrementing to use the 
    #   next list value.
    #   the nModulo value is used to hierarchically collate
    #   values that exist in the domain for each name.
    nModulo = {}

    # for each name.
    for n_argIndex in range(len(arg_names)): # 0, 1, 2...

      # assign references.
      ref_name = arg_names[n_argIndex]

      # find length product of all lists -after- this name. 
      lengthProduct = 1
      for eachList in arg_lists[(n_argIndex + 1):]: # 1, 2, 3...
        lengthProduct *= len(eachList)

      # assign nModulo value for that name.
      nModulo[ref_name] = lengthProduct

    # run.

    # for each name.
    for n_argIndex in range(len(arg_names)):
      
      # assign references.
      ref_name = arg_names[n_argIndex]
      ref_list = arg_lists[n_argIndex]
      ref_listLength = len(ref_list)

      # iterator index below.
      ref_listIncrementor = 0

      # fill out every enum entry for this name.
      for n_entryIndex in range(len(allEntries)):

        # assign references.
        ref_entry = allEntries[n_entryIndex]

        # only increment if n_entryIndex has reached an nModulo.
        if (n_entryIndex % nModulo[ref_name] == 0 and n_entryIndex != 0):
          ref_listIncrementor += 1 

        # assign reference index into space of referenced list.
        ref_listIndex = ref_listIncrementor % ref_listLength

        # assign desired value from reference list to entry at name.
        ref_entry[ref_name] = ref_list[ref_listIndex]

    # ret.
    if debug:
      print(str(allEntries))

    return allEntries


