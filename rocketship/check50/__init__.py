from check50 import *

class rocketship(Checks):

    @check()
    def exists(self):
        """rocketship.java exists"""
        self.require("""
        doc
        """rocketship.java")

    @check("exists") #will only run if exists is successful
    def compiles(self):
        """rocketship.java compiles"""
        self.spawn("javac rocketship.java.exit(0)
