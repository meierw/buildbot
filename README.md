buildbot
========

Ansible role which installs Buildbot `>= 2.0.0` master and/or slave.

Requirements
------------

* `python3.5+` with `dev` and `pip` tools

> `python 2` support was dropped with Buildbot 2. [Source](http://docs.buildbot.net/2.0.0/manual/installation/requirements.html?highlight=requirement)

Role Variables
--------------

```yaml
pip_executable: pip3
```
`pip` executable to use for Buildbot installation.

-------
```yaml
assert_python3_dependencies: true
```
Assert presence of correct `python 3` dependencies for Buildbot installation.


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - meierw.buildbot
```

License
-------

MIT

Author Information
------------------

* _Author:_ [Walter Meier](mailto:valters.meirens@gmail.com)
