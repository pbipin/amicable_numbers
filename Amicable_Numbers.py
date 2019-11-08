"""
Author: Bipin P. (mailto: bipinp2013@gmail.com)
http://iambipin.com

101010101    10  101010101    10  101     10    101010101
1010101010   10  1010101010   10  1010    10    1010101010
10      101  10  10      101  10  10 01   10    10      101
10      101  10  10      101  10  10  10  10    10      101
1010101010   10  1010101010   10  10   01 10    1010101010
1010101010   10  101010101    10  10    1010    101010101
10      101  10  10           10  10     010    10
10      101  10  10           10  10      10    10
1010101010   10  10           10  10      10    10
101010101    10  10           10  10      10    10  10

Amicable Numbers:
Python program to find amicable numbers within a range. Two numbers are classified as amicable numbers 
if the sum of proper divisors of one number is equal to the other number, and vice versa. 
For example, 220 and 280 are amicable numbers for the above-mentioned reason. 
220 - 1+2+4+5+10+11+20+22+44+55+110 = 284 
284 - 1+2+4+71+142 = 220
"""

def amicableNum(i):
    """
    Function to create a set of amicable numbers
    """
    global amicable
    j = 1
    sumofdiv = 0
    
    if(i % 2 == 0): #for even numbers
        while(j < (i/2)+1):
            if(i % j == 0):
                sumofdiv += j
            j += 1

    else: #for odd numbers
        while(j < (i/3)+1):
            if(i % j == 0):
                sumofdiv += j
            j += 1

    k = 1
    ssum = 0
    while(k < sumofdiv):
        if(sumofdiv % k == 0):
            ssum += k
        k += 1

    if(ssum == i) and (sumofdiv != i): #condition for amicable numbers
        amicable.add(i)
        amicable.add(sumofdiv)

        
try:
    num = int(input('Enter the number within which amicable numbers are to be found: '))
    if(num <= 2):
        raise ValueError
    
    indexList = []
    amicable = set()
    numrange = range(2, num)
    for i in range(2, num):
        amicableNum(i)
    
    amicList = list(amicable) #conversion from set to list
    amicList.sort() #list is sorted
    #list slicing(based on even and odd positions of elements) with zip() to convert in to list of 
    #tuples(for printing as pairs)
    amicList = zip(amicList[::2], amicList[1::2]) 
    
    aster = '*'
    print(aster * 60)
    
    print('The pair(s) of amicable numbers within {0} are:' .format(num))
    print(*amicList)
    print(aster * 60)
        
except(ValueError):
    print('Please enter a valid integer number greater than 2')