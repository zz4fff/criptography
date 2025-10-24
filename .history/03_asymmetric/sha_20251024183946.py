import hashlib
import time

def compute_hashes(text):
    return {
        "SHA-1": hashlib.sha1(text.encode()).hexdigest(),
        "SHA-256": hashlib.sha256(text.encode()).hexdigest(),
        "SHA-3-256": hashlib.sha3_256(text.encode()).hexdigest()
    }

# Testar sensibilidade
start = time.time()
texto = "Laboratorio de Seguranca"
texto_alt = "laboratorio de seguranca"
hashes1 = compute_hashes(texto)
hashes2 = compute_hashes(texto_alt)
for algo, h in hashes1.items():
    print(f"{algo} de '{texto}': {h}")
    print(f"{algo} de '{texto_alt}': {hashes2[algo]}")
    print("Iguais?", h == hashes2[algo])
end = time.time()
print("Tempo:", end - start, "segundos")