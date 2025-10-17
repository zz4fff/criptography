from sympy import factorint, nextprime
import time

p = nextprime(10**6)
q = nextprime(10**6 + 100)
n = p * q
start = time.time()
fatores = factorint(n)
end = time.time()
print("Fatores de n:", fatores)
print("Tempo:", end - start)