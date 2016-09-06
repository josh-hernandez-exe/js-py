### Information

Tested with `Python 2.7>` and `Python 3.5>`.

The class will take in a nested object `dict`, or `list` (the output of a `json.loads`) and place them in an object that can be used like a javascrip object.

### Example 1

```python
import json
from pyjs import JSObject

converted_json = json.loads(
    '{ "test" : { "thing" : 1 } , "other":2, "stuff": [4,5,6,7,8]}'
)

myjso = JSObject(converted_json)

# Equivalent to
myjso_also = JSObject({
    u"test" : { u"thing" : 1 },
    u"other": 2,
    u"stuff": [4,5,6,7,8]
})

print myjso == myjso_also # True

print(myjso) # {u'test': {u'thing': 1}, u'other': 2}
print(myjso.test) # {u'thing': 1}
print(myjso.test.thing) # 1
print(myjso.other) # 2
print(myjso.stuff) # [4, 5, 6, 7, 8]
print(myjso.stuff[3]) # 7
```

### Example 2

```python
from pyjs import JSObject

myjso = JSObject({
    "test" : { "thing" : 1 },
    "other":2,
    "stuff": [5,{12:34,"blah":"mine"},7,8,{"rawr":"ha"},0]
})

print(myjso.other) # 2
print(myjso.test) # {'thing': 1}
print(myjso.test.thing) # 1
print(myjso.stuff) # [5, {'blah': 'mine', 12: 34}, 7, 8, {'rawr': 'ha'}, 0]
print(myjso.stuff[1]) # {'blah': 'mine', 12: 34}
print(myjso.stuff[1].blah) # mine

# Iterator functions
print(list(myjso.keys_())) # ['test', 'other', 'stuff']
print(list(myjso.values_())) # [{'thing': 1}, 2, [5, {'blah': 'mine', 12: 34}, 7, 8, {'rawr': 'ha'}, 0]]
print(list(myjso.items_())) # [('test', {'thing': 1}), ('other', 2), ('stuff', [5, {'blah': 'mine', 12: 34}, 7, 8, {'rawr': 'ha'}, 0])]

# Recursive accessor helper function
print(myjso.get_prop_chain_("stuff",2,"blah")) #
print(myjso.get_prop_chain_("stuff",1,"blah")) # 'mine'

```
