import antlr4
import os
from antlr.RadialParser import RadialParser
from antlr.RadialLexer import RadialLexer
from RadialIRBuilder import RadialIRBuilder
from llvmlite import ir

if __name__=="__main__":
    
    test_dir = 'tests/rad'
    for f in os.listdir(test_dir):
        test_file = f'{test_dir}/{f}'

        print('Parsing', test_file)

        # antlr scanner and parser
        lexer = RadialLexer(antlr4.FileStream(test_file))
        stream = antlr4.CommonTokenStream(lexer)
        parser = RadialParser(stream)
        tree = parser.program()

        # print parse tree for input
        print(tree.toStringTree(parser.ruleNames))

        if parser.getNumberOfSyntaxErrors() > 0:
            print('Encountered errors parsing. Unable to compile file.')
            continue

        # create ir
        module = ir.Module(f)
        visitor = RadialIRBuilder(module).visitProgram(tree)

        # write llvm to file
        # will break if name of file contains rad will fix later
        with open(test_file.replace('rad','ll'), 'w') as out:
            out.write(str(module))
