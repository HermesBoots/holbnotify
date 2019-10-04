import holbnotify
import os.path
import subprocess


path = os.path.join(os.path.split(os.path.abspath(__file__))[0], '..')

def addEvent(creds: holbnotify.Creds, project: str):
    """Tell cron to start querying the project every 30 minutes.

    Args:
        creds: the credentials needed to use the Holberton API
        project: URL of the project to check

    """

    crontab = subprocess.check_output(('crontab', '-l'), timeout=3)
    crontab = crontab.splitlines()
    schedule = b'0,30 * * * *'
    command = 'PYTHONPATH={} python3 -m holbnotify.check {} {} {} {}'.format(
        path, project, creds.api_key, creds.email, creds.password
    ).encode('ASCII')
    crontab.append(schedule + b' ' + command)
    cron = subprocess.Popen(('crontab', '-'), stdin=subprocess.PIPE)
    cron.communicate(b'\n'.join(crontab) + b'\n', 3)
    cron.wait(3)

def clearEvent(project: str) -> int:
    """Remove a recurring event from the crontab.

    Args:
        project: the project path to stop querying

    """

    crontab = subprocess.check_output(('crontab', '-l'), timeout=3)
    crontab = crontab.splitlines()
    schedule = b'0,30 * * * *'
    command = 'PYTHONPATH={} python3 -m holbnotify.check {}'.format(
        path, project
    ).encode('ASCII')
    removed = 0
    for index, line in enumerate(crontab):
        if line.startswith(schedule + b' ' + command + b' '):
            del crontab[index]
            removed += 1
    cron = subprocess.Popen(('crontab', '-'), stdin=subprocess.PIPE)
    cron.communicate(b'\n'.join(crontab) + b'\n', 3)
    cron.wait(3)
    return removed
