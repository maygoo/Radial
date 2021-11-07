from antlr.RadialVisitor import RadialVisitor
from antlr.RadialParser import RadialParser
from llvmlite import ir

i32 = ir.IntType(32)


class RadialIRBuilder(RadialVisitor):
    def __init__(self, module: ir.Module) -> None:
        # define the main function of the IR
        function_type = ir.FunctionType(i32, ())
        main = ir.Function(module, function_type, 'main')
        block = main.append_basic_block('entry')
        self.builder = ir.IRBuilder(block)

        super().__init__()

    def visitProgram(self, ctx: RadialParser.ProgramContext):
        self.builder.ret(self.visitChildren(ctx))

    def visitStatement(self, ctx: RadialParser.StatementContext):
        # ignore the second child, which is just ';'
        return self.visit(ctx.getChild(0))

    # Expressions
    def visitBinOp(self, ctx: RadialParser.BinOpContext):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = self.visit(ctx.getChild(1))
        return op(left, right)

    # Operators
    def visitAdd(self, ctx: RadialParser.AddContext):
        return self.builder.add
    
    def visitSub(self, ctx: RadialParser.SubContext):
        return self.builder.sub
    
    def visitMul(self, ctx: RadialParser.MulContext):
        return self.builder.mul

    def visitDiv(self, ctx: RadialParser.DivContext):
        # unsigned int division
        return self.builder.udiv

    def visitMod(self, ctx: RadialParser.ModContext):
        # unsigned
        return self.builder.urem

    # Literals
    def visitInt(self, ctx: RadialParser.IntContext):
        return i32(ctx.getText())

    def visitDec(self, ctx: RadialParser.DecContext):
        pass #TODO

    def visitStr(self, ctx: RadialParser.StrContext):
        pass #TODO
