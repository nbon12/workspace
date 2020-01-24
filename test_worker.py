import unittest
from unittest import TestCase, mock

from worker import Worker, Helper


class TestWorker(TestCase):

    def test_patching_class(self):
        # this test will give a false positive,
        # there is not `get_path` method but we've mocked it
        with mock.patch('worker.Helper', autospec=True) as MockHelper:
            import pdb
            pdb.set_trace()
            MockHelper.return_value.get_path.return_value = 'testing'
            worker = Worker()
            MockHelper.assert_called_once_with('db')
            self.assertEqual(worker.work(), 'testing')

if __name__ == '__main__':
    unittest.main()