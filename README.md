# SysAx
AXIA database ToolKit

![Generic badge](https://img.shields.io/badge/made%20with-Python-blue.svg) ![Generic badge](https://img.shields.io/badge/status-TEST-red.svg)

This is a *wrapper-script* to perform a database backup and restoring functions using **Postgres** dump utilities, even between different servers.
Perform a fast database backup or restoration in a few steps. The only restriction is: __all the servers must have the same postgres version.__

(If you want a script to perform several databases from a DB engine at the same time, take a look [backupDatabase])

**This project runs on Linux.**


### Requirements

- Python version >= 3
- [postgresql-client]. (required postgres binaries to use this script)

### Setting databases

First of all, rename `settings.dat.dist` to `settings.dat`

On `settings.dat` you can add a list of parameters:

    [ALIAS]                            # Alias to be used on the script
    database = DATABASE                # Database name
    host = HOST_IP                     # URL or IP to the database server
    port = HOST_PORT                   # Default: 5432
    username = USERNAME
    password = USER_PASSWD             

### Run the script!

Execute it with a simple command: `./main.py` and follow the menu

### Why this script?

I was motivated by the need to perform a fast backup of several production databases running on Postgres, and replay it on a develop server in a few steps.


About
----

Written by Cristian Bottazzi


[//]: #
   [backupDatabase]: <https://github.com/cristian1604/backupDatabase>
   [postgresql-client]: <https://www.postgresql.org/download/linux/ubuntu/>
