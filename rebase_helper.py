import os
import git
import gitCurator
import config
from models.repositoryConfig import RepositoryConfig
from services.vue_lint_controller import VueLintController
from utils.logging import logger


class RebaseHandler(gitCurator.GitCurator):
    def before_rebase(self, metadata):
        pass

    def before_push(self, metadata):
        if 'vue-lint' in self.plugin_actions:
            controller = VueLintController(os.path.join(
                self.current_workspace, self.plugin_actions['vue-lint']['path']))
            controller.run()
            try:
                self.current_repo.git.add('-u')
                self.current_repo.git.commit(
                    '-m', 'npm run lint by automation tool')
            except git.exc.GitCommandError:
                logger.info('No lint has been done for branch {}'.format(self.current_branch))
        logger.info('Push branch {}'.format(self.current_branch))

    def setup_repo(self, metadata):
        self.reference_branch = metadata.reference_branch
        self.plugin_actions = metadata.plugin_actions
        logger.info('working on repository: {}'.format(metadata.url))

    def run(self, metadata):
        commitId = self.current_repo.head.commit
        self.current_repo.git.checkout(self.current_branch)
        self.before_rebase(metadata)
        self.current_repo.git.rebase(self.reference_branch)
        if self.current_repo.is_dirty():
            raise Exception("rebase fail on branch: {}".format(self.current_branch))
        self.before_push(metadata)
        if commitId != self.current_repo.head.commit:
            self.current_repo.git.push('origin', self.current_branch, '-f')
        else:
            logger.info('Branch {} don\'t need to be push'.format(self.current_branch))


if __name__ == '__main__':
    repos = list(map(lambda x: RepositoryConfig(x), config.config))
    handler = RebaseHandler()
    handler.run_for_each_repo(repos)
