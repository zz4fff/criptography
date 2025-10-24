    import hashlib
    import time

    def compute_md5(text):
        return hashlib.md5(text.encode()).hexdigest()

    # Testar integridade
    start = time.time()
    texto1 = "Seguranca da Informacao"
    texto2 = "Seguranca da Informacao!"
    hash1 = compute_md5(texto1)
    hash2 = compute_md5(texto2)
    print(f"Hash de '{texto1}': {hash1}")
    print(f"Hash de '{texto2}': {hash2}")
    print("Integridade:", hash1 == hash2)

    # Simular colisão (exemplo com entradas conhecidas vulneráveis)
    collision1 = b"d31dd02c5e6ee2e615e6225333477c"  # Exemplo de colisão MD5
    collision2 = b"d31dd02c5e6ee2e615e6225333477d"
    print("Colisão MD5:")
    print(f"Hash colisão 1: {hashlib.md5(collision1).hexdigest()}")
    print(f"Hash colisão 2: {hashlib.md5(collision2).hexdigest()}")
    end = time.time()
    print("Tempo:", end - start, "segundos")