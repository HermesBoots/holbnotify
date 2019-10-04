# HolbNotify

Get notified when the Holberton checker becomes available.

## Description

Uses the Holberton School checker API to send an email to a student once a project is available for correction. This program will alert you once a project has become available to be checked. The email will also inform you of
what checks have been missed

## Usage

`python3 -m holbnotify [-h] [-a APIKEY] [-e EMAIL] [-p PASSWORD] [-c CREDS]
                   {add || remove} PROJECT_URL`

### Positional Arguments

| Argument | Description |
| - | - |
| `{add || remove}`| Starts or stops polling a project checker |
| `PROJECT_URL` | URL of a project to poll |

### Optional Arguments

| Argument | Description |
| - | - |
| `-h, --help` | Help |
| `-a APIKEY, --api-key APIKEY` | API key from Intranet tools page |
| `-e EMAIL, --email EMAIL` | Holberton School email address |
| `-p PASSWORD, --password PASSWORD` | Holberton School Intranet password
| `-c CREDS, --credential-file CREDS` | Path to ini config file |

### Configuration File

A configuration file, `init.ini`, is included for ease of access. This file allows you to store your Intranet email address, password, and api key in one place.

**THIS FILE IS STORED IN PLAIN TEXT** Make sure this file is only readable by you use:

```bash
sudo chmod 600 holbnotify/init.ini
```

## Dependencies

This application uses Cron to schedule when the application checks the checker

If Cron is not installed on your system:

### Ubuntu

```bash
sudo apt-get install cron
```

## Authors

* Sam Hermes ([https://github.com/HermesBoots](https://github.com/HermesBoots))
* Rory Fahy ([https://github.com/HermesBoots](https://github.com/rmf10003))
* Mark Hedgeland ([https://github.com/HermesBoots](https://github.com/zmbslyr))
