Hashmaps :

- What is Hashmap :

Take an example of a diary. Let's just say you maintain a diary

You write about 13, 14, 15 June in your diary
and then on 23 you want to know what happened on 14th of June
you'll just open your diary, check 14 June page, and you'll get to know

Same is with Hashmaps :

We store data in key:value pairs in hashmaps
Where keys are like dates, and values are like events happened on that day

We need to follow a format (key:value), just like in diary

# Keys are Unique, Values can be Duplicate

# Why HashMap :

1) Where we need to find value of any given key, Hashmap can give it to us in O(1) average time

2) To count frequency / occurrences of elements

3) To check if we have that particular key or not

4) To store and reuse previously seen data (avoid recomputation)

# Where to apply :

1) Key : Value Pair problems

2) Frequency counting problems

3) Lookup / search optimization problems

# When to apply :

1) Where we need to remember old data

2) Exact value is asked (or needs to be tracked)

3) Key available or not check is required

4) Mapping relationships between elements

# Steps to implement :

1) Initialize hashmap

   f = {}

2) Store values in hashmap

   f[key] = value

   Example:
   f[1] = 10
   f[2] = 20

3) Access / check key

   if key in f:
       use f[key]

4) Update values

   f[key] = f.get(key, 0) + 1

5) Delete key if required

   del f[key]

6) Get size of hashmap

   len(f)

# Intuition :

- Instead of searching again and again in array,
  we store information once and reuse it

- It converts O(n) search into O(1) average lookup

- Helps in remembering past computations efficiently

# Key Idea :

"Store once, reuse many times using key-value mapping"

# Time Complexity :

- Insert → O(1) average
- Search → O(1) average
- Delete → O(1) average

# Space Complexity :

- O(n) → storing all key-value pairs