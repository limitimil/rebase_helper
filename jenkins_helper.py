import os
import jenkins
import jenkinsCurator
import another_config
from models.jenkinsConfig import JenkinsConfig
from utils.logging import logger


class JenkinsHandler(jenkinsCurator.JenkinsCurator):
    _server = None

    def server(self):
        if self._server:
            raise Exception
        return self._server

    def setup_repo(self, metadata):
        self._current_job = metadata.url
        logger.info('working on jenkins job: {}'.format(metadata.url))

    def run(self, branch):
        self.server.build_job('{job}/{branch}'.format(
            job = self._current_job,
            branch = metadata
        ))


if __name__ == '__main__':
    jobs = list(map(lambda x: JenkinsConfig(x), another_config.config))
    handler = JenkinsHandler()
    handler._server = jenkins.Jenkins('http://192.168.96.25:8082', username='liminchien', password='xxxx')
    handler.run_for_each_repo(repos)

