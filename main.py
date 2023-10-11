import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

user = "wildwolf"

# extension types
docs_ext = [".txt", ".doc", ".docx", ".pdf", ".tex", ".wpd", '.rtf', ".odt"]
music_ext = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac", "."]
pics_ext = [".jpeg", ".gif", ".svg", ".png", ".psd", ".eps", ".tiff", ".raw"]
vids_ext = [".mp4", ".wmv", ".avi", ".avchd", ".flv", ".mkv", ".webm"]

# Location to store each type of extension
docs_location = f"/home/{user}/Documents"
pics_location = f"/home/{user}/Pictures"
music_location = f"/home/{user}/Music"
vids_location = f"/home/{user}/Videos"
desktop_location = f"/home/{user}/Desktop"

# Event handler
if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(
        patterns, ignore_patterns, ignore_directories, case_sensitive)

# Function for when the file is created in the watch directory
def on_created(event):
    print(f"Hey, {event.src_path} has been created.")

# Function for when the file is modified in the watch directory
def on_modified(event):
    print(f"Hey, {event.src_path} has been modified.")
    
    # Seperates directory and filname from the event.src_path
    dir, file_name = os.path.split(event.src_path)

    # Seperates name and extensions from file_name
    name, ext = os.path.splitext(file_name)

    # Moves files according to their extensions
    if ext in tuple(docs_ext):
        shutil.move(event.src_path, docs_location)
    elif ext in tuple(music_ext):
        shutil.move(event.src_path, music_location)
    elif ext in tuple(pics_ext):
        shutil.move(event.src_path, pics_location)
    elif ext in tuple(vids_ext):
        shutil.move(event.src_path, vids_location)

# Function for when the file is deleted in the watch directory
def on_deleted(event):
    print(f"Hey, {event.src_path} has been deleted.")

# Function for when the file is moved in the watch directory
def on_moved(event):
    print(f"Hey, {event.src_path} has moved to {event.dest_path}.")


# Defining what functions to call under each circumstance
my_event_handler.on_created = on_created
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved
my_event_handler.on_deleted = on_deleted

# Watchdog - observer
watch_dir = "/home/wildwolf/Downloads"
watchdog = Observer()
watchdog.schedule(my_event_handler, path=watch_dir, recursive=True)

watchdog.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    watchdog.stop()
    watchdog.join()
