import os

def calc(num1 , operation , num2):
    '''
    this is function do basic calculation (+  -  *  /  ^  %) betweewn two numbers with operation passed as string
    
    #parameters 
    num1 ,num: numbers to be calculated
    operation: a string represent the operation betwean the two numbers
    
    #examples
    >>>print (calc(4,'*',-5))
    -20 
    >>>print (calc(200,'/',10)+calc(10,'^',2))
    120
    '''
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
        print("valid operations are (+  -  *  /  ^  %)")

def extract_problems(file_name = "problems.txt"):    
    '''
    this function reads problem from a text file and return them as a list 
    of seprated problems as string
    if no file included it will create a new one
    called problem.text in same directory

    # parametars
    file_name : the path of the file or just name if same directory

    # problem.txt sample
    1- 0
    1 +      2
    -10 * 3

    # example usage
    >>> print (extract_problems("problem.txt"))
    ['1- 0','1 +   2','-10 * 3']
    '''
    #try opening file if no file excest create it
    try:
        problem_file=open(file_name,"rt")
    except IOError:
        problem_file = open(file_name,"a")
        problem_file.close()
        print ("please add problems to "+file_name)
        exit()

    #extracting problems from file exit if nothing excest
    problems = problem_file.read()
    problems = problems.split('\n')
    
    #if file is empty close
    if len(problems) == 1 and len(problems[0]) == 0:
        print ("please add problems to problem.txt \nfile is empty")        
        exit()

    #close file and return problems
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