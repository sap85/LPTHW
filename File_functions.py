from sys import argv

script, input_file = argv

def print_all(f): # function to open file 
    #print(f.read()) # reading the contents pf the file.
    return f.read() # above thing can be acheived by using return , however it wont print the data.
 
def rewind(f): 
    f.seek(0) # sets the pointer to begining 

def print_a_line(line_count,f): # giving line count and file name as args
    print(line_count, f.readline()) # linecount is a argument and current line is a variable which takes the value 

current_file = open(input_file) # current file will be the file name you give as arugment

print("First lets print the whole file:\n") 

print_all(current_file) # calling print all function from line 5, then takes filename as arguement and assigns to current file in above step , 

print("Now lets rewind, kind oflike a tape")

rewind(current_file) # calls rewind fun, the pointer goes to  begining of file , cos in above step u have read the file

print("lets print 3 lines:")

current_line = 1  
print_a_line(current_line,current_file)  # calls the fun in 11, gives 1 and file name as arg

current_line += 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file) 

