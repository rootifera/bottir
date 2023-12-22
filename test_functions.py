import pytest

from packagecheck import is_required_package_installed


def test_is_apt_package_installed():
    assert is_required_package_installed('zip', 'debian')


def test_is_apt_package_not_installed():
    assert not is_required_package_installed('noname', 'debian')

@pytest.mark.xfail
def test_is_dnf_package_installed():
    assert is_required_package_installed('openssl', 'centos')


def test_is_dnf_package_not_installed():
    assert not is_required_package_installed('noname', 'centos')


def test_is_distro_unknown():
    assert not is_required_package_installed('openssl', 'caldera')
