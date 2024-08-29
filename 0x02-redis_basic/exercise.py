#!/usr/bin/env python3
""" exercise.py """
import redis
import uuid
from typing import Union, Callable, Optional, Any


class Cache:
    """Defines Cache"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes],
                                         Any]] = None) -> Any:
        """ get """
        value = self._redis.get(key)
        if value is None:
            return "(nil)"
        return fn(value) if fn else value

    def get_str(self, key: str) -> Optional[str]:
        """ get_str """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[str]:
        """ get_int """
        return self.get(key, fn=int)
