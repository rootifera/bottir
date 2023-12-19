import subprocess


def generate_certificate_with_dns(domain, email, aws_id, aws_key):
    try:
        # Run Certbot command to obtain a certificate using DNS-01 challenge
        subprocess.run([
            'certbot', 'certonly',
            '--non-interactive',
            '--dns-route53',
            '--key-type', 'rsa',
            '--agree-tos',
            '--work-dir', './certbot',
            '--config-dir', './certbot/config',
            '--logs-dir', './certbot/logs',
            '-d', domain,
            '-m', email,
        ], check=True)

        print(f"Certificate for {domain} successfully obtained using DNS-01 challenge.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
