# Samir Silbak
# Cryptography 1

import gmpy2
import math

def safe_prime(exponent):
    for k in range(0,10000000):
        p = 10**exponent + k 

        # checks to see if p is prime
        a = gmpy2.powmod(2, p-1, p)

        if (a == 1): 
            # since p is prime, check to see if
            # p is a safe prime
            safe_p = gmpy2.c_div(gmpy2.sub(p,1),2)

            if (gmpy2.is_prime(int(safe_p))): 
                print "k = %i \nsafe prime = %i\n" % (k, safe_p)
                return

def twin_prime(exponent):
    for k in range(0,10000000):
        p = 10**exponent + k 

        # checks to see if p is prime
        a = gmpy2.powmod(2, p-1, p)

        if (a == 1): 
            # since p is prime, check to see if
            # p is a twin prime
            twin_p = p + 2

            if (gmpy2.is_prime(twin_p)): 
                print "k = %i \ntwin prime = %i\n" % (k, twin_p)
                return

def probable_prime(exponent):
    for k in range(0,10000000):
        p = 10**exponent + k 
        a = gmpy2.powmod(2, p-1, p)

        if (a == 1): 
            print "k = %i \nprobable prime = %i\n" % (k, p)
            return

def is_prime(r):
    for k in range(0,10000000):
        p = gmpy2.add(r, k)
        a = gmpy2.powmod(2, p-1, p)

        if (a == 1): 
            print "k = %i \nprime = %i\n" % (k, p)
            return

print "-"*80
safe_prime(30)
print "-"*80
twin_prime(30)

print "-"*80
probable_prime(299)
print "-"*80
is_prime(4757465356727831999004128791705437327848295392355362834943053456110093459345837361621774882384242053)
