autorerun
=========

A simple script which will execute a given command and automatically restart if specific files / directories are updated. Useful for development.



Installation
============

Very simple to install. Just use:
    sudo pip install autorerun
    
    
Usage
=====


Very simple to use. The command profile looks like this:

autorerun <directory> <pattern> <command> <arguments>

- Directory is the directory to monitor for changes.
- Pattern is the pattern that updated files have to match in order for it to trigger an automatic restart event. It is a simple terminal glob-match, like "*.py". It is not a regular expression.
- Command is the command which will be executed and restarted automatically when a monitored file / directory is changed.
- Arguments are the arguments which will be given to <command>.

After execution, autorerun will begin monitoring the given directory and all sub-directories for changes. Changes can be deletions, moved files, new files or just updates to a file. If any change occurs, a restart will be initiated. Restarts begin by sending the existing process SIGTERM signal. It will then wait 0.5 seconds, and if the process is still running, a SIGKILL is issued. After it is killed, command is run again with the given arguments in exactly the way it was the first time.

Notes & Caveats
===============

Does not work with network file systems (NFS) because the kernel does not issue file-updated events. Same thing goes with Virtual-Box shared directories.


