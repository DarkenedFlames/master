import math
from fractions import Fraction
import numpy as np

def factorioRatios(n, b, c, t, i):
    n = np.array(n)
    r = n * c / t
    I = np.ceil(r / i)
    b = np.full(len(r), b)
    
    nums = []
    for f in b/r:
      nums.append(
        Fraction(f)
        .limit_denominator()
        .numerator
      )
    
    M = math.lcm(*nums)
    B = r * M / b
    
    return f"r: {r} \n I: {I} \n M: {M} \n B: {B}"

print(factorioRatios([1,3,1], 15, 0.5, 0.5, 0.83))
