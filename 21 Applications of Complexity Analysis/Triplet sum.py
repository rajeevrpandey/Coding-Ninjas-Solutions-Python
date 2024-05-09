'''
Problem statement
You have been given a random integer array/list(ARR) and a number X. Find and return the triplet(s) in the array/list which sum to X.

Note :
Given array/list can contain duplicate elements.
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= t <= 10^2
0 <= N <= 10^3
0 <= X <= 10^9

Time Limit: 1 sec
Sample Input 1:
1
7
1 2 3 4 5 6 7 
12
Sample Output 1:
5
Sample Input 2:
2
7
1 2 3 4 5 6 7 
19
9
2 -5 8 -6 0 5 10 11 -3
10
Sample Output 2:
0
5


 Explanation for Input 2:
Since there doesn't exist any triplet with sum equal to 19 for the first query, we print 0.

For the second query, we have 5 triplets in total that sum up to 10. They are, (2, 8, 0), (2, 11, -3), (-5, 5, 10), (8, 5, -3) and (-6, 5, 11)
'''

from sys import stdin

def tripletSum(arr,n,sum):
    arr.sort()
    trip_count=0
    for i in range(n):
        pair_sum=sum-arr[i]
        pair_count=pairSum(arr,i+1,n-1,pair_sum)
        trip_count+=pair_count
       
    return trip_count

def pairSum(arr,s,e,pair_sum):
    pair_count=0
    while s<e:
        if(arr[s]+arr[e]<pair_sum):
            s=s+1
        elif(arr[s]+arr[e]>pair_sum):
            e=e-1
        else:
            if(arr[s]==arr[e]):
                total_ele=(e-s)+1
                pair_count=pair_count+(total_ele*(total_ele-1)//2)
               
                return pair_count
           
            temp_s=s+1
            temp_e=e-1
            while((temp_s<=temp_e) and (arr[temp_s] == arr[s])):
                temp_s+=1
               
            while((temp_e>=temp_s) and (arr[temp_e] == arr[e])):
                temp_e-=1
               
            total_start=temp_s-s
            total_end=e-temp_e
            pair_count=pair_count+(total_start*total_end)
            s=temp_s
            e=temp_e
           
    return pair_count
