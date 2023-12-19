import OpenSSL


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
