import sys
try:
    from sympy import factorint, nextprime
except ModuleNotFoundError:
    print("Módulo 'sympy' não encontrado. Instale com:\n  python -m pip install sympy\nou\n  py -3 -m pip install sympy")
    sys.exit(1)

import time

p = nextprime(10**6)
q = nextprime(10**6 + 100)
n = p * q
start = time.time()
fatores = factorint(n)
end = time.time()
print("Fatores de n:", fatores)
print("Tempo:", end - start)