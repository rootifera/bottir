import subprocess
import os.path


def is_required_package_installed(package_name, distro):
    try:
        # Run dpkg command to list installed packages
        if os.path.isfile('/usr/bin/dpkg'):
            if distro == 'debian' or distro == 'ubuntu':
                result = subprocess.run(['dpkg', '--get-selections'], stdout=subprocess.PIPE, text=True, check=True)
                installed_packages = result.stdout.split('\n')
                print(installed_packages[0])
        # Run dnf command to list installed packages
        elif os.path.isfile('/usr/bin/dnf'):
            if distro == 'redhat' or distro == 'centos' or distro == 'fedora':
                result = subprocess.run(['dnf', 'list', 'installed'], stdout=subprocess.PIPE, text=True, check=True)
                installed_packages = result.stdout.split('\n')
        else:
            print('else')
            return False

        # Check if the specified package is in the list
        for package in installed_packages:
            print("pack check")
            if package.startswith(package_name):
                print('package found')
                return True

        # Package not found
        return False

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
