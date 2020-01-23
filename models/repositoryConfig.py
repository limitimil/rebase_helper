class RepositoryConfig:
    def __init__(self, config):
        self.url = config['repository_url']
        self.branches = config['branches']
        self.reference_branch = config.get('reference_branch', 'origin/develop')
    def __iter__(self):
        self._iter_pos = 0
        return self
    def __next__(self):
        if self._iter_pos < len(self.branches):
            self._iter_pos += 1
            return self.branches[self._iter_pos-1]
        raise StopIteration