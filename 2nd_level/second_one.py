import tarfile

print("hello there")
with open("tarfile.tar", 'r') as f:
	tarfile.extractall()