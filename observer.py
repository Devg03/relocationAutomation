import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # path of the directory to watch
    path = '/home/wildwolf/Downloads'

    # Creates the isntance of LoggingEventHandler
    event_handler = LoggingEventHandler()

    # Creates the instance of Observer
    observer = Observer() 

    # tells the observer to handle the logging with the location to watch
    observer.schedule(event_handler, path, recursive=True)
    
    # Start the observer
    observer.start() 
    try:
        while True:
            time.sleep(1) # Delay period
    finally:
        observer.stop() # Finally stops the observer
        observer.join()