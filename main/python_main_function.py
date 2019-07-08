# https://www.journaldev.com/17752/python-main-function

print("Hello")

print("__name__ value:", __name__)
# output: __name__ value: __main__

def main():
    print("python main function")

if __name__ == '__main__':
    main()

# If the python source file is imported as module, python interpreter sets the __name__ value to module name,
# so the if condition will return false and main method will not be executed.