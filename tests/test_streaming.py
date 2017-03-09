import unittest
import sys
sys.path.append( '..')

from streaming import *

dest_ip = "10.0.0.10"

class TestStreamingClass(unittest.TestCase):

    def test_init(self):
        s = Streaming()
        self.assertFalse( s.is_running() )

    def test_start( self ):
        s = Streaming()
        s.start( dest_ip )
        self.assertTrue( s.is_running() )
        self.assertEqual( s.destination, dest_ip )

if __name__ == '__main__':
    unittest.main()
