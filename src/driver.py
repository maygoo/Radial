import antlr4
from antlr.RadialParser import RadialParser
from antlr.RadialLexer import RadialLexer
from llvmlite import ir

if __name__=="__main__":
    
    input_file = 'input.rad'

    lexer = RadialLexer(antlr4.FileStream(input_file))
    stream = antlr4.CommonTokenStream(lexer)
    parser = RadialParser(stream)
    tree = parser.program()
    
    print(tree.toStringTree(parser.ruleNames))
    
    # types
    i32 = ir.IntType(32)
    function_type = ir.FunctionType(i32, ())

    # builder
    module = ir.Module(input_file)
    function = ir.Function(module, function_type, 'main')
    block = function.append_basic_block('entry')
    builder = ir.IRBuilder(block)
    builder.add(i32(10), i32(20))
    builder.ret_void()

    print(module)