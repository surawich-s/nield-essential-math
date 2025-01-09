from math import exp
p = 1000 # principal, starting amount
r = .05 # interest rate, by year
t = 3.0 # time, number of years
a = p * exp(r*t)
print(a)