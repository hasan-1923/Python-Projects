#Tesla WebSite Open and Model Pages
import pytest
from Pages.test_cyberTruck   import TestCyberTruck
from Pages.test_testRoadster import TestTestRoadster
from Pages.test_testmodell3  import TestTestmodell3
from Pages.test_testmodels   import TestTestmodels
from Pages.test_testmodelx   import TestTestmodelx
from Pages.test_testmodely   import TestTestmodely
from Pages.test_testpowerwall import TestTestpowerwall

@pytest.mark.usefixtures("setup")
class TestModelClick:
    def test_Car_Model_Click(self):
        test_testmodels=TestTestmodels(self.driver)       # Model-S Page
        test_testmodels.test_testmodelS()

        test_testmodell3=TestTestmodell3(self.driver)     # Model-3 Page 
        test_testmodell3.test_testmodell33()
        
        test_testmodelx=TestTestmodelx(self.driver)       # Model-X Page
        test_testmodelx.test_testmodelX()
        
        test_testmodely=TestTestmodely(self.driver)       # Model-Y Page
        test_testmodely.test_testmodelY()

        test_cyberTruck=TestCyberTruck(self.driver)       # Model CyberTruck Page
        test_cyberTruck.test_cyberTruck()

        test_testRoadster=TestTestRoadster(self.driver)   # Model Roadster Page 
        test_testRoadster.test_testRoadsteR()
      
    def test_Page_Open(self):
        test_testpowerwall=TestTestpowerwall(self.driver) # Powerwall Page 
        test_testpowerwall.test_testPowerwall()





        
    

    