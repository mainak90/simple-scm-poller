from __future__ import print_function
from src.repo import Repo, Mirror
import logging, os, subprocess, json, time

class Poller(object):
    @staticmethod
    def poll():
        def getConfigParsed() -> object:
            if os.path.exists(os.path.expanduser("~") + '/poller.config'):
                return json.loads(open(os.path.expanduser("~") + '/poller.config').read())
            elif 'POLLER_CONFIG_PATH' in os.environ and os.path.isfile(os.environ['POLLER_CONFIG_PATH'] + '/poller.config'):
                return json.loads(open(os.environ['POLLER_CONFIG_PATH'] + '/poller.config').read())
            else:
                logging.error("It seems that there is no poller.config file in homedir neither defined via an env var "
                              "POLLER_CONFIG_PATH")

        _repolist = getConfigParsed()['repos']
        _interval = getConfigParsed()['interval']
        for repo in _repolist:
            if not os.path.isdir(repo['dir']):
                Mirror(repodir=repo['dir'], remote=repo['uri']).mirror()
            elif os.path.isdir(repo['dir']) and Repo(dir=repo['dir'], branch=repo['branch']).get_hash() != Repo(remote=repo['uri'], branch=repo['branch']).get_remote_hash():
                Mirror(repodir=repo['dir'], remote=repo['uri']).sync()
            else:
                logging.info('No changes detected in remote repository')
        time.sleep(_interval)













