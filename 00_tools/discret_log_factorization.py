from sympy.ntheory import discrete_log

p = 23
g = 5
A = pow(g, 4, p)  # a=4
log = discrete_log(p, A, g)
print("Log discreto:", log)