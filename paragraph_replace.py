my_paragraph  = '''
Compiler is operates in various phases each phase transforms the source program from one
representation to another.
Every phase is take inputs from its previous stage and feeds its output is to the next phase of
the compiler.
there are 6 phases in a compiler. Each of this phase help in converting the high-level
language the machine code.
The phases of a compiler is: there is Lexical analysis Syntax analysis Semantic analysis
Intermediate code generator Code optimizer, Code generator
'''
for i in (("is", "are"), ("there", "that")):
    my_paragraph = my_paragraph.replace(*i)
print(my_paragraph)
