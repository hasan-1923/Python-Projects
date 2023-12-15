#Tesla WebSite Open and Model Pages
import pytest
from Pages.test_testmodell3 import TestTestmodell3
from Pages.test_testmodels import TestTestmodels
from Pages.test_testmodely import TestTestmodely

@pytest.mark.usefixtures("setup")
class TestModelClick:
    def test_Car_Model_Click(self):

        test_testmodell3=TestTestmodell3(self.driver) # Model3 Page 
        test_testmodell3.test_testmodell33()
        test_testmodels=TestTestmodels(self.driver)   # ModelS Page
        test_testmodels.test_testmodelS()
        test_testmodely=TestTestmodely(self.driver)   #ModelY Page
        test_testmodely.test_testmodelY()


        
    

    