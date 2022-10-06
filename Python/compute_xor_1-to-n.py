'''
The below function returns the XOR from 1 to n
We can observe a pattern from the below example

Number Binary-Repr  XOR-from 1-to-n

1         1           [0001]  <----- We get a 1
2        10           [0011]  <----- Equals to n+1
3        11           [0000]  <----- We get a 0
4       100           [0100]  <----- Equals to n
5       101           [0001]  <----- We get a 1
6       110           [0111]  <----- Equals to n+1
7       111           [0000]  <----- We get 0
8      1000           [1000]  <----- Equals to n
9      1001           [0001]  <----- We get a 1
10     1010           [1011]  <----- Equals to n+1
11     1011           [0000]  <------ We get 0
'''



def compute_xor(n):

    if n%4 == 0:
        return n

    elif n%4 == 1:
        return 1

    elif n%4 == 2:
        return n+1

    else:
        # n%4 == 3
        return 0
