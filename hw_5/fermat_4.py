# Samir Silbak
# Cryptography 1
# Hw 5

import gmpy2

R = 178364106734022579915357141142372699027567004266137223687186843534009772394527786774481895952357016567786317933763105630159756629545998973467529932163
S = 748527342779114509108012294258799978873616793124897195999683439531549256719899101076581473269289844176980812683605133154847306734359363305955569274099
M = 7968676964940788667185699649931393523249305289513974584333136676341463565681661753884408243356921203756614416198117542773426855898584332117778238518937443311869418322477842614544024955562101488244089968303933818924421750697467476415540142041425360265505864339061433372577700188914846968223935567188

def probable_prime(prime, i):
    for k in range(0,10000000):
        p = prime + k

        # check to see if p is prime
        a = gmpy2.powmod(2, p-1, p)
        # check to see if 3 divides into prime - 1
        b = gmpy2.mpz(gmpy2.f_mod(p-1, 3))

        if (a == 1 and b == 1): 
            print "k_%i = %i" %(i, k)
            print "p_%i = %i" %(i, p)
            return p

def rabins_test():
    i = 1

    p = probable_prime(R, i)
    print "--"*78
    i += 1
    q = probable_prime(S, i)
    print "--"*78
    print "\n"

    base = (2,3,5,7)

    for k in base:
        a = gmpy2.powmod(k, p-1, p)
        b = gmpy2.powmod(k, q-1, q)

        if (a == 1): 
            print "p passes Miller-Rabin's test with base: ", k
        else:
            print "p has not passed Miller-Rabin's test with base " + str(k) + ", therefore p is not a prime number"

        if (b == 1):
            print "q passes Miller-Rabin's test with base: ", k
        else:
            print "q has not passed Miller-Rabin's test with base " + str(k) + ", therefore p is not a prime number"
    return p,q

def chinese_rm():
    p,q = rabins_test()

    n = gmpy2.mul(p, q)
    c = gmpy2.lcm(p-1, q-1)

    # decoding exponent
    d = gmpy2.powmod(3, -1, c)

    print "\n"
    print "--"*78
    print "n = ", n
    print "--"*78
    print "C(n) = ", c
    print "--"*78
    print "decoding exponent = ", d

    return n,d

def decryption(message):
    n,d = chinese_rm()

    e = gmpy2.powmod(message, 3, n)
    check_m = gmpy2.powmod(e, d, n)

    print "\n"
    print "--"*78
    print "e = ", n
    print "--"*78

    if (check_m == message):
        print "Message is verified!"
        print "--"*78
        print "M = ", message
        print "--"*78
        print "E^d mod n = ", check_m

    else:
        print "Message was not verified!"

    return

decryption(M)
