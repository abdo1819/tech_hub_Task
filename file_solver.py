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

#valid operation 
operations = "-+*/%^"
#note  " - " minus must be at first so if it is just signal operation will be the real one     
numbers = "1234567890"

valid_input = operations + numbers

problems = extract_problems()

for problem in problems:
    #git operation index
    for operation in operations:
        if operation in problem:
            index =problem.index(operation)
    #git first num
    
    try:
        num1 = int(problem[:index])

        #git operation
        operation = problem[index]

        #second number
        num2 = int(problem[index+1:])

        #print result
        print(problem)
        print(calc(num1,operation,num2))

    except ValueError:
        pass
    except IndexError:
        pass