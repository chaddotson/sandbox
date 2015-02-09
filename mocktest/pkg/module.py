

class Tester(object):

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
