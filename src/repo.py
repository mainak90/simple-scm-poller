import logging, subprocess, os

class Repo(object):
    def __init__(self, dir=None, remote=None, branch=None):
        self._dir = dir
        self._remote = remote
        self._branch = branch

    def get_branch(self):
        logging.debug("Getting BranchRef")
        if os.path.isdir(self._dir):
            cmd = ['git', '--git-dir={0}'.format(self._dir), 'branch']
            logging.info("executing cmd: {0}".format(cmd))
            return subprocess.check_output(cmd).decode('utf-8').replace('*', '').split()
        else:
            # Errorclass to go here
            pass

    def get_hash(self) -> object:
        logging.debug("Getting commit hash")
        cmd = ['git', '--git-dir={0}'.format(self._dir), 'rev-parse', self._branch]
        logging.info("executing cmd: {0}".format(cmd))
        return subprocess.check_output(cmd).decode('utf-8').strip()

    def get_remote_hash(self) -> object:
        logging.debug('Getting remote hash')
        return subprocess.check_output("git ls-remote {0} | grep {1} | head -1 | awk '{print $1}'".format(self._remote, self._branch)).decode('utf-8').strip()

class Mirror(object):
    def __init__(self, repodir: object = None, remote: object = None) -> object:
        self._repodir = repodir
        self._remote = remote

    def mirror(self):
        if self._repodir is None or self._remote is None:
            # Raise Errorclass exception
            pass
        logging.info("Mirroring {0} at {1}.".format(self._remote, self._repodir))
        cmd = ['git', 'clone', '--mirror', self._remote, self._repodir
        logging.info("Executing command: {0}".format(cmd))
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)

    def sync(self):
        if self._repodir is None:
            # Errorclass invoke
            pass
        logging.info("Updating an existing mirror {0} from remote".format(self._repodir))
        cmd = ['git', '--git-dir={0}'.format(self._repodir), 'remote', 'update']
        logging.info("Executing command: {0}".format(cmd))
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)