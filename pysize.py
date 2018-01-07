import sys
import inspect

def get_size(obj):
    """Recursively finds size of objects in bytes"""
    size, queue, seen = 0, [obj], set()
    while queue:
        obj = queue.pop()
        obj_id = id(obj)
        if obj_id not in seen:
            size += sys.getsizeof(obj)
            seen.add(obj_id)
            if hasattr(obj, '__dict__'):
                for cls in obj.__class__.__mro__:
                    if '__dict__' in cls.__dict__:
                        d = cls.__dict__['__dict__']
                        if inspect.isgetsetdescriptor(d) or inspect.ismemberdescriptor(d):
                            queue.append(obj.__dict__)
                            queue.extend(obj.__dict__.keys())
                            queue.extend(obj.__dict__.values())
                        break
            if isinstance(obj, dict):
                queue.extend(obj.values())
                queue.extend(obj.keys())
            elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
                queue.extend(obj)
    return size
