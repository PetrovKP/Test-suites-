from subprocess import Popen, PIPE


def execut():
	cmd = ['python2 ./run_test.py']
	p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)

	out, err = p.communicate()

	out = out.decode("utf-8")
	return out

print(execut())