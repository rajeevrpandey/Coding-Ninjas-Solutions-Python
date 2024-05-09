'''
Problem statement
You have been given an integer array/list(ARR) and a number 'num'. Find and return the total number of pairs in the array/list which sum to 'num'.

Note:
Given array/list can contain duplicate elements. 
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= t <= 10^2
0 <= N <= 10^4
0 <= num <= 10^9

Time Limit: 1 sec
Sample Input 1:
1
9
1 3 6 2 5 4 3 2 4
7
Sample Output 1:
7
Sample Input 2:
2
9
1 3 6 2 5 4 3 2 4
12
6
2 8 10 5 -2 5
10
Sample Output 2:
0
2


 Explanation for Input 2:
Since there doesn't exist any pair with sum equal to 12 for the first query, we print 0.

For the second query, we have 2 pairs in total that sum up to 10. They are, (2, 8) and (5, 5).
'''


from sys import stdin
def pairSum(arr, n, num) :
	#Your code goes here
    
    arr.sort()
    numPair = 0
    startIndex = 0
    endIndex = n-1
    
    while startIndex < endIndex:
        if arr[startIndex] + arr[endIndex] < num:
            startIndex += 1
            
        elif arr[startIndex] + arr[endIndex] > num:
            endIndex -=1
            
        else:
            elementAtStart = arr[startIndex]
            elementAtEnd = arr[endIndex]
            
            if elementAtStart == elementAtEnd:
                totalElements = endIndex - startIndex +1
                numPair += totalElements *(totalElements-1) //2
                return numPair
            
            tempStartIndex = startIndex +1
            tempEndIndex = endIndex -1
            
            while tempStartIndex <= tempEndIndex and arr[tempStartIndex]== elementAtStart:
                tempStartIndex +=1
                
            while tempEndIndex >= tempStartIndex and arr[tempEndIndex] == elementAtEnd:
                tempEndIndex -=1
                
            totalElementsFromStart = tempStartIndex - startIndex
            totalElementsFromEnd =  endIndex - tempEndIndex
            
            numPair += totalElementsFromStart *totalElementsFromEnd
            
            startIndex = tempStartIndex
            endIndex = tempEndIndex
            
    return numPair
