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

        self.assertEquals(xx.test.thing,1)
        self.assertEquals(xx.other,2)
        self.assertEquals(xx.stuff[0],5)
        self.assertEquals(xx.stuff[1].blah,"mine")


    def test_property_chain(self):
        xx = self.make_object()

        self.assertEquals(xx.get_prop_chain_("test","thing",raise_missing=True),1)
        self.assertEquals(xx.get_prop_chain_("stuff",1,"blah",raise_missing=True),"mine")



if __name__ == '__main__':
    unittest.main()
