'''
Problem statement
Write as you speak is a special sequence of strings that starts with string “1” and after one iteration you rewrite the sequence as whatever you speak.

Example :
The first few iterations of the sequence are :
First iteration: “1”
    As we are starting with one.

Second iteration: “11”
    We speak “1” as   “one 1” then we write it as “11”

Third iteration: “21”
    We speak “11” as “Two 1” then we write it as “21”

Fourth iteration: “1211”
    We speak “21” as “one 2, one 1”  then we write it as “1211”

Fifth iteration: “111221”
    We speak “1211” as “one 1, one 2, two 1” then we write it as “111221”

Sixth iteration: “312211”
    We speak “111221” as “three 1, two 2, one 1” then we write it as “312211”
You will be given a single positive integer N, Your task is to write the sequence after N iterations.

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 10
1 <= N <= 30

Time Limit: 1 sec
Sample Input 1 :
2
1
2
Sample Output 1:
1
11
Explanation For Sample Input 2:
First iteration: “1”
    As we are starting with one.

Second iteration: “11”
    We speak “1” as   “one 1” then we write it as “11”
Sample Input 2 :
2
3
4
Sample Output 2:
21
1211
'''

def writeAsYouSpeak(n):
    sequence = "1"  # Initial sequence starts with "1"
    for _ in range(n - 1):  # Perform N-1 iterations
        new_sequence = ""  # Initialize the new sequence for this iteration
        count = 1  # Initialize the count of the current digit
        for i in range(1, len(sequence)):
            if sequence[i] == sequence[i - 1]:  # If the current digit is the same as the previous one, increment the count
                count += 1
            else:  # If the current digit is different from the previous one
                new_sequence += str(count) + sequence[i - 1]  # Add the count and the digit to the new sequence
                count = 1  # Reset the count for the new digit
        new_sequence += str(count) + sequence[-1]  # Add the count and the last digit to the new sequence
        sequence = new_sequence  # Update the sequence for the next iteration
    return sequence
