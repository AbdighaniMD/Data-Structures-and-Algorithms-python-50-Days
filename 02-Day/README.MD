# **Welcome to Day 2 of the DSA Coding Challenge:** 

## Today's Goals (Arrays):

- Learn the fundamentals of Recursion

### Question 1: k-th symbol in Grammar:

We build a table of n rows __(1-indexed).__ We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.

Given two integer n and k, return the kth __(1-indexed)__ symbol in the nth row of a table of n rows.


### Question 2: Josephus problem:

1.Start at the 1st friend.

2.Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.

3.The last friend you counted leaves the circle and loses the game.

4.If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.

5.Else, the last friend in the circle wins the game.

Given the number of friends, n, and an integer k, return the winner of the game.

## Author

- [@AbdighaniMD](https://github.com/AbdighaniMD)