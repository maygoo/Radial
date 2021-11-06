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

    def visitAdd(self, ctx: RadialParser.AddContext):
        left = ctx.getChild(0)
        right = ctx.getChild(2)
        
        return self.builder.add(self.visit(left), self.visit(right), 'adding')

    def visitNumber(self, ctx: RadialParser.NumberContext):
        return i32(ctx.getText())
