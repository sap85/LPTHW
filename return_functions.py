def add(a,b):
    print(f"adding {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"subtracting {a}-{b}")
    return a-b

def multiply(a,b):
    print(f"multi {a},{b}")
    return a * b

def devide(a,b):
    print(f"divid {a}/{b}")
    return a / b


print("lets do some math")

age = add(30,5)
height = subtract(78,4)
weigh = multiply(90,2)
iq = devide(100,2)

print (f"age:{age},height ={height},weight = {weigh},id ={iq}")


# a puzzle for extra credit , type in anyway
print("here is puzzle")

what = add(age,subtract(height,multiply(weigh,devide(iq,2))))

print("this becomes:", what,"can you do it by hand")
