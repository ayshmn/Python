# Ways to Import a Module
# 1. Import Entire Module
import math

print(math.sqrt(25))


# 2. Import Specific Function
from math import sqrt

print(sqrt(49))


# 3. Import Multiple Functions
from math import sqrt, factorial

print(sqrt(64))
print(factorial(5))


# 4. Import with Alias
import math as m

print(m.sqrt(81))


# Built-in Modules in Python

# Math Module

import math

print(math.pi)
print(math.factorial(5))


# Random Module
import random

print(random.randint(1, 10))


# Datetime Module
import datetime

print(datetime.datetime.now())


# OS Module
import os

print(os.getcwd())