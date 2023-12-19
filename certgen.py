import subprocess


def generate_certificate_with_dns(domain, email, is_test=False):
    try:
        if is_test:
            # Run Certbot command to obtain a certificate using DNS-01 challenge
            subprocess.run([
                'certbot', 'certonly',
                '--server', 'https://acme-staging-v02.api.letsencrypt.org/directory',
                '--test-cert',
                '--non-interactive',
                '--dns-route53',
                '--key-type', 'rsa',
                '--agree-tos',
                '--work-dir', './certbot',
                '--config-dir', './certbot/staging/config',
                '--logs-dir', './certbot/staging/logs',
                '-d', domain,
                '-m', email,
            ], check=True)

            print(f"A Staging Certificate for {domain} successfully obtained using DNS-01 challenge.")
        else:
            subprocess.run([
                'certbot', 'certonly',
                '--non-interactive',
                '--dns-route53',
                '--key-type', 'rsa',
                '--agree-tos',
                '--work-dir', './certbot',
                '--config-dir', './certbot/live/config',
                '--logs-dir', './certbot/live/logs',
                '-d', domain,
                '-m', email,
            ], check=True)

            print(f"Certificate for {domain} successfully obtained using DNS-01 challenge.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
