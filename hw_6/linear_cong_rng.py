import gmpy2

x_0 = 56687054115473550533
x_1 = 71501923691929981066
x_2 = 1162551557687152936
x_3 = 8117163952857350660
x_4 = 16754986973331962115

def linear_cong_rng():
    x = (x_0, x_1, x_2, x_3, x_4)

    t_0 = (x[1] - x[0])
    t_1 = (x[2] - x[1])
    t_2 = (x[3] - x[2])
    t_3 = (x[4] - x[3])

    u_0 = abs(gmpy2.mul(t_2, t_0) - gmpy2.square(t_1))
    u_1 = abs(gmpy2.mul(t_3, t_1) - gmpy2.square(t_2))

    gcd = gmpy2.gcd(u_0, u_1)

    print "t[0] = %i\nt[1] = %i\nt[2] = %i\nt[3] = %i\n\nu[0] = %i\nu[1] = %i\n\ngcd(u[0], u[1]) = %i" %(t_0, t_1, t_2, t_3, u_0, u_1, gcd)

linear_cong_rng()
