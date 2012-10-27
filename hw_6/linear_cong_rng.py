# Samir Silbak
# Cryptography 1
# Hw 6

import gmpy2

x_0 = 56687054115473550533
x_1 = 71501923691929981066
x_2 = 1162551557687152936
x_3 = 88117163952857350660
x_4 = 16754986973331962115

def linear_cong_rng():
    x = (x_0, x_1, x_2, x_3, x_4)

    t_0 = gmpy2.sub(x[1], x[0])
    t_1 = gmpy2.sub(x[2], x[1])
    t_2 = gmpy2.sub(x[3], x[2])
    t_3 = gmpy2.sub(x[4], x[3])

    u_0 = abs(gmpy2.mul(t_2, t_0) - gmpy2.square(t_1))
    u_1 = abs(gmpy2.mul(t_3, t_1) - gmpy2.square(t_2))

    gcd = gmpy2.gcd(u_0, u_1)

    print "t[0] = %i\nt[1] = %i\nt[2] = %i\nt[3] = %i\n\nu[0] = %i\nu[1] = %i\n\ngcd(u[0], u[1]) = %i\n" %(t_0, t_1, t_2, t_3, u_0, u_1, gcd)

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
                print "k = %i \nsafe prime = %i\n" % (k, safe_p)
                return

linear_cong_rng()
#safe_prime(150)
