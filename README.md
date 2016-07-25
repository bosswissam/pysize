[![Build Status](https://travis-ci.org/bosswissam/pysize.svg?branch=master)](https://travis-ci.org/bosswissam/pysize)

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
