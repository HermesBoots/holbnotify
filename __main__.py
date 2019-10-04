import argparse
import getpass
import holbnotify
import holbnotify.config
import holbnotify.cron
import sys
import urllib.parse


def getArgs():
    description = 'Watch for checker to unlock on Holberton projects.'
    args = argparse.ArgumentParser(description=description)
    args.add_argument(
        'command',
        choices=('add', 'remove'),
        help='whether to start or stop polling a project checker'
    )
    args.add_argument(
        'project',
        metavar='PROJECT_URL',
        help='URL of project to poll'
    )
    args.add_argument(
        '-a', '--api-key',
        dest='apiKey',
        help='API key given on your Intranet tools page'
    )
    args.add_argument(
        '-e', '--email',
        dest='email',
        help='your Holberton e-mail address'
    )
    args.add_argument(
        '-p', '--password',
        dest='password',
        help='your Holberton intranet password (yes, the API needs this)'
    )
    args.add_argument(
        '-c', '--credential-file',
        dest='creds',
        help='path to INI file containing your Holberton credentials'
    )
    return args.parse_args()


def getCreds(args):
    if args.creds is not None:
        creds = holbnotify.config.config(args.creds)
    else:
        if args.apiKey is None:
            apiKey = getpass.getpass('Your API key: ')
        else:
            apiKey = args.apiKey
        if args.email is None:
            email = input('Your Holberton e-mail: ')
        else:
            email = args.email
        if args.password is None:
            password = getpass.getpass('Holberton password: ')
        else:
            password = args.password
        creds = holbnotify.Creds(apiKey, email, password)
    return creds


if __name__ == '__main__':
    args = getArgs()

    if args.command == 'remove':
        removed = holbnotify.cron.clearEvent(args.project)
        print('{} polling events removed'.format(removed))
        sys.exit(0)
    creds = getCreds(args)
    holbnotify.cron.addEvent(creds, args.project)
    print('You will be notified if the project checker is available.')
