class JenkinsConfig:

    def __init__(self, config):
        self.url = config['jenkins_url']
        self.branches = config['branches']
        self.plugin_actions = config.get('plugin_actions', {})
    @property
    def work_load(self):
        return len(self.branches)

    def __iter__(self):
        self._iter_pos = 0
        return self

    def __next__(self):
        if self._iter_pos < len(self.branches):
            self._iter_pos += 1
            return self.branches[self._iter_pos-1]
        raise StopIteration