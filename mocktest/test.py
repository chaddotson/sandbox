from pkg.module import Factory


import mock

from unittest import TestCase

from pkg.module import say_something

def replacement_prefix():
    return "in replacement prefix -"

def replacement_postfix():
    return "- in replacement postfix"

def replacement_say_something(msg):
    print "{" + msg + "}"



class MyTestFixture(TestCase):


    def test_can_do_it(self):


        with mock.patch("pkg.module.Tester._prefix") as mockery:

            with mock.patch("pkg.module.Tester._postfix") as mockery2:

                mockery.side_effect = replacement_prefix
                mockery2.side_effect = replacement_postfix
                factory = Factory()

                instance = factory.get()
                maker = factory.get2()
                instance2 = maker()

                instance.say("test")
                instance2.say("test")

        with mock.patch("pkg.module.say_something") as mockery3:


            mockery3.side_effect = replacement_say_something

            say_something("here")

        self.assertTrue(False)
