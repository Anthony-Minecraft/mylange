# IMPORTS
from lanregexes import LanRe
from lantypes import RandomTypeConversions
from lantypes import VariableValue
# Handles Arithmetics of All kinds
class LanArithmetics:
    LambdaOperations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b
    }
    @staticmethod
    def evalute_string(string:str) -> any:
        if LanRe.search(LanRe.GeneralArithmetics, string):
            m = LanRe.match(LanRe.GeneralArithmetics, string)
            left = RandomTypeConversions.convert(m.group(1)).value
            operation = m.group(2)
            right = RandomTypeConversions.convert(m.group(3)).value
            return LanArithmetics.evaluate(left, operation, right)
        else: raise Exception("Arithmetic Evaluation cannot be preformed on this string.")
    @staticmethod
    def evaluate(left:VariableValue, operation:str, right:VariableValue) -> any:
        return LanArithmetics.LambdaOperations[operation](left.value, right.value)