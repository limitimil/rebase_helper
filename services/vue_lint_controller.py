import os
import subprocess
from subprocess import Popen
SCRIPT = """
npm install
npm run lint
"""


class VueLintController:
    history = []

    def __init__(self, working_directory):
        self.working_directory = working_directory
        self.history = []

    def run(self):
        for line in SCRIPT.split('\n'):
            process = Popen(line,
                            stdout=subprocess.PIPE, shell=True, cwd=self.working_directory)
            result = process.communicate()
            self.history.append(result)
        return self.history
