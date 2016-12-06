from subprocess import Popen, PIPE

def executive():
	cmd = ['python2 ./run.py']
	p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)

	out, err = p.communicate()

	out = out.decode("utf-8")
	# print(err)

	return out

print(executive())