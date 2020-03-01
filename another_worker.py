import tempfile
import tqdm
import abc

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
        self.repo_history.append(url)

    def clean_repo(self):
        pass

    def run_for_each_repo(self, repo_configuration):
        for repo in tqdm.tqdm(repo_configuration):
            #setup
            self.create_workspace(repo.url)
            self.setup_repo(repo)
            #execute
            self.run_with_error_handler(repo, self.run_for_each_branch)
            #teardown
            self.teardown_repo(repo)

    def run_for_each_branch(self, branch_configuration):
        for branch in tqdm.tqdm(branch_configuration, total=branch_configuration.work_load):
            self.branch_history.append(branch)
            #setup
            self.clean_repo()
            self.setup_branch(branch)
            #execute
            self.run_with_error_handler(branch, self.run)
            #teardown
            self.teardown_branch(branch)

    def run_with_error_handler(self, metadata, func):
        try:
            func(metadata)
        except Exception as e:
            print(e)
            self.handle_error(e)

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

