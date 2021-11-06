import antlr4
from antlr.RadialParser import RadialParser
from antlr.RadialLexer import RadialLexer

if __name__=="__main__":
    
    lexer = RadialLexer(antlr4.FileStream('input.rad'))
    stream = antlr4.CommonTokenStream(lexer)
    parser = RadialParser(stream)
    tree = parser.program()
    
    print(tree.toStringTree(parser.ruleNames))    
