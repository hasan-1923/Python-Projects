import pytest
from Pages.anasayfa import Anasayfa
from Pages.ParfumPage import parfumepage
from Pages.sepet import SepetPage

@pytest.mark.usefixtures("setup")
class Testuruneklemetestler:

    def test_urun_ekleme_test(self):
        
        anasayfa=Anasayfa(self.driver)
        anasayfa.kategoryClick()
        ParfumePage=parfumepage(self.driver)
        ParfumePage.parfumeclick()
        sepet=SepetPage(self.driver)
        sepet.SepetClick()


        


    