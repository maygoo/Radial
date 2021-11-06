# Generated from Radial.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RadialParser import RadialParser
else:
    from RadialParser import RadialParser

# This class defines a complete listener for a parse tree produced by RadialParser.
class RadialListener(ParseTreeListener):

    # Enter a parse tree produced by RadialParser#program.
    def enterProgram(self, ctx:RadialParser.ProgramContext):
        pass

    # Exit a parse tree produced by RadialParser#program.
    def exitProgram(self, ctx:RadialParser.ProgramContext):
        pass


    # Enter a parse tree produced by RadialParser#Add.
    def enterAdd(self, ctx:RadialParser.AddContext):
        pass

    # Exit a parse tree produced by RadialParser#Add.
    def exitAdd(self, ctx:RadialParser.AddContext):
        pass


    # Enter a parse tree produced by RadialParser#Number.
    def enterNumber(self, ctx:RadialParser.NumberContext):
        pass

    # Exit a parse tree produced by RadialParser#Number.
    def exitNumber(self, ctx:RadialParser.NumberContext):
        pass



del RadialParser