import collections
#list1=[10,10,10,10,10,20,20,20,20,30,20,40,10,30,40,50]

b=[]
#functions to find unique elements from a list of given numbers and frequency of those numbers.

def uniqueelements(list1):
    #print ("Unique elements =")
    for i in list1:
        if i not in b:
            b.append(i)
    return(b)
def frequency(list1):
    x=collections.Counter(list1)
    #print ("Frequency =")
    return(x)
    
#print ("Unique elements =")
#print(uniqueelements(list1))
#print ("Frequency =")
#print(frequency(list1))









