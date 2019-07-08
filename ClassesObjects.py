class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# the variable "myobjectx" holds an object of the class "MyClass" that 
# contains the variable and the function defined within the class 
# called "MyClass".

print(myobjectx.variable)
# output: blah
print(myobjecty.variable)
# output: yackity

myobjectx.function()
# This is a message inside the class

