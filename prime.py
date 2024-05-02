import numpy as np

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(start, end):
    """Find all prime numbers in a given range using numpy arrays."""
    # Generating the array of numbers in the range
    nums = np.arange(start, end+1)
    # Filter the array for primes using vectorization for the initial conditions
    # and list comprehension for the nuanced prime checking
    prime_nums = np.array([n for n in nums if is_prime(n)])
        
    return prime_nums
