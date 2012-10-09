# Samir Silbak
# Cryptography 1

import gmpy2
import math

def safe_prime(exponent, count):
    for k in range(0,10000000):
        p = 10**exponent + k 

        # checks to see if p is prime
        a = gmpy2.powmod(2, p-1, p)

        if (a == 1): 
            # since p is prime, check to see if
            # p is a safe prime
            safe_p = 0.5*(p-2)

            if (gmpy2.is_prime(int(safe_p))): 
                count += 1
                if count == 1: 
                    print "k = %i \nsafe prime = %i\n" % (k, safe_p)
                return

def twin_prime(exponent, count):
    for k in range(0,10000000):
        p = 10**exponent + k 

        # checks to see if p is prime
        a = gmpy2.powmod(2, p-1, p)

        if (a == 1): 
            # since p is prime, check to see if
            # p is a twin prime
            twin_p = p + 2

            if (gmpy2.is_prime(twin_p)): 
                count += 1
                if count == 1: 
                    print "k = %i \ntwin prime = %i\n" % (k, twin_p)
                return

def probable_prime(exponent, count):
    for k in range(0,10000000):
        p = 10**exponent + k 
        a = gmpy2.powmod(2, p-1, p)

        if (a == 1): 
            count += 1
            if count == 1: 
                print "k = %i \nprobable prime = %i\n" % (k, p)
            return

def is_prime(r, count):
    for k in range(0,10000000):
        p = r + k
        a = gmpy2.powmod(2, p-1, p)

        if (a == 1): 
            if (gmpy2.is_prime(k)): 
                count += 1
                if count == 1: 
                    print "k = %i \nprime = %i\n" % (k, p)
                return

safe_prime(30,0)
twin_prime(30,0)

probable_prime(299,0)
is_prime(4757465356727831999004128791705437327848295392355362834943053456110093459345837361621774882384242053,0)
