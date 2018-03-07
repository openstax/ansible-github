ansible-github
=========

Requirements
------------

Role Variables
--------------
| Name               | Default Value |Description                                                 |
|--------------------|---------------|------------------------------------------------------------|
|`gh_copy_keys`      | false         | copy and use ssh private to clone repository               |
|`gh_repo`           | *required*    | the git URL or ssh url of the repository to clone          |
|`gh_dest_dir`       | *required*    | the destination directory in which to clone the repository |
|`gh_dest_dir_user`  | *required*    | the user that should own the destination directory         |
|`gh_dest_dir_group` | *required*    | the group that should own the destination directory        |
|`gh_priv_key_path`  |               | the local file path of the ssh key to copied               |

Dependencies
------------

N/A

Example Playbook
----------------

Example Playbook
----------------

    - hosts: servers
      hosts: all
        vars:
            gh_repo: https://github.com/openstax/tutor-js.git
            gh_dest_dir: /var/www
            gh_dest_dir_user: www-data
            gh_dest_dir_group: www-data
          roles:
            - role: ansible-github

License
-------

GPLv3

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

To run the role

```bash
molecule test
```
