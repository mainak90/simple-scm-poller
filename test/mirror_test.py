import src.repo
import unittest

class TestMirror(unittest.TestCase):
    def test_mirror(self):
        mirror = src.repo.Mirror(repodir='/testdir', remote='testgit.com/test/test.git')
        self.assertIsInstance(mirror, src.repo.Mirror)
        self.assertEqual(mirror._remote, 'testgit.com/test/test.git')
        self.assertEqual(mirror._repodir, '/testdir')

    def test_sync(self):
        sync = src.repo.Mirror(repodir='/testdir')
        self.assertIsInstance(sync, src.repo.Mirror)
        self.assertEqual(sync._remote, None)
        self.assertEqual(sync._repodir, '/testdir')

if __name__ == '__main__':
    unittest.main()