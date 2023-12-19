import subprocess


def is_apt_package_installed(package_name, distro):
    try:
        # Run dpkg command to list installed packages
        if distro == 'debian' or 'ubuntu':
            result = subprocess.run(['dpkg', '--get-selections'], stdout=subprocess.PIPE, text=True, check=True)
            installed_packages = result.stdout.split('\n')
        elif distro == 'redhat' or distro == 'centos' or distro == 'fedora':
            result = subprocess.run(['dnf', 'list', 'installed'], stdout=subprocess.PIPE, text=True, check=True)
            installed_packages = result.stdout.split('\n')
        else:
            return 'Unknown Distro'

        # Check if the specified package is in the list
        for package in installed_packages:
            if package.startswith(package_name):
                return True

        # Package not found
        return False

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
