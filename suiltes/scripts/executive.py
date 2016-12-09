from subprocess import Popen, PIPE


def execut():
	cmd = ["py", "-2", "./scripts/run_test.py"]
	p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)

	out, err = p.communicate()

	out = out.decode("utf8")
	return out

#print(execut())