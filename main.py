import distro
import argparse
import configparser
from packagecheck import is_apt_package_installed
from certgen import generate_certificate_with_dns


config = configparser.ConfigParser()
config.read('aws-credentials.ini', encoding='utf')
parser = argparse.ArgumentParser()

parser.add_argument('-e', '--email')
parser.add_argument('-d', '--domain')
args = parser.parse_args()

if not args.email or not args.domain:
    raise SystemExit("Please provide an email and domain and AWS credentials.")

REQUIRED_PACKAGES = ["python3-certbot-dns-route53", "certbot", "openssl"]

# Check packages
for package in REQUIRED_PACKAGES:
    if not is_apt_package_installed(package, distro.id()):
        print("Package '{}' is not installed".format(package))
        quit(1)

# generate cert
# Call the function to generate the certificate using DNS-01 challenge
generate_certificate_with_dns(args.domain, args.email, config['aws']['id'], config['aws']['key'])

