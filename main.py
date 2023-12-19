import distro
import argparse
import os
from packagecheck import is_apt_package_installed
from certgen import generate_certificate_with_dns

parser = argparse.ArgumentParser()

parser.add_argument('-e', '--email')
parser.add_argument('-d', '--domain')
parser.add_argument('-k', '--aws-key')
parser.add_argument('-s', '--aws-secret')
parser.add_argument('-t', '--test', action=argparse.BooleanOptionalAction)
args = parser.parse_args()

print(args.test)
os.environ["AWS_ACCESS_KEY_ID"] = args.aws_key
os.environ["AWS_SECRET_ACCESS_KEY"] = args.aws_secret

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
generate_certificate_with_dns(args.domain, args.email, args.test)

