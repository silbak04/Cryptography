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
                print "-"*136
                return safe_p

def prim_root():

    # calls safe_prime func
    # and uses safe prime
    # for primitive root
    p = safe_prime(100)

    base = (2,3,5,7,11,13)
    
    for k in base:

        # checks to see if p is prime
        a = gmpy2.powmod(k, gmpy2.c_div(gmpy2.sub(p,1), 2), p)

        if (a != 1): 
            print "%i is a primitive root modulo     %i\n" % (k, p)
        
        else:
            print "%i is not a primitive root modulo %i\n" % (k, p)

    return

def factor_prime(prime):

    # p - 1 is 37-smooth
    base = 2
    k_sm = 37

    # pow(base,k_sm!) mod prime
    a = gmpy2.powmod(base, gmpy2.fac(k_sm), prime)

    # gcd(r_k - 1, prime)
    p = gmpy2.gcd(a-1, prime)

    # get second factor of prime
    q = (prime / p)

    # make sure factors (pq) are prime
    if (gmpy2.is_prime(p) and gmpy2.is_prime(q)):
        print "p = ", p
        print "q = ", q

        # make sure n = p*q = prime number
        n = gmpy2.mul(p,q)

        if (n == prime):
            print "n = ", gmpy2.mul(p,q)

    return

print "-"*136
prim_root()
print "-"*136
factor_prime(190248273382547686244479775579416295505415044511)
print "-"*136
