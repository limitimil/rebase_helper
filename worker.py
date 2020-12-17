import git
import tempfile
import tqdm
import abc
import os

from utils.system_functions import remove_folder
from utils.wrappers import FeatureToggle

class Worker(abc.ABC):
    repo_history = []
    branch_history = []
    workspace_history = []

    @property
    def current_repo(self):
        return self.repo_history[-1]

    @property
    def current_workspace(self):
        return self.workspace_history[-1]

    @property
    def current_branch(self):
        return self.branch_history[-1]

    def create_workspace(self,url):
        p = tempfile.mkdtemp()
        self.workspace_history.append(p)
        self.repo_history.append(git.Repo.clone_from(url=url, to_path=p))

    def clean_repo(self):
        repo = self.current_repo
        repo.git.reset('HEAD')
        repo.git.checkout('--','.')

    def run_for_each_repo(self, repo_configuration):
        for repo in tqdm.tqdm(repo_configuration):
            #setup
            self.create_workspace(repo.url)
            try :
                self.setup_repo(repo)
                #execute
                self.run_with_error_handler(repo, self.run_for_each_branch)
                #teardown
                self.teardown_repo(repo)
            except Exception as e:
                print(e)
                self.handle_error(e)

    def run_for_each_branch(self, branch_configuration):
        for branch in tqdm.tqdm(branch_configuration, total=branch_configuration.work_load):
            self.branch_history.append(branch)
            #setup
            self.clean_repo()
            try :
                self.setup_branch(branch)
                #execute
                self.run_with_error_handler(branch, self.run)
                #teardown
                self.teardown_branch(branch)
            except Exception as e:
                print(e)
                self.handle_error(e)

    def run_with_error_handler(self, metadata, func):
        try:
            func(metadata)
        except Exception as e:
            print(e)
            self.handle_error(e)

    @FeatureToggle.disable
    def remove_all_workspace(self):
        for folder in self.workspace_history:
            remove_folder(folder)
        self.workspace_history = []

    @abc.abstractmethod
    def run(self, metadata):
        return NotImplemented

    @abc.abstractmethod
    def teardown_repo(self, metadata):
        return NotImplemented

    @abc.abstractmethod
    def setup_repo(self, metadata):
        return NotImplemented

    @abc.abstractmethod
    def teardown_branch(self, metadata):
        return NotImplemented

    @abc.abstractmethod
    def setup_branch(self, metadata):
        return NotImplemented

    @abc.abstractmethod
    def handle_error(self, error):
        return NotImplemented
