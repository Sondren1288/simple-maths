

def fibonacci_calculator(count):
    result=[0,1]
    j=2
    while(j<=count):
        print(j)
        number=result[j-1]+result[j-2]
        result.append(number)
        j=j+1
        print(result)
fibonacci_calculator(8)