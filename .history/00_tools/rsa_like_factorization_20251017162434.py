import sympy as sp
import time

p = sp.nextprime(10**6)
q = sp.nextprime(10**6 + 100)
n = p * q
start = time.time()
fatores = sp.factorint(n)
end = time.time()
print("Fatores de n:", fatores)
print("Tempo:", end - start)