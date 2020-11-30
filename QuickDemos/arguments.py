import argparse
parser = argparse.ArgumentParser()

# This is prefered
parser.add_argument("-r", "--reverse", help="This will reverse the order of the array", action="store_true")

# This is considered poor practice.
parser.add_argument("number", help="This number will printed from one to the number")   
args = parser.parse_args()



# Factorial

# Provide a number and we'll calculate the factorial of that number.
def array_of_numbers(number):
    arr = []
    for index in range(number + 1):
        arr.append(index)

    if args.reverse:
        arr = list(reversed(arr))

    return arr

print(array_of_numbers(int(args.number)))