# What does this piece of code do?
# Answer: to find an prime number between 1 and 100 (but 1 may also be one of the output)

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil


p=False
#turn p to true when p is false
while p==False:
    p=True
    #let n be an random number between 1 and 100
    n = randint(1,100)
    #n to power 0.5 and then take the next higher integer
    u = ceil(n**(0.5))
    #for any i in the range of (2, u+1)
    for i in range(2,u+1):
        if n%i == 0:
            p=False


     
print(n)
