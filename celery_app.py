import shlex, subprocess, sys
from subprocess import PIPE
args = shlex.split('''/usr/bin/bash toss.sh''')
stdout, stderr = subprocess.Popen(args, stdout=PIPE).communicate()
