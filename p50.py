# Activity Selection Problem | Greedy Algo-1
# Greedy is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. Greedy algorithms are used for optimization problems. An optimization problem can be solved using Greedy if the problem has the following property: At every step, we can make a choice that looks best at the moment, and we get the optimal solution of the complete problem.
# If a Greedy Algorithm can solve a problem, then it generally becomes the best method to solve that problem as the Greedy algorithms are in general more efficient than other techniques like Dynamic Programming. But Greedy algorithms cannot always be applied. For example, Fractional Knapsack problem (See this) can be solved using Greedy, but 0-1 Knapsack cannot be solved using Greedy.




"""The following implementation assumes that the activities 
are already sorted according to their finish time"""
  
"""Prints a maximum set of activities that can be done by a 
single person, one at a time"""
# n --> Total number of activities 
# s[]--> An array that contains start time of all activities 
# f[] --> An array that contains finish time of all activities 
  
def printMaxActivities(s , f ): 
    n = len(f) 
    print "The following activities are selected"
  
    # The first activity is always selected 
    i = 0
    print i, 
  
    # Consider rest of the activities 
    for j in xrange(n): 
  
        # If this activity has start time greater than 
        # or equal to the finish time of previously 
        # selected activity, then select it 
        if s[j] >= f[i]: 
            print j, 
            i = j 
  
# Driver program to test above function 
s = [1 , 3 , 0 , 5 , 8 , 5] 
f = [2 , 4 , 6 , 7 , 9 , 9] 
printMaxActivities(s , f)