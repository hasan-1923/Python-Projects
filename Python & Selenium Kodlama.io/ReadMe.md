1-)	 @pytest.fixture: Testler arasında paylaşılan öğeleri (nesneler, bağımlılıklar vb.) hazırlar. Yani bir testin çalışması için gereken 	önceden koşulların hazırlanmasına yardımcı olur.

2-)	@pytest.mark.parametrize: Bir test fonksiyonunu farklı parametre değerleriyle tekrar tekrar çalıştırır.

3-)	@pytest.mark.skip: Belirli bir testi atlamak için kullanılır.

4-)	@pytest.mark.xfail: Testin geçmesi beklenmeyen ve hatalı sonuçlar vermesi beklenen durumlarda kullanılır.

5-)	@pytest.mark.timeout: Bir testin belirli bir süre içinde çalışmasını sağlar ve belirtilen sürenin üzerine çıktığında testi durdurur.

6-)	@pytest.mark.dependency: Testler arasında bağımlılıklar belirlemek için kullanılır.

7-)	@pytest.mark.usefixtures: Test fonksiyonlarına, belirli bir fixture'ı otomatik olarak eklemek için kullanılır.
