import random

def random_number10():
    return random.randint(0, 10)

def random_number100():
    return random.randint(0, 100)

if __name__ == "__main__":
    print(random_number10())
    print("This came from random_number.py")