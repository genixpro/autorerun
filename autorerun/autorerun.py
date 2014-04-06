#    This file is part of Autorerun
# 
#    Autorerun is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    
#    Autorerun is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#



import watchdog
import sys
import logging
import time
import subprocess
import fnmatch
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RestartSubProcessEvent(FileSystemEventHandler):
    def __init__(self, command, pattern):
        super(RestartSubProcessEvent, self).__init__()
        self.process = None
        self.command = command
        self.pattern = pattern
        self.restart()
    
    def restart(self):
        if self.process is not None and self.process.poll() == None:
            logging.info("Killing old process.")
            self.process.kill()
        logging.info("Running %s" % (" ".join(self.command)))
        self.process = subprocess.Popen(self.command)
            
    def on_moved(self, event):
        super(RestartSubProcessEvent, self).on_moved(event)

        if fnmatch.fnmatch(event.src_path, self.pattern) or fnmatch.fnmatch(event.dest_path, self.pattern):
            what = 'directory' if event.is_directory else 'file'
            logging.info("Moved %s: from %s to %s", what, event.src_path, event.dest_path)
            self.restart()
         
    def on_created(self, event):
        super(RestartSubProcessEvent, self).on_created(event)
        
        if fnmatch.fnmatch(event.src_path, self.pattern):
            what = 'directory' if event.is_directory else 'file'
            logging.info("Created %s: %s", what, event.src_path)
            self.restart()

    def on_deleted(self, event):
        super(RestartSubProcessEvent, self).on_deleted(event)

        if fnmatch.fnmatch(event.src_path, self.pattern):
            what = 'directory' if event.is_directory else 'file'
            logging.info("Deleted %s: %s", what, event.src_path)
            self.restart()

    def on_modified(self, event):
        super(RestartSubProcessEvent, self).on_modified(event)

        if fnmatch.fnmatch(event.src_path, self.pattern):
            what = 'directory' if event.is_directory else 'file'
            logging.info("Modified %s: %s", what, event.src_path)
            self.restart()
    

def main():
    if len(sys.argv) < 4:
        print "Usage: autorerun <directory_to_monitory> <pattern> <command> <command_args>"
        return
    
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        
    directory = sys.argv[1]
    pattern = sys.argv[2]
    command = sys.argv[3:]
    
    event_handler = RestartSubProcessEvent(command, pattern)
    
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    
