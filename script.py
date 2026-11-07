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
        if len(program.strip()) < len("STORE:"):
            print(f"Error: Line {line + 1}: missing variable name")

        elif tokens[line + 1].strip() == "":
            print(f"Error: Line {line + 2}: missing value to store")


        else: 
            vars[program.strip().split()[1]] = tokens[line + 1].strip()



    """if "RUN:" in program:
        if len("output!") == len(tokens[line + 1].strip()):
            print()
            #print empty line like in python"""



print(tokens)
print(vars)



    


        