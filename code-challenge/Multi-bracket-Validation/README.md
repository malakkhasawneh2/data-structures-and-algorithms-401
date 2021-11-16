# PR : https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/pull/14

# Challenge Summary
writing a function that, when given a string, can determine wither or not brackets are being opened and closed at the proper places. The function returns True or False based on correct bracket usage.
## Whiteboard Process
![Whiteboard Solution](https://github.com/malakkhasawneh2/data-structures-and-algorithms-401/blob/stack-queue-brackets/code-challenge/Multi-bracket-Validation/lab13.PNG)

## Approach & Efficiency
For this module, the goal was to traverse the string that came into the function as input - for loop was used. Then conditionals were set up to check...
IF the character is an open bracket THEN add the character to a string of all the open brackets (open_brac variable).
IF the character is a closing bracket THEN check the end of the string (open_brac) and if the end of open_brac was the corresponding open bracket, continue the loop and remove the open bracket character from the open_brac string.

The for loop continues for the length of the string. At the end, if all the conditions are met along the way, one last conditional is checked. If the open_brac string that was storing all the open bracket characters is now empty... that means that all of the brackets were opened and were closed. Only then can the function return True.

The BigO for this function is O(n) for both time and space. The entire input string is traversed each time the function is invoked. The bigger the input, the bigger the space and time.

## Solution
```
Input string: (){}[]
Output: True
```
```
Input string: ({[hello_world]}){}
Output: True
```
```
Input string: ({)}[]
Output: False
```