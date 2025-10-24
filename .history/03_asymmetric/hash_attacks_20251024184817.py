import hashlib
import random
import string
import time

def short_hash(text):
    # Simula hash curto (primeiros 8 chars de SHA-256)
    return hashlib.sha256(text.encode()).hexdigest()[:8]

hashes = set()
attempts = 0
max_attempts = 100000
start = time.time()

while attempts < max_attempts:
    text = ''.join(random.choices(string.ascii_letters, k=10))
    h = short_hash(text)
    if h in hashes:
        print("Colisão encontrada após", attempts, "tentativas!")
        print("Hash:", h, "Texto:", text)
        break
    hashes.add(h)
    attempts += 1
if attempts == max_attempts:
    print("Nenhuma colisão em", max_attempts, "tentativas.")

end = time.time()
print("Tempo:", end - start)