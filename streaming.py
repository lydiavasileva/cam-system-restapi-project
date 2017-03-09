# mock class to show how a streaming class could function.
# could be probably implemented at some point, though.

class Streaming( object ):
    def __init__( self ):
        self.running = False

    def is_running( self ):
        return self.running
