import subprocess
import time
import sys

# no subsub process coverage
#sub = subprocess.Popen(['python', './thing/subsub.py'])
sub = subprocess.Popen(['coverage', 'run', '--debug', 'dataio', '-p', './thing/subsub.py'])
if False:
    ret = sub.wait()
    print "subsub returned", ret
    sys.exit(ret)
else:
    time.sleep(2)
    # no coverage if we kill it
    #sub.kill()
    # :( also not if we terminate?!
    sub.terminate()
    if False:
        #sub.send_signal(3) # SIGQUIT
        print "sending HUP"
        sub.send_signal(1) # SIGHUP
        time.sleep(1)
        print "sending QUIT"
        sub.send_signal(3) # SIGQUIT
        #sub.wait() # does work
print "done sub"
