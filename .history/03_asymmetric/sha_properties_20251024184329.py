import hashlib
import random
import string
import time

def generate_random_string(size):
    return ''.join(random.choices(string.ascii_letters, k=size))

# Testar sensibilidade e colisão
start = time.time()
text1 = generate_random_string(20)
text2 = text1[:-1] + 'X'  # Pequena alteração
text3 = generate_random_string(20)  # Totalmente diferente
hash1 = hashlib.sha256(text1.encode()).hexdigest()
hash2 = hashlib.sha256(text2.encode()).hexdigest()
hash3 = hashlib.sha256(text3.encode()).hexdigest()
print("Text1:", text1, "\nHash1:", hash1)
print("Text2:", text2, "\nHash2:", hash2)
print("Text3:", text3, "\nHash3:", hash3)
print("Hash1 == Hash2?", hash1 == hash2)
print("Hash1 == Hash3?", hash1 == hash3)
end = time.time()
print("Tempo:", end - start)