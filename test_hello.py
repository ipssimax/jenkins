#!/usr/bin/env python3

import pytest
from hello_world import say_hello

def test_say_hello():
    result = say_hello()
    assert result == "Hello World!"
