# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 17:25:40 2020

@author: fredr
"""

"""
THEORY ON METHODS USED: 
Degree of precision def 5.2 page 258 i intro. vit.ber: 
Funksjoner til og med denne graden integreres eksakt av metoden. For Simpsons er den 3. grad.

Simpson's rule (5.22) p 257:
integral of f(x) from xo to x2 = h/3 * (f(xo) + 4f(x1) + f(x2)) - h^5 / 90 * f''''(c)
Der h = x2- x1 = x1 - xo.
Så avstanden mellom x2 og xo er 2h.
"""


import numpy as np

def simpsons(x_0, x_2, f, *parameters): #Simpsons method
    x_1 = (x_2 + x_0)/2
    return ((x_2 - x_1)/3  * (f(x_0, *parameters) + 4*f(x_1, *parameters) + f(x_2, *parameters)))
    
def adap_q(x_0, x_2, f, method, TOL, *parameters):
    #x_0, x_2 is the partition of the integral. f is the function 
    #"method" is the numerical method used. e.g. Simpson's method.
    #*paramaters are parameters for f
    x_1 = (x_0 + x_2)/2
    Q, q1, q2 = method(x_0, x_2, f, *parameters), method(x_0,x_1,f, *parameters), method(x_1,x_2,f, *parameters) 
    if( np.abs(Q - q1 - q2) < 10*TOL): #(3*TOL * (x_2 - x_0 /(b - a))):
        return Q
    return(adap_q(x_0, x_1, f, method, TOL, *parameters) + adap_q(x_1, x_2, f, method, TOL, *parameters))

if __name__ == '__main__':  
    print(adap_q(2.13,14.62,(lambda x: x**5 + x**(-4)+np.exp(-x**4)),simpsons,0.0000001))
    print("\nGeogebra gives 1627529,396")
print("num_int_adaptive.py called as:", __name__)
