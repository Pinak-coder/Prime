import math 
def is_prime(n): 
    if n <= 1: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(2, 1 + max_div): 
        if n % i == 0: 
            return False
    return True
n=int(input())
if is_prime(n) :
    print('Yes it is Prime')
else:
    print('No it is not Prime')