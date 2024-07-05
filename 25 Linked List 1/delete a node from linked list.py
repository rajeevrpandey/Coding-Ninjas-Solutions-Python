'''
Problem statement
You have been given a linked list of integers. Your task is to write a function that deletes a node from a given position, 'POS'.

Note :
Assume that the Indexing for the linked list always starts from 0.

If the position is greater than or equal to the length of the linked list, you should return the same linked list without any change.
Illustration :
The following images depict how the deletion has been performed.
Image-I :

Alt txt

Image-II :

Alt txt

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
3 4 5 2 6 1 9 -1
3
Sample Output 1 :
3 4 5 6 1 9
Explanation of Sample Output 1 :
The data in the node with index 3 is 2 which has been removed.
Sample Input 2 :
3 4 5 2 6 1 9 -1
0
Sample Output 2 :
4 5 2 6 1 9
Constraints :
0 <= N <= 10^5
POS >= 0

Time Limit: 1sec
Expected Complexity :
Time Complexity  : O(N)
Space Complexity  : O(1)
'''

from sys import stdin

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def deleteNode(head, pos) :
    if pos<0 or pos>=length(head):
        return head
    count = 0
    prev = None
    curr = head
    if pos == 0:
        head = head.next
    else:
        while count<pos:
            count += 1
            prev  = curr
            curr = curr.next
        prev.next = curr.next
    del curr
    return head
    
    

   

def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1
    return head
def printLinkedList(head) :
    while head is not None :
        print(head.data, end = " ")
        head = head.next
head = takeInput()
pos = int(stdin.readline().rstrip())
head = deleteNode(head, pos)
printLinkedList(head)
