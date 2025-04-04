import os  # Os modülünü içeri aktarır, dosya sistemi ile etkileşim için kullanılır.
import sys  # Sys modülünü içeri aktarır, Python çalışma zamanına dair bazı fonksiyonları kullanmak için gereklidir.

def error_message_detail(error, error_detail: sys):  # Hata detaylarını işleyen fonksiyonun başı.
    _, _, exc_tb = error_detail.exc_info()  # Hata bilgisini ve traceback (izleme) detaylarını almak için sys.exc_info() kullanılır.
    file_name = exc_tb.tb_frame.f_code.co_filename  # Hatanın oluştuğu dosyanın adını alır.
    
    # Hata mesajını formatlar, dosya adı, satır numarası ve hata mesajını içeren bir string oluşturur.
    error_message = "Hata oluştu, Python script adı [{0}] satır numarası [{1}] hata mesajı [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)  # Dosya adı, satır numarası ve hata mesajını formatlayarak birleştirir.
    )

    return error_message  # Oluşturulan hata mesajını geri döndürür.

class USvisaException(Exception):  # USvisaException isminde yeni bir özel hata sınıfı tanımlar. Bu sınıf Exception sınıfından türetilmiştir.
    def __init__(self, error_message, error_detail):  # Hata mesajı ve detayları ile ilgili yapıcı metod.
        """
        :param error_message: Hata mesajı (string formatında).
        """
        super().__init__(error_message)  # Üst sınıf (Exception) yapıcısına hata mesajını iletir.
        self.error_message = error_message_detail(  # Hata mesajını detaylandırmak için error_message_detail fonksiyonunu çağırır.
            error_message, error_detail=error_detail  # Hata mesajı ve hata detaylarını gönderir.
        )

    def __str__(self):  # Hata mesajını döndüren metodu tanımlar.
        return self.error_message  # Özelleştirilmiş hata mesajını geri döndürür.