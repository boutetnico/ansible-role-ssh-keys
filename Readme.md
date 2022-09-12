[![tests](https://github.com/boutetnico/ansible-role-ssh-keys/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-ssh-keys/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.ssh-keys-blue.svg)](https://galaxy.ansible.com/boutetnico/ssh-keys)


ansible-role-ssh-keys
=====================

This role installs SSH keys.

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)

Role Variables
--------------

| Variable                 | Required | Default                     | Choices   | Comments                     |
|--------------------------|----------|-----------------------------|-----------|------------------------------|
| ssh_keys_dependencies    | yes      | `[openssh-{client,server}]` | list      |                              |
| ssh_keys_authorized_keys | yes      | `[]`                        | list      |                              |
| ssh_keys_known_hosts     | yes      | `[]`                        | list      |                              |
| ssh_keys_private_keys    | yes      | `[]`                        | list      |                              |
| ssh_keys_public_keys     | yes      | `[]`                        | list      |                              |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-ssh-keys

          ssh_keys_authorized_keys:
            - user: root
              src: files/id_rsa.pub

          ssh_keys_known_hosts:
            - name: github.com
              type: ssh-rsa
              key: "AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ=="

          ssh_keys_private_keys:
            - owner: root
              group: root
              src: files/id_rsa_deploy
              dest: /root/.ssh/id_rsa_deploy

          ssh_keys_public_keys:
            - owner: root
              group: root
              src: files/id_rsa_deploy.pub
              dest: /root/.ssh/id_rsa_deploy.pub

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
