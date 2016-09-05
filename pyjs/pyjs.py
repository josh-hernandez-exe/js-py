import six

class JSObject(object):

    def __init__(self, *args, **kwargs):

        argtemp = []

        for item in args:
            if issubclass(item.__class__, dict):
                kwargs.update(item)
            else:
                argtemp.append(item)

        self.__dict__.update(kwargs)

        for key,value in enumerate(argtemp):
            if self.__dict__.has_key(key):
                raise KeyError("Duplicate keys are being inserted from args.")
            else:
                self.__dict__.update((key,value))

        self._recursive_dict_constructor(self.__dict__)

    def _recursive_dict_constructor(self,object_=None):
        try:
            for key,value in six.iteritems(object_):
                self._recusive_helper_constructor(object_,key,value)
        except TypeError, te:
            pass

    def _recursive_list_constructor(self,object_=None):
        try:
            for key,value in enumerate(object_):
                self._recusive_helper_constructor(object_,key,value)
        except TypeError, te:
            pass

    def _recusive_helper_constructor(self,object_,key,value):
        value_class = value.__class__
        if issubclass(value_class, dict):
            object_[key] = self.__class__(value)
        elif issubclass(value_class,(list,tuple)):
            self._recursive_list_constructor(value)

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

    def __contains__(self,item):
        return self.__dict__.__contains__(item)

    def __iter__(self):
        return self.keys_()

    def keys_(self,**kwargs):
        for key in six.iterkeys(self.__dict__,**kwargs):
            if not ( key.startswith("_") or key.endswith("_") ):
                yield key

    def values_(self,**kwargs):
        for key in self.keys_(**kwargs):
            yield self[key]

    def items_(self,**kwargs):
        for key in self.keys_(**kwargs):
            yield key,self[key]

    def get_prop_chain_(self,*args,**kwargs):

        default_value=kwargs.get("default_value",None)
        raise_missing=kwargs.get("raise_missing",False)

        cur_instance = self
        for key in args:

            if isinstance(cur_instance, (JSObject,dict)) and key in cur_instance:
                cur_instance = cur_instance[key]

            elif isinstance(cur_instance, (tuple,list)) and 0 <= key <= len(cur_instance):
                cur_instance = cur_instance[key]

            else:
                if raise_missing:
                    raise Exception("Missing property {property} in property chain {chain}".format(
                        property=str(key),
                        chain=str(args),
                    ))
                return default_value

        return cur_instance
