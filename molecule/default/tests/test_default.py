import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.fixture(scope='module')
def AnsibleRoleDefaults(host):
    return host.ansible('include_vars', '../../defaults/main.yml')['ansible_facts']


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_etcd_service(host, AnsibleRoleDefaults):

    postgresql_version = AnsibleRoleDefaults['postgresql_version']
    
    postgresql_service = host.service('postgresql-' + str(postgresql_version))

    assert postgresql_service.is_running
    assert postgresql_service.is_enabled
