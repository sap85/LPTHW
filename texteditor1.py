from sys import argv

script,filname = argv

#input file to be open

print(f"we are going to erase the contents from {filname}")
print("hit enter to continue else type CTRL ^C at the prompt \n")
input(">")

print("opening file")
target = open(filname,'w')
#target =target.read()
print ("this is the current content in the file",target)


print("now lets delete this file and add some new lines")
target.truncate()

print ("lets write something in the file")
line1 = input("write something here")
line2 = input("LINE2: ")

target.write(line1)
target.write("\n")
target.write(line2)

print("this is the new content")
target = open(filname,'r')
target = target.read()

print(target)


