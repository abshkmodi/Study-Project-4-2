#!/usr/bin/env python
from math import exp,sqrt

# Input stock parameters 
S = input("Enter the initial asset price: ")
K = input("Enter the option strike price: ")
r = input("Enter the risk-free discount rate: ")
v = input("Enter the volatility: ")
N = input("Enter the number of timesteps until expiration: ")
dt = input("Enter the timestep: ")

# Input whether this is a call or a put option
call = raw_input("Is this a call or put option? (C/P) ").upper().startswith('C')

u=exp(v * sqrt(dt) )
d=1/u
p= ( exp(r*dt)-d)/(u-d)

def price(k, us):
    """ Compute the stock price after 'us' growths and 'k - us' decays. """
    return S * (u ** (2 * us - k))

def bopm(k, us):
    """
    Compute the option price for a node 'k' timesteps in the future
    and 'us' growth events. Note that thus there are 'k - us' decay events.
    """

    # Compute the exercise profit
    stockPrice = price(k, us)
    if call: exerciseProfit = max(0, stockPrice - K)
    else:    exerciseProfit = max(0, K - stockPrice)

    # Base case (this is a leaf)
    if k == N: return exerciseProfit

    # Recursive case: compute the binomial value 
    decay = exp(-r * dt)
    expected = p * bopm(k + 1, us + 1) + (1 - p) * bopm(k + 1, us)
    binomial = decay * expected

    # Assume this is an American-style option
    return max(binomial, exerciseProfit)

print ('Computed option price: %.2f' % bopm(0, 0))
