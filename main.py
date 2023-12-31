import distro
import argparse
import os
from packagecheck import is_required_package_installed
from certgen import generate_certificate_with_dns
from pemtopfx import pem_to_pfx, validate_pfx

parser = argparse.ArgumentParser(description='Simple tool to generate certificates')

parser.add_argument('-e', '--email')
parser.add_argument('-d', '--domain')
parser.add_argument('-k', '--aws-key')
parser.add_argument('-s', '--aws-secret')
parser.add_argument('-t', '--test', action=argparse.BooleanOptionalAction)
parser.add_argument('-p', '--pfx', action=argparse.BooleanOptionalAction)
parser.add_argument('-v', '--validate-pfx', action=argparse.BooleanOptionalAction)
args = parser.parse_args()

if args.email is None or args.domain is None or args.aws_key is None or args.aws_secret is None:
    raise SystemExit(
        "Usage: bottir -e mail@domain.com -d sub.domain.com -k awskey -s aws-secret \
        (optional: --test --pfx --validate-pfx)")

os.environ["AWS_ACCESS_KEY_ID"] = args.aws_key
os.environ["AWS_SECRET_ACCESS_KEY"] = args.aws_secret

if not args.email or not args.domain:
    raise SystemExit("Please provide an email and domain and AWS credentials.")

REQUIRED_PACKAGES = ["python3-certbot-dns-route53", "certbot", "openssl"]

# Check packages
for package in REQUIRED_PACKAGES:
    if not is_required_package_installed(package, distro.id()):
        print("Package '{}' is not installed".format(package))
        quit(1)

# Call the function to generate the certificate using DNS-01 challenge
generate_certificate_with_dns(args.domain, args.email, args.test)

if args.pfx:
    if args.test:
        cert_path = './certbot/staging/config/live/{}/fullchain.pem'.format(args.domain)
        key_path = './certbot/staging/config/live/{}/privkey.pem'.format(args.domain)
        save_pfx = './certbot/staging/config/live/{}/{}.pfx'.format(args.domain, args.domain)
        pem_to_pfx(cert_path, key_path, save_pfx)
        print("PFX Generated at {}".format(save_pfx))
        if args.validate_pfx:
            validate_pfx(save_pfx)
    else:
        cert_path = './certbot/live/config/live/{}/fullchain.pem'.format(args.domain)
        key_path = './certbot/live/config/live/{}/privkey.pem'.format(args.domain)
        save_pfx = './certbot/live/config/live/{}/{}.pfx'.format(args.domain, args.domain)
        pem_to_pfx(cert_path, key_path, save_pfx)
        print("PFX Generated at {}".format(save_pfx))
        if args.validate_pfx:
            validate_pfx(save_pfx)
