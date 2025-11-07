import os
import datetime
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID

# Gerar chave privada da CA
ca_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Criar subject/issuer
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "BR"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "MiniPKI Lab"),
    x509.NameAttribute(NameOID.COMMON_NAME, "MiniPKI Root CA"),
])

# Datas (uso de UTC)
now = datetime.datetime.utcnow()
not_before = now - datetime.timedelta(minutes=1)
not_after = now + datetime.timedelta(days=365)

# Construir certificado da CA com extensões úteis
builder = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(ca_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(not_before)
    .not_valid_after(not_after)
    .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
    .add_extension(
        x509.KeyUsage(
            digital_signature=False,
            content_commitment=False,
            key_encipherment=False,
            data_encipherment=False,
            key_agreement=False,
            key_cert_sign=True,
            crl_sign=True,
            encipher_only=False,
            decipher_only=False,
        ),
        critical=True,
    )
    .add_extension(
        x509.SubjectKeyIdentifier.from_public_key(ca_key.public_key()), critical=False
    )
    .add_extension(
        x509.AuthorityKeyIdentifier.from_issuer_public_key(ca_key.public_key()), critical=False
    )
)

# Assinar o certificado da CA
ca_cert = builder.sign(private_key=ca_key, algorithm=hashes.SHA256())

print("✅ CA criada: MiniPKI Root CA")

# Salvar chave e certificado (PEM)
out_dir = os.path.dirname(__file__) or "."
with open(os.path.join(out_dir, "ca_key.pem"), "wb") as f:
    f.write(
        ca_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )

with open(os.path.join(out_dir, "ca_cert.pem"), "wb") as f:
    f.write(ca_cert.public_bytes(serialization.Encoding.PEM))

print(f"🔑 Chave da CA salva: {os.path.join(out_dir, 'ca_key.pem')}")
print(f"📜 Certificado da CA salvo: {os.path.join(out_dir, 'ca_cert.pem')}")