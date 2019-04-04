# Greedy Algorithm to find Minimum number of Coins
# Given a value V, if we want to make change for V Rs, and we have infinite supply of each of the denominations in Indian currency, i.e., we have infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, what is the minimum number of coins and/or notes needed to make the change?


# Python 3 program to find minimum  
# number of denominations 
  
def findMin(V): 
      
    # All denominations of Indian Currency 
    deno = [1, 2, 5, 10, 20, 50,  
            100, 500, 1000] 
    n = len(deno) 
      
    # Initialize Result 
    ans = [] 
  
    # Traverse through all denomination 
    i = n - 1
    while(i >= 0): 
          
        # Find denominations 
        while (V >= deno[i]): 
            V -= deno[i] 
            ans.append(deno[i]) 
  
        i -= 1
  
    # Print result 
    for i in range(len(ans)): 
        print(ans[i], end = " ") 
  
# Driver Code 
if __name__ == '__main__': 
    n = 93
    print("Following is minimal number", 
          "of change for", n, ": ", end = "") 
    findMin(n) 