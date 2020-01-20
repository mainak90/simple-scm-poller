import src.repo
import unittest

class TestRepo(unittest.TestCase):
    def test_get_branch(self):
        branch = src.repo.Repo(dir='/testdir')
        self.assertIsInstance(branch, src.repo.Repo)
        self.assertEqual(branch._dir, '/testdir')
        self.assertEqual(branch._remote, None)
        self.assertEqual(branch._branch, None)

    def test_get_hash(self):
        hash = src.repo.Repo(dir='/testdir')
        self.assertIsInstance(hash, src.repo.Repo)
        self.assertEqual(hash._dir, '/testdir')
        self.assertEqual(hash._remote, None)
        self.assertEqual(hash._branch, None)

    def test_get_remote_hash(self):
        remotehash = src.repo.Repo(remote='dummygit.com/dummy/test.git', branch='master')
        self.assertIsInstance(remotehash, src.repo.Repo)
        self.assertEqual(remotehash._dir, None)
        self.assertEqual(remotehash._remote, 'dummygit.com/dummy/test.git')
        self.assertEqual(remotehash._branch, 'master')

if __name__ == '__main__':
    unittest.main()