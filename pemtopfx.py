import OpenSSL
from digital_certificate.cert import Certificate


def pem_to_pfx(cert_path, key_path, pfx_path):
    # Read the certificate in PEM format
    with open(cert_path, 'rb') as cert_file:
        cert_data = cert_file.read()

    # Read the private key in PEM format
    with open(key_path, 'rb') as key_file:
        key_data = key_file.read()

    key = OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM, key_data)
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert_data)
    pkcs = OpenSSL.crypto.PKCS12()
    pkcs.set_privatekey(key)
    pkcs.set_certificate(cert)

    with open(pfx_path, 'wb') as file:
        file.write(pkcs.export())


def validate_pfx(certificate_path):
    _cert = Certificate(
        pfx_file=certificate_path,
        password=b""
    )

    _cert.read_pfx_file()
    print("Serial Number: ", format(_cert.serial_number()))
    print("Valid From: ", format(_cert.not_valid_before()))
    print("Valid Until: ", format(_cert.not_valid_after()))
    print("Subject: ", format(_cert.subject()))
    print("Common Name: ", format(_cert.common_name()))
    print("Issuer: ", format(_cert.issuer()))
