import subprocess
import sys
def dump(url):
    try:
        return subprocess.Popen(['pgp_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print e
        sys.exit(1)
