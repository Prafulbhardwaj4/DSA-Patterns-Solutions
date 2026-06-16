"""
Qn.

We are given a number n.

We repeatedly replace the number with the sum of the square of its digits.

We need to determine whether the process ends in 1 or not.

If it ends in 1 -> return True (Happy Number)
Else -> return False

"""

"""
Solution :

This is a Slow and Fast Pointer (Cycle Detection) problem.

Idea :

For a number n,
we repeatedly transform it using:

sum_of_squares_of_digits(n)

Example :

n = 19

19 -> 1² + 9² = 82
82 -> 8² + 2² = 68
68 -> 6² + 8² = 100
100 -> 1² + 0² + 0² = 1

So this number is happy.

But for non-happy numbers,
this process enters a cycle.

So instead of storing all visited numbers,
we use Floyd Cycle Detection.

We treat each number as a node in a sequence.

Next node = sumOfSquares(current number)

We maintain:

slow -> moves one transformation at a time
fast -> moves two transformations at a time

Step 1 :

slow = n
fast = n

Step 2 :

Move both pointers repeatedly:

slow = f(slow)
fast = f(f(fast))

where f(x) = sum of squares of digits

If at any point:

slow == fast

It means we are in a cycle.

Now check:

If cycle contains 1 -> Happy number
If cycle does not contain 1 -> Not happy

So we return False when slow == fast and slow != 1.

If fast reaches 1,
then the process ends successfully,
so we return True.

Helper Function :

sumOfSquares(n)

This function computes:

sum of square of each digit of n

Example :

n = 23

2² + 3² = 13

This transformation is applied repeatedly
until we detect cycle or reach 1.

"""

class Solution:
    def isHappy(self, n: int) -> bool:
        slow = fast = n

        while (fast != 1):
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)

            if slow == fast and slow != 1:
                return False
        return True
    
    def sumOfSquares(self,n):
        sum = 0

        while n > 0:
            d = n % 10
            sum += d * d
            n //= 10
        
        return sum