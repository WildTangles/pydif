"""elementary.py
This file overloads elementary functions which do no have dunder methods
including exponential and trig functions. The functions first try to work 
with x as a dual number and falls back to treating x as a normal numerical type"""

from pydif.dual.dual import Dual 
import numpy as np 

def cos(x):
    try: 
        return Dual(np.cos(x.val), -1 * x.der * np.sin(x.val))
    except:
        return np.cos(x)

def sin(x):
    try: 
        return Dual(np.sin(x.val),  x.der * np.cos(x.val))
    except:
        return np.sin(x)

def tan(x):
    try:
        return Dual(np.tan(x.val), x.der * (1/np.cos(x.val))**2)
    except:
        return np.tan(x)

def arccos(x):
    try:
        return Dual(np.arccos(x.val), -1 * x.der * 1/(np.sqrt(1- x.val**2)))
    except:
        return np.arccos(x)


def arcsin(x):
    try:
        return Dual(np.arcsin(x.val), x.der * 1/(np.sqrt(1- x.val**2)))
    except:
        return np.arcsin(x)


def arctan(x):
    try:
        return Dual(np.arctan(x.val), x.der * 1/(x.val**2 +1))
    except:
        return np.arctan(x)

def sinh(x):
    try:
        return Dual(np.sinh(x.val), x.der * np.cosh(x.val))
    except:
        return np.sinh(x)

def cosh(x):
    try:
        return Dual(np.cosh(x.val), x.der * np.sinh(x.val) )
    except:
        return np.cosh(x)

def tanh(x):
    try:
        return Dual(np.tanh(x.val), x.der * 1/(np.cosh(x.val)**2))
    except:
        return np.tanh(x)

def arcsinh(x):
    try:
        return Dual(np.arcsinh(x.val), x.der * 1/np.sqrt(x.val**2 +1))
    except:
        return np.arcsinh(x)

def arccosh(x):
    try:
        return Dual(np.arccosh(x.val), x.der * (1/np.sqrt(x.val -1) * 1/(np.sqrt(x.val +1))))
    except:
        np.arccosh(x)

def arctanh(x):
    try:
        return Dual(np.arctanh(x.val), -1 * x.der * 1/(x.val**2 -1))
    except:
        np.arctanh(x)

def exp(x):
    try:
        return Dual(np.exp(x.val), x.der * np.exp(x.val))
    except:
        return np.exp(x)

def exp2(x):
    try:
        return Dual(np.exp2(x.val), np.exp2(x.val) * (x.der * np.log(2)))
    except:
        return np.exp2(x)

# natural log 
def log(x):
    try: 
        return Dual(np.log(x.val), (1 / float(x.val)) * x.der  )
    except:
        return np.log(x)    

# log base 2
def log2(x):
    try:
        return Dual(np.log2(x.val), 1/(x.val * np.log(2)) * x.der)
    except:
        return np.log2(x)

# log base 10
def log10(x):
    try:
        return Dual(np.log10(x.val), 1/(x.val * np.log(10)) * x.der)
    except:
        return np.log10(x)


