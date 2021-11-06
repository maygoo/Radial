# Radial

A hobby project to create a programming language dubbed `Radial` and compile it to the LLVM IR.

## Requirements

ANTLR jar added to the java classpath, e.g.:

```bash
export CLASSPATH=".:/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH"
```

Python modules for antlr4 and llvm:

```bash
python -m pip install antlr4-python3-runtime llvmlite
```
