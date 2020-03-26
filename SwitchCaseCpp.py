# 
# holds the contents of a switch / case structure in deserialized format.
# 
class SwitchCaseCpp:

  # 
  # ctor.
  #   arg_switchKey          : string representing variable of switch/case.
  #   arg_caseConsequence    : Maps cases to resultant C++ statements.
  #   arg_defaultConsequence : C++ statement for default-case.
  # 
  def __init__(self, arg_switchKey, arg_caseConsequence, arg_defaultConsequence):
    
    # member assignment.
    self.switchKey = arg_switchKey
    self.caseConsequence = arg_caseConsequence
    self.defaultConsequence = arg_defaultConsequence

  # 
  # ToString.
  #   Returns string representation of this switch-case structure.
  #   arg_caseBracing: integer denoting bracing style. Default:  maximal flatness.
  #   arg_baseIndent: base number of spaces in front of each line.
  # 
  def ToString(self, arg_caseBracing = 0, arg_baseIndent = ""):
    
    # vars.
    toReturn = ""

    # run.

    # write header line + brace.
    toReturn += arg_baseIndent + "switch " + "(" + self.switchKey + ")" + "\n"
    toReturn += arg_baseIndent + "{" + "\n"

    # write case body.
    for eachCaseKey in self.caseConsequence.keys():
      toReturn += arg_baseIndent + "  " + "case " + eachCaseKey + ": "
      toReturn += "{" + " " + self.caseConsequence[eachCaseKey] + " " + "}" + "\n"

    # write default.
    toReturn += arg_baseIndent + "  " + "default: " + "{" + " " + self.defaultConsequence + " " + "}" + "\n"

    # close.
    toReturn += "}" + "\n"

    # ret.
    return toReturn
  
  # 
  # members: data.
  # 
  switchKey = "" # driver of switch/case.
  caseConsequence = { } # case -> C++ statement for that case.
  defaultConsequence = "" # C++ statement for default-case.

