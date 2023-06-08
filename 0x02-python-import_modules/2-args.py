import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    print("Number of argument{}: {}".format("s" if num_arguments != 1 else "", num_arguments))
    print("Argument{}:{}".format("" if num_arguments == 0 else "s", " ." if num_arguments == 0 else ""))

    for i, arg in enumerate(arguments, start=1):
        print("{}: {}".format(i, arg))
