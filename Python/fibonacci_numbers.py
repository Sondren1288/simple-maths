def fibonacci(n):
   """
   Returns nth fibonacci number
   """
    if n < 2:
        return n
  return fibonacci(n-2) + fibonacci(n-1)

print("Enter a number: ")
print("output : {}".format(fibonacci(x))
