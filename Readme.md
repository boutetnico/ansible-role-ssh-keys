[![tests](https://github.com/boutetnico/ansible-role-ssh-keys/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-ssh-keys/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.ssh_keys-blue.svg)](https://galaxy.ansible.com/boutetnico/ssh_keys)


ansible-role-ssh-keys
=====================

This role installs SSH keys.

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
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
              key: "AAAAB3NzaC1yc2EAAAADAQABAAABgQCj7ndNxQowgcQnjshcLrqPEiiphnt+VTTvDP6mHBL9j1aNUkY4Ue1gvwnGLVlOhGeYrnZaMgRK6+PKCUXaDbC7qtbW8gIkhL7aGCsOr/C56SJMy/BCZfxd1nWzAOxSDPgVsmerOBYfNqltV9/hWCqBywINIR+5dIg6JTJ72pcEpEjcYgXkE2YEFXV1JHnsKgbLWNlhScqb2UmyRkQyytRLtL+38TGxkxCflmO+5Z8CSSNY7GidjMIZ7Q4zMjA2n1nGrlTDkzwDCsw+wqFPGQA179cnfGWOWRVruj16z6XyvxvjJwbz0wQZ75XK5tKSb7FNyeIEs4TT4jk+S4dhPeAUC5y+bDYirYgM4GC7uEnztnZyaVWQ7B381AK4Qdrwt51ZqExKbQpTUNn+EjqoTwvqNj4kqx5QUCI0ThS/YkOxJCXmPUWZbhjpCg56i+2aB6CmK2JGhn57K5mj0MNdBXA4/WnwH6XoPWJzK5Nyu2zB3nAZp+S5hpQs+p1vN1/wsjk="

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
