from hello import toyou, add, subtract, add_one

def test_add():
    assert add(1,2)==3

def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x


### Run to see failed test
def test_hello_add_one():
    assert add_one(test_hello_add_one.x) == 11

def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9