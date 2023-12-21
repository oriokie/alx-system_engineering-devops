# Shell Loops, Conditions,
![](https://phoenixnap.com/kb/wp-content/uploads/2021/12/individual.sh-for-loop-script.png)

## Use this command to generate RSA key `ssh-keygen -t rsa`

## Learning objectives

- How to create SSH keys
- What is the advantage of using `#!/usr/bin/env` bash over `#!/bin/bash`
- How to use `while`, `until` and `for` loops
- How to use `if`, `else`, `elif` and case condition statements
- How to use the `cut` command
- What are files and other comparison operators, and how to use them

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on `Ubuntu 20.04 LTS`
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- You are not allowed to use `awk`
- Your Bash script must pass `Shellcheck` (version 0.7.0) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script doing

## Concepts

- `env`
- `cut`
- `for`
- `while`
- `until`
- `if

## Files
| Filename | Description |
| -------- | ----------- |
| `0-RSA_public_key.pub` | Files that stores a RSA public key to access servers via SSH.|
| `1-for_holberton_school` | Displays `Best School` 10 times with a `for` loop.|
| `2-while_holberton_school` | Displays `Best School` 10 times with a `while` loop.|
| `3-until_holberton_school` | Displays `Best School` 10 times with an `until` loop.|
| `4-if_9_say_hi` | Displays `Best School` 10 times and displays `Hi` for the 9th iteration.|
| `5-4_bad_luck_8_is_your_chance` | Loops from 1 to 10 and displays `Best School`, except for t4th and 8th iteration which displays `bad luck` and `good luck`, respectively.|
| `6-superstitious_numbers` | Displays numbers from 1 to 20 and displays `bad luck from China`, `bad luck from Japan` and `bad luck from Italy` for the 4th , 9th and 17th iteration respectively.|
| `7-clock` | Displays the time for 12 hours and 59 minutes.|
| `8-for_ls` | Displays the content of the current directory in a list format.|
| `9-to_file_or_not_to_file` | Gives informaton about the `Bestschool` file.|
| `10-fizzbuzz` | Displays the `fizzbuzz` sequence.|
| `100-read_and_cut` | Displays the content of the file `/etc/passwd`|
| `101-tell_the_story_of_passwd` | Displays the content of the file `/etc/passwd` with a specific message.|
| `102-lets_parse_apache_logs` | Displays the visitor IP along with the HTTP status code from an Apache log file.|
| `103-dig_the-data` | Groups visitors by IP and HTTP status code and displays the occurences, from the greteast to the lowest number.|`
