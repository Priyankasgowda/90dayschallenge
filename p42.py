# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.

# Given a number n, the task is to find n’th Ugly number.



# Python3 code to find nth ugly number 
  
# This function divides a by greatest  
# divisible power of b 
def maxDivide( a, b ): 
    while a % b == 0: 
        a = a / b 
    return a  
  
# Function to check if a number  
# is ugly or not 
def isUgly( no ): 
    no = maxDivide(no, 2) 
    no = maxDivide(no, 3) 
    no = maxDivide(no, 5) 
    return 1 if no == 1 else 0
  
# Function to get the nth ugly number 
def getNthUglyNo( n ): 
    i = 1
    count = 1 # ugly number count 
  
    # Check for all integers untill  
    # ugly count becomes n 
    while n > count: 
        i += 1
        if isUgly(i): 
            count += 1
    return i 
  
# Driver code to test above functions 
no = getNthUglyNo(150) 
print("150th ugly no. is ", no) 
  
