# Ansible role kubectl

[![Build Status](https://travis-ci.org/tottoto/ansible-role-kubectl.svg?branch=master)](https://travis-ci.org/tottoto/ansible-role-kubectl)

This is an ansible role to install kubectl.

## Installation

```sh
$ ansible-galaxy install tottoto.kubectl
```

## Example

```yaml
- name: Example playbook to use tottoto.kubectl
  hosts: all
  become: yes
  roles:
    - tottoto.kubectl
```

## License

See [LICENSE](./LICENSE).
