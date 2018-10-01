import os

def calc(num1 , operation , num2):
    if (operation == '+'):
        return num1+num2
    elif(operation== '-'):
        return num1-num2
    elif(operation== '*'):
        return num1*num2
    elif(operation== '/'):
        return num1/num2
    elif(operation== '^'):
        return num1**num2    
    elif(operation== '%'):
        return num1%num2
    else:
        print (num1 + operation + num2 +"not valid operation")
        #TODO print valid operations

def extract_problems():    
    #try opening file if no file excest create it
    try:
        problem_file=open("problems.txt","rt")
    except IOError:
        problem_file = open("problems.txt","a")
        problem_file.close()
        print ("please add problems to problem.txt")
        exit()
    #extracting problems from file exit if nothing excest
    problems = problem_file.read()
    problems = problems.split('\n')
    if len(problems) == 1 and len(problems[0]) == 0:
        print ("please add problems to problem.txt \nfile is empty")        
        exit()
    else:
        problem_file.close()
        return problems

signal = "+-"
operations = "+-*/%^"
numbers = "1234567890"
valid_input = operations + numbers

problems = extract_problems()

for problem in problems:
    #git first num signal

    #git first num

    #git operation

    #git second num signal

    #second number
    pass
else:
    pass