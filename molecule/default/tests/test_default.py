import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.fixture(scope='module')
def AnsibleRoleDefaults(host):
    return host.ansible('include_vars', '../../defaults/main.yml')['ansible_facts']


def test_hosts_file(host, AnsibleRoleDefaults):
    pg_data = AnsibleRoleDefaults['pg_data']
    
    # pg_data needs to be constructed including postgresql_version. How to do in in testinfra?
    f = host.file('/var/lib/pgsql/11/data')

    assert f.exists
    assert f.is_directory
    assert f.user == 'postgres'
    assert f.group == 'postgres'


def test_etcd_service(host, AnsibleRoleDefaults):

    postgresql_version = AnsibleRoleDefaults['postgresql_version']
    
    postgresql_service = host.service('postgresql-' + str(postgresql_version))

    assert postgresql_service.is_running
    assert postgresql_service.is_enabled
