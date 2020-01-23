import git
import gitCurator
import config
from models.repositoryConfig import RepositoryConfig

class RebaseHandler(gitCurator.GitCurator):
    def setup_repo(self, metadata):
        self.reference_branch = metadata.reference_branch
    def run(self, metadata):
        commitId = self.current_repo.head.commit
        self.current_repo.git.checkout(self.current_branch)
        self.current_repo.git.rebase(self.reference_branch)
        if commitId == self.current_repo.head.commit or self.current_repo.is_dirty():
            raise Exception("rebase fail")
        self.current_repo.git.push('origin', self.current_repo.name, '-f')

if __name__ == '__main__':
    repos = map(lambda x: RepositoryConfig(x), config.config)
    handler = RebaseHandler()
    handler.run_for_each_repo(repos)