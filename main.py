import sys

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    TrainingPipelineConfig,
)
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()

        dataingestionconfig = DataIngestionConfig(
            trainingpipelineconfig
        )

        dataingestion = DataIngestion(dataingestionconfig)

        logging.info("Data ingestion started")

        dataingestionartifact = dataingestion.initiate_data_ingestion()

        logging.info("Data ingestion completed")

        data_validation_config = DataValidationConfig(
            trainingpipelineconfig
        )

        data_validation = DataValidation(
            dataingestionartifact,
            data_validation_config
        )

        logging.info("Data validation started")

        data_validation_artifact = (
            data_validation.initiate_data_validation()
        )

        logging.info("Data validation completed")

    except Exception as e:
        raise NetworkSecurityException(e, sys)