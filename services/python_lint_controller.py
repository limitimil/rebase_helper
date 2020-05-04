import os
import subprocess
from subprocess import Popen
SCRIPT = " python -m autopep8 -i {file_path} --ignore E402 --max-line-length 120"
exception_files = [
    'testtools/api_testing_builder/api_testing_builder/generator/api_request/robot_api_request_generator.py',
    'testutils/edc_simulator/EDCSimFormAuto.py',
    'testtools/performance_testing/delete_receipts_in_services.py',
    'testutils/utils/test_data_utils/data_generator.py',
    'testutils/utils/test_data_utils/utils.py',
]
exception_files = list(map(lambda x: os.path.normpath(x), exception_files))
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
        exceptions = list(map(lambda x: os.path.join(self.working_directory, x), exception_files))
        files = []
        for f in folders:
            files.extend(self._get_python_paths(f))
        for f in files:
            if f in exceptions:
                continue
            process = Popen(SCRIPT.format(file_path=f),
                stdout=subprocess.PIPE, shell=True
            )
            result = process.communicate()
            self.history.append(result)
        return self.history
