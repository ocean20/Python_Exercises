# raising exceptions
# raise lets you use your own class
# note: Exception is a class

def func(level):
    if level < 1:
        raise Exception("Invalid level {}".format(level))
    return level

try:
    out_lev = func(-1)
    print("The output level is", out_lev)
except:
    print("Level is less than 1")


