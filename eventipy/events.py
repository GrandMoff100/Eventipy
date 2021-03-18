import threading
from .defaults import Defaults

class Event:
    def __init__(self, func, name=None):
        if name is None:
            name = Defaults('unnamed')
        self.name = name
        self._f = func
        self.listeners = []
        self.threads = None
    
    def _trigger(self, *args, **kwargs):
        ts = []

        ts.append(threading.Thread(
            target=self._f,
            args=args,
            kwargs=kwargs
        ))
        for listener in self.listeners:
            ts.append(threading.Thread(
                target=listener,
                args=args,
                kwargs=kwargs
            ))
        return ts
    
    def trigger(self, *args, block=False, **kwargs):
        threads = self._trigger(*args, **kwargs)
        for t in threads:
            t.start()
        if block:
            for t in threads:
                t.join()

    def listener(self, func):
        self.listeners.append(func)
        return func
    
    def __repr__(self):
        return f'<Event {self.name}>'
    
    def __call__(self, *args, **kwargs):
        self.trigger(*args, **kwargs)


def event(*args, **kwargs):
    def decorator(func):
        return Event(*args, func, **kwargs)
    return decorator
