import subprocess
import signal
import time

def main():
	proc = subprocess.Popen(["python", "test.py"], creationflags=0)

	child_pid = proc.pid

	(output, error) = proc.communicate()

	if error:
		print "Error:", error

	print "Output:", output

	#sleep(1)
	print child_pid
	proc.terminate()
	print child_pid




main()
