from datetime import datetime
from from_root import from_root
import os
from src.constants import *
from dataclasses import dataclass

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

# The below code is defining the configuration for the training pipeline

@dataclass
class TrainingPipielineConfig:
    pipeline_name: str = 'src'
    artifact_dir: str = os.path.join(from_root(), 'artifact', TIMESTAMP)
    timestamp: datetime = TIMESTAMP
    
training_pipeline_config: TrainingPipielineConfig = TrainingPipielineConfig()


@dataclass
class DataIngestionConfig:
    download_dir: str = os.path.join(from_root(), DOWNLOAD_DIR)
    zip_file_path: str = os.path.join(download_dir, ZIPFILE_NAME)
    unzip_data_dir_path: str = os.path.join(download_dir, EXTRACT_DIR)
    
@dataclass
class DataPreprocessingConfig:
    data_preprocessing_artifacts_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_PREPROCESSING_ARTIFACTS_DIR)
    metadata_dir_path: str = os.path.join(data_preprocessing_artifacts_dir, METADATA_DIR)
    metadata_path: str = os.path.join(data_preprocessing_artifacts_dir, METADATA_DIR, METADATA_FILE_NAME)
    train_dir_path: str = os.path.join(data_preprocessing_artifacts_dir, DATA_PREPROCESSING_TRAIN_DIR)
    train_file_path: str = os.path.join(data_preprocessing_artifacts_dir, DATA_PREPROCESSING_TRAIN_DIR, TRAIN_FILE_NAME)
    test_dir_path: str = os.path.join(data_preprocessing_artifacts_dir, DATA_PREPROCESSING_TEST_DIR )
    test_file_path: str = os.path.join(data_preprocessing_artifacts_dir, DATA_PREPROCESSING_TEST_DIR, TEST_FILE_NAME)
    transformations_dir: str = os.path.join(data_preprocessing_artifacts_dir, OTHER_ARTIFACTS)
    transformations_object_path = os.path.join(data_preprocessing_artifacts_dir, transformations_dir, TRANSFORMATION_OBJECT_NAME)
    class_mappings_object_path = os.path.join(data_preprocessing_artifacts_dir, transformations_dir, CLASS_MAPPING_OBJECT_NAME)
    sample_rate: int = SAMPLE_RATE