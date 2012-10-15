# Samir Silbak
# Cryptography 1
# Hw 4

import gmpy2

def safe_prime(exponent):
    for k in range(0,10000000):
        p = 10**exponent + k 

        # checks to see if p is prime
        a = gmpy2.powmod(2, p-1, p)

        if (a == 1): 
            # since p is prime, check to see if
            # p is a safe prime
            safe_p = gmpy2.c_div(gmpy2.sub(p,1), 2)

            if (gmpy2.is_prime(int(safe_p))): 
                print "k = %i \nsafe prime = %i\n" % (k, safe_p)
                return 

def prim_root():
    #safe_prime(100)
    base = (2,3,5,7,9,11,13)
    for k in base:
        #print "base = ", k

        p = 5000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000021861

        # checks to see if p is prime
        a = gmpy2.powmod(k, gmpy2.c_div(gmpy2.sub(p,1), 2), p)

        if (a != 1): 
            #print "base = %i \nsafe prime = %i\n" % (base, safe_p)
            print "%i is a primitive root modulo %i\n" % (k, p)
        
        else:
            print "%i is not a primitive root modulo %i\n" % (k, p)

    return

#def factor_prime(prime):

#print "-"*80
#safe_prime(100)
#print "-"*80
prim_root()
#print "-"*80
#factor_prime(190248273382547686244479775579416295505415044511)
#print "-"*80
