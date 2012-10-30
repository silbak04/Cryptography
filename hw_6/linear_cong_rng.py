# Samir Silbak
# Cryptography 1
# Hw 6

import gmpy2

x = [0]*80
t = [0]*80
u = [0]*80

def linear_cong_rng():

    x[0] = 56687054115473550533
    x[1] = 71501923691929981066
    x[2] = 1162551557687152936
    x[3] = 88117163952857350660
    x[4] = 16754986973331962115

    t[0] = gmpy2.sub(x[1], x[0])
    t[1] = gmpy2.sub(x[2], x[1])
    t[2] = gmpy2.sub(x[3], x[2])
    t[3] = gmpy2.sub(x[4], x[3])

    u[0] = abs(gmpy2.mul(t[2], t[0]) - gmpy2.square(t[1]))
    u[1] = abs(gmpy2.mul(t[3], t[1]) - gmpy2.square(t[2]))

    # M'
    gcd = gmpy2.gcd(u[0], u[1])

    # true M = M'/6 since gcd(t[0], M) = 1
    #M = gmpy2.mpz(gmpy2.div(gcd, 6.0))
    M = gcd

    # x[2] = A * x[1] + B (mod M)
    # x[1] = A * x[0] + B (mod M)
    # ---------------------------
    # x[2] - x[1] = A (x[1] - x[0]) mod M

    # t[1] = A * t[0] mod M
    # A * t[0] = t[1] mod M

    # -x[0] * x[2] = -A * x[0] * x[1] - B * x[0] (mod M)
    #  x[1] * x[1] =  A * x[0] * x[1] + B * x[1] (mod M)
    # --------------------------------------------------
    # x[1]^2 - (x[0] * x[1]) = B (x[1] - x[0]) mod M

    # B * t[0] = (x[1]^2 - x[0]) mod M

    # used Diophantine equations to retrieve A and B
    # using M = M'/6
    #A = 184643116198852796934
    #B = 166536178911507583114
    # using M
    A = 12630192673789351314
    B = 71501923691929981066

    #check_a = gmpy2.f_mod(gmpy2.mul(A, t[0]), M)
    #x_diffe = gmpy2.sub(gmpy2.square(x[1]), gmpy2.mul(x[0], x[1]))

    #print "check_a = ", check_a
    #print "x_diffe = ", x_diffe

    print "t[0] = %i\nt[1] = %i\nt[2] = %i\nt[3] = %i\n\nu[0] = %i\nu[1] = %i\n\nM = gcd(u[0], u[1]) = %i\n" %(t[0], t[1], t[2], t[3], u[0], u[1], M)

    x[5]  = gmpy2.mpz(gmpy2.f_mod(gmpy2.add(gmpy2.mul(A,  x[4]), gmpy2.mpz(B)), gmpy2.mpz(M)))
    x[6]  = gmpy2.mpz(gmpy2.f_mod(gmpy2.add(gmpy2.mul(A,  x[5]), gmpy2.mpz(B)), gmpy2.mpz(M)))
    x[7]  = gmpy2.mpz(gmpy2.f_mod(gmpy2.add(gmpy2.mul(A,  x[6]), gmpy2.mpz(B)), gmpy2.mpz(M)))
    x[8]  = gmpy2.mpz(gmpy2.f_mod(gmpy2.add(gmpy2.mul(A,  x[7]), gmpy2.mpz(B)), gmpy2.mpz(M)))
    x[9]  = gmpy2.mpz(gmpy2.f_mod(gmpy2.add(gmpy2.mul(A,  x[8]), gmpy2.mpz(B)), gmpy2.mpz(M)))
    x[10] = gmpy2.mpz(gmpy2.f_mod(gmpy2.add(gmpy2.mul(A,  x[9]), gmpy2.mpz(B)), gmpy2.mpz(M)))
    x[11] = gmpy2.mpz(gmpy2.f_mod(gmpy2.add(gmpy2.mul(A, x[10]), gmpy2.mpz(B)), gmpy2.mpz(M)))

    #print "x[5] = ", x[5]
    #print "x[6] = ", x[6]
    #print "x[7] = ", x[7]
    #print "x[8] = ", x[8]
    #print "x[9] = ", x[9]
    print "x[10] = ", x[10]
    print "x[11] = ", x[11]

    print "A     = ", A
    print "B     = ", B

    return 

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
                print "\nk = %i \nsafe prime = %i\n" % (k, safe_p)
                return

def diophantine(a, b, c):
    q,r = gmpy2.f_divmod(a, b)

    if (r == 0):
        print "remainder = ", gmpy2.div(c, b)
        return([0, gmpy2.div(c, b)])

    else:
        sol = diophantine(b, r, c)
        x = sol[1]
        y = sol[0]

        print "x = ", x
        print "y = ", y

        return ([x, gmpy2.sub(y, gmpy2.mul(x, q))])

linear_cong_rng()
print "-"*80
safe_prime(150)
#print "-"*80
#diophantine(14814869576456430533,95034255219577602048,-70339372134242828130)
