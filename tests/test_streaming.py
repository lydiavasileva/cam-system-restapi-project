import unittest
import sys
sys.path.append( '..')

from streaming import *

dest_ip = "10.0.0.10"

class TestStreamingClass(unittest.TestCase):

    def test_init(self):
        s = Streaming()
        self.assertEqual( s.is_running(), False )

if __name__ == '__main__':
    unittest.main()
