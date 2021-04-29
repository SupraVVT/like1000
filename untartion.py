import glob, os
import tarfile


while glob.glob('*.tar'):
    for file in glob.glob("*.tar"):
            print("Unzipping {file}")
            my_tar = tarfile.open(file)
            my_tar.extractall()
            my_tar.close()


    deleteFile = file
    os.remove(deleteFile)


