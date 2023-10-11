import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# Event handler
if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

# Function for when the file is created in the watch directory
def on_created(event):
    print(f"Hey, {event.src_path} has been created.")

# Function for when the file is modified in the watch directory
def on_modified(event):
    print(f"Hey, {event.src_path} has been modified.")

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
watchdog.schedule(my_event_handler, path = watch_dir, recursive=True)

watchdog.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    watchdog.stop()
    watchdog.join()