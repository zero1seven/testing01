import tarfile

tarfile = "tarfile.tar"
with open(tarfile, 'r') as f:
	tarfile.extractall()