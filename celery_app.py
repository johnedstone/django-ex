import shlex, subprocess
args = shlex.split('''celery worker -A picha.celery -B -Q default -n default@%h -l info''')
p = subprocess.Popen(args)
