# Overlapping Subproblems Property in Dynamic Programming | DP-1
# Dynamic Programming is an algorithmic paradigm that solves a given complex problem by breaking it into subproblems and stores the results of subproblems to avoid computing the same results again. Following are the two main properties of a problem that suggests that the given problem can be solved using Dynamic programming.

# In this post, we will discuss first property (Overlapping Subproblems) in detail. The second property of Dynamic programming is discussed in next post i.e. Set 2.

# 1) Overlapping Subproblems
# 2) Optimal Substructure

# 1) Overlapping Subproblems:
# Like Divide and Conquer, Dynamic Programming combines solutions to sub-problems. Dynamic Programming is mainly used when solutions of same subproblems are needed again and again. In dynamic programming, computed solutions to subproblems are stored in a table so that these don’t have to be recomputed. So Dynamic Programming is not useful when there are no common (overlapping) subproblems because there is no point storing the solutions if they are not needed again. For example, Binary Search doesn’t have common subproblems. If we take an example of following recursive program for Fibonacci Numbers, there are many subproblems which are solved again and again.



# Python program for Memoized version of nth Fibonacci number 
  
# Function to calculate nth Fibonacci number 
def fib(n, lookup): 
  
    # Base case 
    if n == 0 or n == 1 : 
        lookup[n] = n 
  
    # If the value is not calculated previously then calculate it 
    if lookup[n] is None: 
        lookup[n] = fib(n-1 , lookup)  + fib(n-2 , lookup)  
  
    # return the value corresponding to that value of n 
    return lookup[n] 
# end of function 
  
# Driver program to test the above function 
def main(): 
    n = 34 
    # Declaration of lookup table 
    # Handles till n = 100  
    lookup = [None]*(101) 
    print "Fibonacci Number is ", fib(n, lookup) 
  
if __name__=="__main__": 
    main()