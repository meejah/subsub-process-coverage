import time
import signal

# do-nothing signal handler ensures that this process has "a" TERM
# handler in Python, which allows coverage's atexit() function to
# run...
signal.signal(signal.SIGTERM, lambda a, b: None)


print "subsub"
time.sleep(5)
print "done subsub"
