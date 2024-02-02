import pytest


# parent class for all test classes
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
