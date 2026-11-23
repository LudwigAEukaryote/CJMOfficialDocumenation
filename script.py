import sys
#Allow python to interact with the OS
conn = "HelloWorld.cjm"

tokens = []
print("Compiling...")


with open(conn, 'r') as code:
    #Open the file and read it, the computer names it at 'code'
    for line in code:
        if line.strip() == "":
            continue
        ##Check if the line is empty, if it is, skip it
        else:
            line.strip().split()
            tokens.append(line)
            #append only the lines that are not empty 

prec = []
##Hold the the variables and functions that are called before the main functions

comp = []
##Main function

vars = {}
##Defined variables


for line, program in enumerate(tokens):
    #each line is assigned a number
    # each program is the line of code

    if "STORE:" in program:
        if len(program.strip()) + 5 < len("STORE:"):
            print(f"Error: Line {line + 1}: missing variable name")

        elif tokens[line + 1].strip() == "":
            print(f"Error: Line {line + 2}: missing value to store")



        else: 
            vars[program.strip().split()[1]] = tokens[line + 1].strip()



    if "RUN:" in program:
        if len("output!") == len(tokens[line + 1].strip()):
            print("\n")
            #print empty line like in python


##Assembler Code --> x86
assembler = "assembler.asm"
asm = open(assembler, 'w')
##Allows python to be able to write in the assembly file

asm.write("""; Info---
bits 64
default rel ; allows for adresses to be moved 

""")

asm.write("""section .bss; this will hold varibles

""")

asm.write("""section .data ; this will hold constants --> only moved not changed

""")

asm.write("""section .text ; hold the main function --> assembly logic
global main ; int main in C
extern ExitProcess ; terminal can end Assembly program


extern printf
extern scanf
;pulls these functions from C 
;can read user input
;GCC as linker

main: ; entry port

;creating shadow space --> 32 bytes

\t PUSH rbp ; push the base pointer to the top of the stack
\t MOV rbp, rsp ; move the the stack pointer into the base pointer
\t SUB rsp, 32 ; subtract 32 from the bottom of the stack

""")



asm.close()
#Closes the assembler

for defs in vars:
    if 

"""
print(tokens)
print(vars)"""



    


        