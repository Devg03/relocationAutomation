import shutil
import os

path = "/home/wildwolf/Downloads/"
# Collects the lists of files available in PATH
files = os.listdir(path)


doc_ext = [".doc", ".docx", ".html", ".odt", ".pdf",
            ".xls", ".xlsx", ".ppt", ".pptx", ".zip", ".txt"]
pic_ext = [".jpeg", ".png", ".jpg", ".gif",
           ".tiff", ".bmp", "svg", ".psd", ".raw", ".av1"]
music_ext = [".pcm", ".wav", ".aiff", ".mp3", ".aac", ".ogg",
             ".wma", ".flac", ".alac", "wma"]
vid_ext = [".mp4", ".mov", ".wmv", ".avi", ".avchd", 
           ".flv", ".f4v", ".swf", ".mkv", ".webm", ".mpeg-2"]


orig_location = path  # Orig_location = Downloads directory
pictures_location = "/home/wildwolf/Pictures/"  # pictures_location = Pictures Directory
docs_location = "/home/wildwolf/Documents/"  # docs_location = Documents Directory
music_location = "/home/wildwolf/Music/"  # music_location = Music Directory
vid_location = "/home/wildwolf/Videos/"  # vid_location = Videos Directory
desktop_location = "/home/wildwolf/Desktop"  # desktop_location = Desktop Directory

def ren(full_name: str):
    count = 0
    if full_name.endswith(tuple(doc_ext)):
        for file_name in os.listdir(docs_location):
            if file_name in os.listdir(docs_location):
                count += 1

    name, ext = os.path.split(full_name)

    old_name = os.path.join(orig_location, full_name)
    new_name = os.path.join(orig_location, name + str(count) + ext)
    ren_name = os.rename(old_name, new_name)
    rename_measure(str(ren_name))

def rename_measure(full_name: str):
    if full_name.endswith(tuple(doc_ext)):
        if os.path.isfile(os.path.join(docs_location, full_name)):
            ren(full_name)
        else:
            shutil.move(orig_location + files[0], docs_location)

def main():

    counter = len(files)
    num = 0

    while num < counter:

        # splits the filename into name and extensions
        full_name = files[0]
        rename_measure(full_name)

        num += 1


if __name__ == '__main__':
    main()
