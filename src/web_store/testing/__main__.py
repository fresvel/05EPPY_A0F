import unittest
from .test_login import TestLogin
from .test_store import TestStore
from .test_auth import TestAuth

def suite():
    test_suite=unittest.TestSuite()
    test_suite.addTest(TestLogin('test_get_login_page'))
    test_suite.addTest(TestLogin('test_successful_login'))
    test_suite.addTest(TestStore('test_get_store_page'))
    test_suite.addTest(TestStore('test_add_item'))

    test_suite.addTest(TestAuth('test_home_authentication'))
    test_suite.addTest(TestAuth('test_store_authentication'))
    return test_suite


def main():
    print("Running Test")
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
    unittest.main()


if __name__ == "__main__":
    main()

# suite y runners 38:37
#Mocking 47:00
#1:21:56