# SysAx
AXIA database ToolKit
![Generic badge](https://img.shields.io/github/pipenv/locked/python-version/cristian1604/SysAx) ![Generic badge](https://img.shields.io/badge/made%20with-Python-blue.svg) ![Generic badge](https://img.shields.io/badge/status-TEST-red.svg)

This is a *wrapper-script* to perform a database backup and restoring functions using **Postgres** dump utilities.

(If you want a script to perform several databases from a DB engine at the same time, take a look [backupDatabase])

**This project currently runs on Linux.**


### Changelog

  - Improve documentation
  - Tested on multiple MySQL and Postgres databases (one script to call each DB engine)
  - Comment code


### Requirements

- Python version >= 3
- The provided Postgres binaries correspond to the Pg 11.2
- Notice: If you run this script on the database server, I recommend strongly use the provided binaries by the database engine.


### How to set parameters

Parameters:

On `settings.dat` you can add a list of parameters:

    [ALIAS]                            # Alias for the connection
    database = DATABASE                # Database name
    host = HOST_IP                     # URL or IP to the database server
    port = HOST_PORT                   # Default: 5432
    username = USERNAME
    password = USER_PASSWD             


### To Do:

This is the first commit. It's not functional yet.


### Why this script?

I was motivated by the need to perform a fast backup of several production databases on Postgres and replay it on a develop server.


About
----

Written by Cristian Bottazzi


[//]: #
   [backupDatabase]: <https://github.com/cristian1604/backupDatabase>
