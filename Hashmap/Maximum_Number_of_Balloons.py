"""
Qn. We are given 1 string, we need to check, how many "balloon" string we can make using that string

"""

"""
Example : "loonbalxballpoon"

"""

"""
Solution :

We will have 2 hashmaps storing frequencies of each character of "balloon" and given text
we will also have a res varaible inititated with infinity

for each char in bal, we will check the minimum required character to create balloon, that will be the number of "balloon" string we can make using that text

Analogy -> A company is only as fast as the slowest worker of the company  


"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ques = "balloon"
        bal = {}
        req = {}
        res = float('inf')

        for ch in ques:
            bal[ch] = bal.get(ch,0) + 1

        for ch in text:
            req[ch] = req.get(ch,0) + 1
        
        for ch in bal:
            res = min(res,req.get(ch,0)//bal[ch])
        
        return res