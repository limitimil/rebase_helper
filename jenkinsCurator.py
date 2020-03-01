import another_worker
from utils.logging import logger

class JenkinsCurator(another_worker.Worker):
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
            self.create_workspace(self.current_repo)
            self.is_dirty_workspace = False
        workspace = self.current_repo

    def teardown_branch(self, metadata):
        pass

    def handle_error(self, error):
        self.is_dirty_workspace = True
        logger.exception('JenkinsCurator')

