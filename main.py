from packagecheck import is_apt_package_installed
from certgen import generate_certificate_with_dns
import distro
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-e', '--email')
parser.add_argument('-d', '--domain')
parser.add_argument('-i', '--aws-id')
parser.add_argument('-s', '--aws-secret')
args = parser.parse_args()

if not args.email or not args.domain or not args.aws_id or not args.aws_secret:
    raise SystemExit("Please provide an email and domain and an AWS credentials.")

REQUIRED_PACKAGES = ["python3-certbot-dns-route53", "certbot", "openssl"]

for package in REQUIRED_PACKAGES:
    if not is_apt_package_installed(package, distro.id()):
        print("Package '{}' is not installed".format(package))
        quit(1)

# set credentials

# set environment variables

# generate cert
# Specify your domain, email, DNS plugin, and plugin options

your_domain = 'hey.example.com'
your_email = 'your_aws_access_key_id'
your_dns_plugin = 'route53'
your_dns_plugin_options = [
    '--dns-route53',
    '--dns-route53-credentials', '/path/to/aws/credentials.ini',  # Replace with the actual path
]

# Call the function to generate the certificate using DNS-01 challenge
generate_certificate_with_dns(your_domain, your_email, your_dns_plugin, your_dns_plugin_options)

# convert to pk12

# save certificate
