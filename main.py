import sys

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.exception.exception import NetworkSecurityException


if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()

        dataingestionconfig = DataIngestionConfig(
            trainingpipelineconfig
        )

        dataingestion = DataIngestion(
            dataingestionconfig
        )

        print("Data ingestion object created successfully")

    except Exception as e:
        raise NetworkSecurityException(e, sys)