# Generated from Radial.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RadialParser import RadialParser
else:
    from RadialParser import RadialParser

# This class defines a complete generic visitor for a parse tree produced by RadialParser.

class RadialVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RadialParser#program.
    def visitProgram(self, ctx:RadialParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RadialParser#Add.
    def visitAdd(self, ctx:RadialParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RadialParser#Number.
    def visitNumber(self, ctx:RadialParser.NumberContext):
        return self.visitChildren(ctx)



del RadialParser