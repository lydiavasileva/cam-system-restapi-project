# mock class to show how a streaming class could function.
# could be probably implemented at some point, though.

class Streaming( object ):
    def __init__( self ):
        self.running = False
        self.destination = None

    def is_running( self ):
        return self.running

    def start( self, dest_addr ):
        self.destination = dest_addr
        self.running = True

    def stop( self ):
        self.running = False
