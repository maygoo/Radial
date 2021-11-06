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


    # Visit a parse tree produced by RadialParser#statement_func.
    def visitStatement_func(self, ctx:RadialParser.Statement_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RadialParser#statement.
    def visitStatement(self, ctx:RadialParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RadialParser#var_def.
    def visitVar_def(self, ctx:RadialParser.Var_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RadialParser#func_def.
    def visitFunc_def(self, ctx:RadialParser.Func_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RadialParser#Add.
    def visitAdd(self, ctx:RadialParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RadialParser#Call.
    def visitCall(self, ctx:RadialParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RadialParser#Mul.
    def visitMul(self, ctx:RadialParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RadialParser#Lit.
    def visitLit(self, ctx:RadialParser.LitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RadialParser#Var.
    def visitVar(self, ctx:RadialParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RadialParser#Int.
    def visitInt(self, ctx:RadialParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RadialParser#Dec.
    def visitDec(self, ctx:RadialParser.DecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RadialParser#Str.
    def visitStr(self, ctx:RadialParser.StrContext):
        return self.visitChildren(ctx)



del RadialParser