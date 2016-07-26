# pysize

Use to quickly measure the size of your python objects. Supports:
* Measuring the size of self-referential objects
* No double-counting for repeated objects in a collection
* Python v2/v3

# Examples:
```python
>>> class Test(object):
>>>    pass
>>> from pysize import get_size
>>> z = Test()
>>> get_size(z)
344
>>> y = [z] * 10000
>>> get_size(y)
80416
>>> z.l = ["test"*100]
>>> get_size(z)
899
>>> get_size(y)
80971
```

To measure the size of `properties`, call `pysize.get_size` on the full list
of the object's members minus overhead and unwanted memberes:
```python
import pysize
class Ping(object):
    @property
    def ping(self):
        return 'pong'

class B(Ping):
    @property
    def marko(self):
        return 'polo'

obj = B()

to_measure = [getattr(obj, prop) for prop in dir(obj)\
              if prop not in dir(Ping)] # Exclude inherited attrs
empty_list_size = pysize.get_size([])
pysize.get_size(to_measure) - empty_list_size - 8 * len(to_measure)
```
