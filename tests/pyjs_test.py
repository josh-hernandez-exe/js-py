import os, sys
import unittest

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
))

from pyjs import JSObject


class TestJSObject(unittest.TestCase):

    def make_object(self):
        return JSObject({
            "test" : { "thing" : 1 } ,
            "other":2,
            "stuff": [5,{12:34,"blah":"mine"},7,8,{"rawr":"ha"},0]
        })

    def test_jsobject_access(self):
        xx = self.make_object()

        print(xx.other)
        print(xx.test)
        print(xx.test.thing)
        print(xx.stuff)
        print(xx.stuff[1])
        print(xx.stuff[1].blah)


    def test_jsobject_value(self):

        xx = self.make_object()

        self.assertTrue(xx.test.thing==1)
        self.assertTrue(xx.other==2)
        self.assertTrue(xx.stuff[0]==5)
        self.assertTrue(xx.stuff[1].blah=="mine")


    def test_property_chain(self):
        xx = self.make_object()

        print "Hey"
        print xx.get_prop_chain_("test","thing",raise_missing=True)
        print "Bye"
        self.assertTrue(xx.get_prop_chain_("test","thing",raise_missing=True)==1)
        self.assertTrue(xx.get_prop_chain_("stuff",1,"blah",raise_missing=True)=="mine")



if __name__ == '__main__':
    unittest.main()
