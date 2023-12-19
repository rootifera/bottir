import subprocess


def generate_certificate_with_dns(domain, email, dns_plugin, dns_plugin_options):
    try:
        # Run Certbot command to obtain a certificate using DNS-01 challenge
        subprocess.run([
            'certbot', 'certonly',
            '--server', 'https://acme-v02.api.letsencrypt.org/directory',  # Use Let's Encrypt v2 API
            '--non-interactive',
            '--preferred-challenges', 'dns',
            '--email', email,
            '--agree-tos',
            '-d', domain,
            f'--dns-{dns_plugin}',
            *dns_plugin_options,
        ], check=True)

        print(f"Certificate for {domain} successfully obtained using DNS-01 challenge.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
