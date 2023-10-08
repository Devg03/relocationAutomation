import shutil
import os

path = "/home/wildwolf/Downloads/"

# Collects the lists of files available in PATH
files = os.listdir(path)

def main():
    counter = len(files)
    num = 0
    while num < counter:

        file = os.path.split(files[0])
        dir = str(file[0])
        file_name = str(file[1])

        name, ext = os.path.splitext(file_name)

        
if __name__ == '__main__':
    main()