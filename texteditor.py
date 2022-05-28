from sys import argv

script, filename = argv

print(f"we're going to erase {filename}.") # picksup filename from arg input
print("if you dont want then hit ctrl-c(^C).")
print("if you do wnat then hit return")

input("?")

print("Opening the file...")
target = open(filename,'w')#opens the file in write mode

print("truncate the file.Goodbye")
target.truncate() # deletes stuff from file.

print("Now im going to ask you for three lines")

line1 = input ("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("i'm going to writhe these to file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally , we close it.")
target.close()
