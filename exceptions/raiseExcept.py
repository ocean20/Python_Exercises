# raising exceptions

def func(level):
    if level < 1:
        raise("Invalid level", level)
    return level

out_lev = func(10)
print("The output level is", out_lev)
# The output level is 10

'''
The exception is not raised, so the code below can be executed
'''