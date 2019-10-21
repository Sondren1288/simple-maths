def count_digits(n):
   """
   count the number of digita in the given number.
   """
    if n == 0:
        return 1
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count

if __name__ == '__main__':
    number = input("Enter a number")
    print("The number of digits in the number is = {}".format(count_digits(number)))
