import gmpy2

def safe_prime(exponent, count):
    for k in range(0,10000000):
        p = 10**exponent + k 
        safe_prime = 0.5*(p-1)
        a = gmpy2.powmod(2, p-1, p)

        if (a == 1): 
            if (gmpy2.is_prime(int(safe_prime))): 
                count += 1
                if count == 1: 
                    print "k = %i \nsafe prime = %i\n" % (k, safe_prime)
                return

def twin_prime(exponent, count):
    for k in range(0,10000000):
        p = 10**exponent + k 
        twin_prime = p + 2
        a = gmpy2.powmod(2, p-1, p)

        if (a == 1): 
            if (gmpy2.is_prime(twin_prime)): 
                count = count + 1
                if count == 1: 
                    print "k = %i \ntwin prime = %i\n" % (k, twin_prime)
                return

def probable_prime(exponent, count):
    for k in range(0,10000000):
        p = 10**exponent + k 
        a = gmpy2.powmod(2, p-1, p)

        if (a == 1): 
            count = count + 1
            if count == 1: 
                print "k = %i \nprobable prime = %i\n" % (k, p)
            return

def is_prime(r, count):
    for k in range(0,10000000):
        p = r + k
        a = gmpy2.powmod(2, p-1, p)

        if (a == 1): 
            if (gmpy2.is_prime(k)): 
                count = count + 1
                if count == 1: 
                    print "k = %i \nprime = %i\n" % (k, p)
                return

#safe_prime(30, 0)
twin_prime(30, 0)
probable_prime(299, 0)
is_prime(4757465356727831999004128791705437327848295392355362834943053456110093459345837361621774882384242053, 0)
