Introduction

This repository contains a collection of Python scripts, shell scripts, and C scripts. Each script serves a specific purpose and adheres to the guidelines specified below.

## Python Scripts

- All Python scripts are written in Python 3.8.5 and will be interpreted on Ubuntu 20.04 LTS.
- Each Python script starts with `#!/usr/bin/python3` as the first line.
- The code in the Python scripts follows the PEP 8 style guidelines and is checked using `pycodestyle` version 2.8.*.
- All Python scripts are executable.
- Examples of Python scripts can be found in the repository.

## Shell Scripts

- All shell scripts are tested on Ubuntu 20.04 LTS.
- Each shell script is exactly two lines long (excluding the shebang and the newline).
- Each shell script starts with `#!/bin/bash` as the first line.
- All shell scripts are executable.
- Examples of shell scripts can be found in the repository.

## C Scripts

- All C scripts are compiled on Ubuntu 20.04 LTS using `gcc` with the options `-Wall -Werror -Wextra -pedantic -std=gnu89`.
- Each C script adheres to the Betty style guidelines and is checked using `betty-style.pl` and `betty-doc.pl`.
- Global variables are not used in any of the C scripts.
- Each C script has no more than 5 functions.
- The prototypes of all functions are included in the `lists.h` header file.
- All header files are include guarded.
- Examples of C scripts and header files can be found in the repository.


