import subprocess
import signal
import time

def main():
	proc = subprocess.Popen(["python", "test.py"], creationflags=0)

	child_pid = proc.pid

	time.sleep(1)
	proc.terminate()




main()
