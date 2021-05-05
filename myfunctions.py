import subprocess
import time
import sys

class myfunctions:
    def openFolderButton(self):
        subprocess.Popen(r'explorer /open,"P:\Finished Coding Projects\Instagram Photo Downloader UNFINISHED"')

    def exit(self):
        time.sleep(0.5)
        sys.exit()

