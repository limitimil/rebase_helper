import os
import subprocess
from subprocess import Popen
SCRIPT = " python -m autopep8 -i {file_path} --ignore E402"
exception_files = [
    'testtools/api_testing_builder/api_testing_builder/generator/api_request/robot_api_request_generator.py',
    'testutils/edc_simulator/EDCSimFormAuto.py'
]
class PythonLintController:
    history = []

    def __init__(self, working_directory):
        self.working_directory = working_directory
        self.history = []

    def _get_python_paths(self, root_folder):
        files = []
        for r, d, f in os.walk(root_folder):
            for file in f:
                if file.endswith('.py'):
                    files.append(os.path.join(r, file))

        return files

    def run(self, **kwargs):
        folders = kwargs.get('targets', [])
        folders = list(map(lambda x: os.path.join(self.working_directory, x), folders))
        files = []
        for f in folders:
            files.extend(self._get_python_paths(f))
        for f in files:
            if f in exception_files:
                continue
            process = Popen(SCRIPT.format(file_path=f),
                stdout=subprocess.PIPE, shell=True, cwd = self.working_directory
            )
            result = process.communicate()
            self.history.append(result)
        return self.history