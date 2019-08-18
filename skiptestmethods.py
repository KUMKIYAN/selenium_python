import unittest

def setUpModule():
    print("setup Module")
    
def tearDownModule():
    print("after Module")
        
class AppTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("this is login test")
    
    @classmethod
    def tearDown(self):
        print("this is logout test")
        
    @classmethod
    def setUpClass(cls):
        print("Open the application")
        
    @classmethod
    def tearDownClass(cls):
        print("Close the application")    

    @unittest.SkipTest #this decorator skip the test and not reflect in the report as well.    
    def test_search(self):
        print("this is search test")

    @unittest.skip("I am skipping this test method bcos it is not yet ready") #this decorator skip the test and however reflects in the report.
    def test_advancesearch(self):
        print("this is advance search")

    @unittest.skipIf(1==1,"Numbers are same") #this decorator skip the test based on condition and reflects in the report.
    def test_prepaidRecharge(self):
        print("this is prepaid recharge test")
    
    def test_postpaidPayment(self):
        print("this is postpaid payment test")

if __name__ == "__main__":
    unittest.main()
