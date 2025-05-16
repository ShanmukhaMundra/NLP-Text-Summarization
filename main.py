from src.textSummarizer.components.data_validation import DataValiadtion
from src.textSummarizer.pipeline.phase1_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.phase2_data_validation import DataValidationTrainingPipeline
from src.textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f"stage {STAGE_NAME} started")
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f"stage {STAGE_NAME} started")
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
        logger.exception(e)
        raise e