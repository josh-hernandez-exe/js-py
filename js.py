class JSObject(object):

    def __init__(self, *args, **kwargs):

        argtemp = []

        for item in args:
            if isinstance(item, dict):
                kwargs.update(item)
            else:
                argtemp.append(item)

        argtemp = (
            (key,JSObject(**value) if isinstance(value,dict) else value)
            for key,value in argtemp
        )

        kwargs = {
            key:JSObject(**value) if isinstance(value,dict) else value
            for key,value in kwargs.items()
        }

        for arg in argtemp:
            self.__dict__.update(arg)

        self.__dict__.update(kwargs)

    def __getitem__(self, name):
        return self.__dict__.get(name, None)

    def __setitem__(self, name, val):
        return self.__dict__.__setitem__(name, val)

    def __delitem__(self, name):
        if self.__dict__.has_key(name):
            del self.__dict__[name]

    def __getattr__(self, name):
        return self.__getitem__(name)

    def __setattr__(self, name, val):
        return self.__setitem__(name, val)

    def __delattr__(self, name):
        return self.__delitem__(name)

    def __iter__(self):
        return self.__dict__.__iter__()

    def __repr__(self):
        return self.__dict__.__repr__()

    def __str__(self):
        return self.__dict__.__str__()

    def __eq__(self,other):
        if not isinstance(other, JSObject):
            return False

        return self.__dict__ == other.__dict__
