import weakref

class Cached(type):
    def __init__(self, *args, **kwargs):
        super(Cached, self).__init__(*args, **kwargs)
        #self.__cache = weakref.WeakValueDictionary()
        self.__cache = {} 

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super(Cached, self).__call__(*args)
	    self.__cache[args] = obj
            return obj 
