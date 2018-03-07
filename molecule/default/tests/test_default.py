import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_git_is_installed(host):
    pkg = host.package('git')
    assert pkg.is_installed


def test_repo_was_copied(host):
    repo = host.file('/var/www/package.json')
    print(repo)
    assert repo.contains('openstax-frontend')
    assert repo.user == 'www-data'
    assert repo.group == 'www-data'
