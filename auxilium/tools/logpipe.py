# -*- coding: utf-8 -*-

# auxilium
# --------
# Python project for an automated test and deploy toolkit.
#
# Author:   sonntagsgesicht
# Version:  0.1.5, copyright Wednesday, 29 September 2021
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


import logging
import threading
import os

"""
from auxilium.tools.logpipe import LogPipe

proc = run(command, cwd=path, shell=True,
           stdout=LogPipe(level, log),
           stderr=LogPipe(ERROR, log), text=True)

"""


class LogPipe(threading.Thread):

    def __init__(self, level, log=logging.log):
        """Setup the object with a logger and a loglevel
        and start the thread
        """
        threading.Thread.__init__(self)
        self.daemon = False
        self.level = level
        self.log = log
        self.fdRead, self.fdWrite = os.pipe()
        self.pipeReader = os.fdopen(self.fdRead)
        self.start()

    def start(self):
        pass

    def fileno(self):
        """Return the write file descriptor of the pipe"""
        return self.fdWrite

    def run(self):
        """Run the thread, logging everything."""
        for line in iter(self.pipeReader.readline, ''):
            self.log(self.level, line.strip('\n'))
        self.pipeReader.close()

    def close(self):
        """Close the write end of the pipe."""
        os.close(self.fdWrite)

    def write(self, message):
        """If your code has something like sys.stdout.write"""
        self.log(self.level, message)

    def flush(self):
        """If you code has something like this sys.stdout.flush"""
        pass


# For testing
if __name__ == "__main__":
    import sys
    import subprocess

    logging.basicConfig(format='%(levelname)s  %(message)s',
                        level=logging.INFO)

    logpipe = LogPipe(logging.INFO, logging.log)
    with subprocess.Popen(['/bin/ls'], stdout=logpipe, stderr=logpipe) as s:
        logpipe.close()

    sys.exit()
