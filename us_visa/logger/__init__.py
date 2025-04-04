import logging  # Python'daki logging modülünü içeri aktarıyor. Bu modül, log mesajlarını kaydetmek için kullanılır.
import os  # OS modülünü içeri aktarıyor. Bu modül, dosya ve dizin işlemleri yapmamıza olanak tanır.
from from_root import from_root  # 'from_root' modülünden 'from_root' fonksiyonunu içeri aktarıyor. Bu, genellikle projenin kök dizinini bulmak için kullanılır.
from datetime import datetime  # datetime modülünden datetime sınıfını içeri aktarıyor. Bu sınıf, tarih ve saatle ilgili işlemler yapmamıza olanak tanır.

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # Geçerli tarih ve saati kullanarak log dosyasının adını dinamik olarak oluşturuyor. Örneğin: "03_17_2025_14_23_12.log".

log_dir = 'logs'  # Log dosyalarının saklanacağı dizini belirtir. Burada 'logs' dizini kullanılacak.

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)  # 'logs' dizini içinde oluşturulacak log dosyasının tam yolunu belirtir. 'from_root()' projenin kök dizinini döndürür.

os.makedirs(log_dir, exist_ok=True)  # 'logs' dizinini oluşturur. Eğer dizin zaten varsa, 'exist_ok=True' parametresi sayesinde hata vermez ve devam eder.

logging.basicConfig(  # logging modülünü yapılandırır. 
    filename=logs_path,  # Logların kaydedileceği dosyanın yolunu belirler. 'logs_path' burada önceki satırlarda belirlenen tam dosya yoludur.
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",  # Log mesajlarının formatını belirtir. Zaman damgası, logger adı, log seviyesi ve mesajı içerir.
    level=logging.DEBUG,  # Log seviyesini belirler. 'DEBUG' seviyesi, en ayrıntılı logları (DEBUG, INFO, WARNING, ERROR, CRITICAL) kaydeder.
)