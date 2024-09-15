class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True] * n

        if n<= 2:
            return 0

        p = 2
        while (p * p <= n):
    
            if (prime[p] == True):
  
                for i in range(p * p, n, p):
                    prime[i] = False
            p += 1
    
        return prime.count(True) - 2
            
