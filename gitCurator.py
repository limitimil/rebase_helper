import worker
import tempfile
import os

from utils.logging import logger

project_dir = os.path.dirname(os.path.abspath(__file__))
os.environ['GIT_ASKPASS'] = os.path.join(
    project_dir,
    'utils',
    'git_askpasswd.py'
)
class GitCurator(worker.Worker):
    def __init__(self):
        self.is_dirty_workspace = False
    @property
    def current_workspace(self):
        return self.workspace_history[-1]

    def setup_repo(self, metadata):
        self.is_dirty_workspace = False

    def teardown_repo(self, metadata):
        pass

    def setup_branch(self, metadata):
        if self.is_dirty_workspace == True:
            self.create_workspace(self.current_repo.remotes.origin.url)
            self.is_dirty_workspace = False
        workspace = self.current_repo
        workspace.git.checkout(self.current_branch)

    def teardown_branch(self, metadata):
        pass

    def handle_error(self, error):
        self.is_dirty_workspace = True
        logger.exception('GitCurator')
