#Variable
variable = 10
print(variable)

#Function
def test():
    print(f"function")
test()

#For Loop
for i in range(4):
    print(f"for")

#While loop
while i == 0:
    print(f"while")

#If loop
if variable == 10:
    print(f"If")

#Function paramaters
def function_paramaters(times):
    for i in range(times):
        print(f"Hi")

function_paramaters(4) #4 is the amount of times the word "Hi" will be printed in the terminal


#Else loop
if variable == 5:
    print(f"yes")
else:
    print(f"no")

#Elif loop (else if)
if variable == 5:
    #If
    print(f"yes")
elif variable == 10:
    #Elif
    print(f"no")
else:
    #Else
    print(f"undefined")