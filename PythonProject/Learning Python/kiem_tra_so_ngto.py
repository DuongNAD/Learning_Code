import math

def is_prime(n):
    """
    Kiem tra so nguyen to
    """
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


input_number = int(input("Enter a number: "))

if is_prime(input_number):
    print(f"{input_number} is prime number")

else:
    print(f"{input_number} is not prime number")

for i in range (2, int(input_number) + 1,1):
    if is_prime(i):
        print(i)

