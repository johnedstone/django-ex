import shlex, subprocess, sys
from subprocess import PIPE
args = shlex.split(''' celery worker -A picha.celery -B -Q default -n default@%h -l info ''')
# stdout, stderr = subprocess.Popen(args, stdout=PIPE).communicate()
p = subprocess.Popen(args)
