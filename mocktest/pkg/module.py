


class Base:
    def __init__(self):
        print "in base"

class Tester(Base):

    def __init__(self):
        print "in tester"

        Base.__init__(self)
    

    @staticmethod
    def _postfix():
        return "- in original"

    def _prefix(self):
        return "in original -"

    def say(self, msg):
        print self._prefix() + msg + self._postfix()


def say_something(msg):
    print "[" + msg + "]"

class Factory(object):
    def get(self):
        return Tester()

    def get2(self):
        return Tester
