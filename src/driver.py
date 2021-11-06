import antlr4
from antlr.RadialParser import RadialParser
from antlr.RadialLexer import RadialLexer
from RadialIRBuilder import RadialIRBuilder
from llvmlite import ir

if __name__=="__main__":
    
    input_file = 'input.rad'

    lexer = RadialLexer(antlr4.FileStream(input_file))
    stream = antlr4.CommonTokenStream(lexer)
    parser = RadialParser(stream)
    tree = parser.program()
    
    print(tree.toStringTree(parser.ruleNames))

    # initialise ir builder
    module = ir.Module(input_file)

    # attempting to parse
    visitor = RadialIRBuilder(module).visitProgram(tree)
    print(module)
