import sys
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.components.data_ingestion import DataIngestion
from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact


class TrainPipeline:
    def __init__(self):
        # Veri çekme konfigürasyonunu başlatıyoruz
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        Bu metot, TrainPipeline sınıfının veri çekme (data ingestion) bileşenini başlatmaktan sorumludur.
        """
        try:
            # Metoda girildiğini logluyoruz
            logging.info("TrainPipeline sınıfının start_data_ingestion metoduna girildi.")
            logging.info("Veriler MongoDB'den alınıyor.")
            
            # Veri çekme işlemi için DataIngestion sınıfından bir nesne oluşturuluyor
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            # Veri çekme işlemi başlatılıyor ve sonuç alınıyor
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            
            # Eğitim ve test verileri MongoDB'den alındı loglanıyor
            logging.info("Eğitim verisi (train_set) ve test verisi (test_set) MongoDB'den alındı.")
            # Metodun sonlandırıldığı loglanıyor
            logging.info("start_data_ingestion metodundan çıkıldı.")
            
            # Veri çekme işleminin sonucu (data_ingestion_artifact) döndürülüyor
            return data_ingestion_artifact
        except Exception as e:
            # Hata oluşursa, özel bir hata sınıfı olan USvisaException ile hata fırlatılıyor
            raise USvisaException(e, sys) from e

    def run_pipeline(self, ) -> None:
        """
        This method of TrainPipeline class is responsible for running complete pipeline
        """
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise USvisaException(e, sys)
        
