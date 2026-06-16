
# Time Complexity

1) O(1)

Example :

print("Hello") O(1)   |
a = 10         O(1)   |-> O(1) X 4 = O(4)
b = 10         O(1)   |-> still O(1) constant. These all are independent lines
return a+b     O(1)   |

For full program's time complexity -> max of TC of all independent sections 

If a section's value changes with change in input that is dependent, and veice-versa

Independent of input ->
for i in range(100):
    print(i)

2) O(n)

Example :

Dependent on input ->
n = int(input())
for i in range(n):
    print(i)

The loop is running for n times(dependent on input), ao the TC of this function will be O(n)

Even if loop is running till n-1, the TC will be O(n) and not O(n-1) because we consider the highes power of n, like in O(n-1), we can write it as O(n^1 - n^0), so O(n).

Also if O(n^2 + 2n - 3) -> O(n^2)

3) O(n^2)

Example :

Again dependent on input ->
n = int(input())
for i in range(n):
    for j in range(n):
        print(i)

4) O(n logn) -> sort

Example :

n = int(input())
for i in range(n):
    print(i)
arr = [ 3,5,2,6,2,3,6]
arr = arr.sort()
print(arr)

TC -> O(n logn)