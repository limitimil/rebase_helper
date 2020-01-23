import os
import git
import gitCurator
import config
from models.repositoryConfig import RepositoryConfig
from services.vue_lint_controller import VueLintController


class RebaseHandler(gitCurator.GitCurator):
    def before_rebase(self, metadata):
        pass

    def before_push(self, metadata):
        if 'vue-lint' in self.plugin_actions:
            controller = VueLintController(os.path.join(
                self.current_workspace, self.plugin_actions['vue-lint']['path']))
            controller.run()
            self.current_repo.git.add('-u')
            self.current_repo.git.commit(
                '-m', 'npm run lint by automation tool')

    def setup_repo(self, metadata):
        self.reference_branch = metadata.reference_branch
        self.plugin_actions = metadata.plugin_actions

    def run(self, metadata):
        commitId = self.current_repo.head.commit
        self.current_repo.git.checkout(self.current_branch)
        self.before_rebase(metadata)
        self.current_repo.git.rebase(self.reference_branch)
        if commitId == self.current_repo.head.commit or self.current_repo.is_dirty():
            raise Exception("rebase fail")
        self.before_push(metadata)
        self.current_repo.git.push('origin', self.current_branch, '-f')


if __name__ == '__main__':
    repos = map(lambda x: RepositoryConfig(x), config.config)
    handler = RebaseHandler()
    handler.run_for_each_repo(repos)
