import pytest

import os


import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "username,groupname,path,key",
    [
        (
            "root",
            "root",
            "/root/.ssh/authorized_keys",
            "ssh-rsa PUBLIC KEY 1 dummy@molecule",
        ),
    ],
)
def test_authorized_keys_file(host, username, groupname, path, key):
    f = host.file(path)
    assert f.exists
    assert f.is_file
    assert f.user == username
    assert f.group == groupname
    assert f.contains(key)


@pytest.mark.parametrize(
    "username,groupname,path,name",
    [
        ("root", "root", "/root/.ssh/known_hosts", "github.com"),
    ],
)
def test_known_hosts_file(host, username, groupname, path, name):
    f = host.file(path)
    assert f.exists
    assert f.is_file
    assert f.user == username
    assert f.group == groupname
    assert f.contains(name)


@pytest.mark.parametrize(
    "username,groupname,path,mode,key",
    [
        ("root", "root", "/root/.ssh/id_rsa_deploy", 0o600, "PRIVATE KEY 2"),
        ("root", "root", "/root/.ssh/id_rsa_deploy.pub", 0o644, "PUBLIC KEY 2"),
    ],
)
def test_keys_file(host, username, groupname, path, mode, key):
    f = host.file(path)
    assert f.exists
    assert f.is_file
    assert f.user == username
    assert f.group == groupname
    assert f.mode == mode
    assert f.contains(key)
