from js import JSObject

xx = JSObject({
    "test" : { "thing" : 1 } ,
    "other":2,
    "stuff": [5,{12:34,"blah":"mine"},7,8,{"rawr":"ha"},0]
})

print(xx.other)
print(xx.test)
print(xx.test.thing)
print(xx.stuff)
print(xx.stuff[1])
print(xx.stuff[1].blah)
