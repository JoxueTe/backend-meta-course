import addition
import pytest

def test_add():
    assert addition.add(4,5) == 9


## pass the test without conditions
# def test_sub():
#     pass

def test_sub():
    assert addition.sub(4,5) == -1


# Flags for tests
#python3 -m pytest abc.py -v
#Fixture: @pytest.fixture 
#Marker: @pytest.mark.<markername>

'''
-v for verbose
-q quiet mode
-s allows the print statement inside the functions to be executed
-x is to flag the tests to stop execution after first failure
-m is used to mark a specific function
-k is a flag for searching and running tests with a specific keyword
--tb is to disable the traceback code of errors
--maxfail n specifies maximum number of test fails allowed
'''