import git
from config import config
import tempfile
import tqdm
class RebaseHelper:
    repos = []
    current = None
    base_branch = 'origin/develop'

    @property
    def current(self):
        return self.repos[-1]

    # Workspace
    def set_workspace(self, target=None):
        if target:
            p = tempfile.mkdtemp()
            self.repos.append(git.Repo.clone_from(url=target['repository_url'],
                to_path=p))
        else:
            p = tempfile.mkdtemp()
            self.repos.append(git.Repo.clone_from(url=self.current.remotes.origin.url,
                to_path=p))

    def clean_workspace(self):
        ws = self.current
        ws.git.reset('HEAD')
        ws.git.checkout('--','.')

    # Worker
    def run(self):
        for target in tqdm.tqdm(config):
            self.set_workspace(target)
            self.rebase_worker(target)

    def rebase_worker(self, target):
        ws = self.current
        for branch_name in tqdm.tqdm(target['branches']):
            self.rebase_handler(branch_name)

    def rebase_handler(self, branch_name):
        ws = self.current
        try:
            commitId = ws.head.commit
            ws.git.checkout(branch_name)
            ws.git.rebase(self.base_branch)
            if commitId == ws.head.commit or ws.is_dirty():
                return
            self.post_stage_when_success()
        except:
            self.set_workspace()

    # Post Handler When Success
    def post_stage_when_success(self):
        ws = self.current
        ws.git.push('origin', ws.active_branch.name, '-f')

if __name__ == '__main__':
    rh = RebaseHelper()
    rh.run()
    
