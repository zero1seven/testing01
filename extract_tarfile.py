import tarfile

tarfile = "tarfile.tar"
file_obj = tarfile.open(filename,"r")
file = file_obj.extractall("extracted_tar_folder")
file_obj.close()