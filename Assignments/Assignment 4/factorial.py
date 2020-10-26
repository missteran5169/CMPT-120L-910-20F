def factorial(target) -> int:
    total = 0
    for number in range(target + 1):
        total += number
    return total

if __name__ == "__main__":
    user_number = int(input("Please enter a number that you'd like to see the factorial of.\n"))
    example = factorial(user_number)
    print("The factorial of", user_number, "is", example)