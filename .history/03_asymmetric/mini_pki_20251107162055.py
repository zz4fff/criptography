from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
import datetime

# 1. Gerar chave privada da CA
ca_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# 2. Criar certificado autoassinado da CA
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "BR"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "MiniPKI Lab"),
    x509.NameAttribute(NameOID.COMMON_NAME, "MiniPKI Root CA"),
])

ca_cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    ca_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    datetime.datetime.utcnow() + datetime.timedelta(days=365)
).add_extension(
    x509.BasicConstraints(ca=True, path_length=0), critical=True,
).sign(ca_key, hashes.SHA256())

print("✅ CA criada: MiniPKI Root CA")

# 3. Salvar CA
with open("ca_key.pem", "wb") as f:
    f.write(ca_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("ca_cert.pem", "wb") as f:
    f.write(ca_cert.public_bytes(serialization.Encoding.PEM))

print("🔑 Chave da CA salva: ca_key.pem")
print("📜 Certificado da CA salvo: ca_cert.pem")