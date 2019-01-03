import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_kubectl_is_installed(host):
    kubectl = host.package('kubectl')
    assert kubectl.is_installed
