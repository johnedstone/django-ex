import shlex, subprocess
from subprocess import PIPE

args = shlex.split('''/usr/bin/bash run_celery.sh''')
stdout, stderr = subprocess.Popen(args, stdout=PIPE).communicate()
