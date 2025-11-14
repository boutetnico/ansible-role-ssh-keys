import pytest

import os


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
        (
            "testuser",
            "users",
            "/home/testuser/.ssh/id_rsa_testuser",
            0o600,
            "PRIVATE KEY 2",
        ),
        (
            "testuser",
            "users",
            "/home/testuser/.ssh/id_rsa_testuser.pub",
            0o644,
            "PUBLIC KEY 2",
        ),
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


@pytest.mark.parametrize(
    "username,groupname,path,mode",
    [
        ("root", "root", "/root/.ssh", 0o700),
        ("testuser", "users", "/home/testuser/.ssh", 0o700),
    ],
)
def test_ssh_directory_ownership(host, username, groupname, path, mode):
    """Test that .ssh directories are owned by the correct user, not root."""
    d = host.file(path)
    assert d.exists
    assert d.is_directory
    assert d.user == username
    assert d.group == groupname
    assert d.mode == mode
