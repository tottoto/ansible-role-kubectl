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

## Development

### Requirements

- [Docker](https://www.docker.com/)
- Python (The version is declared in [Pipfile](./Pipfile))
- [Pipenv](https://github.com/pypa/pipenv)

### Tests

Create python virtualenv.

```sh
$ pipenv install -d
```

Run the test. The target distribution can be specified by environment variable `MOLECULE_DOCKER_IMAGE`. The default value is `ubuntu:bionic`.

```sh
$ MOLECULE_DOCKER_IMAGE=ubuntu:bionic pipenv run molecule test
```

## License

See [LICENSE](./LICENSE).
