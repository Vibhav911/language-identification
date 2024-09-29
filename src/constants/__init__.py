# common constants
DOWNLOAD_DIR = "download"
EXTRACT_DIR = 'download_language_data'
ZIPFILE_NAME = 'language-audio-data.zip'
S3_BUCKET_URI = 's3://language-audio-data/dataset/'
UNZIPPED_FOLDERNAME = 'language-audio-data'

DATA_PREPROCESSING_ARTIFACTS_DIR = "data_preprocessing_artifacts"
METADATA_DIR = 'metadata'
METADATA_FILE_NAME: str = "metadata.csv"
TRAIN_FILE_NAME: str = 'metadata_train.csv'
TEST_FILE_NAME: str = 'metadata_test.csv'

# Constants related to data preprocessing
DATA_PREPROCESSING_TRAIN_DIR: str = 'train'
DATA_PREPROCESSING_TEST_DIR : str = 'test'
DATA_PREPROCESSING_TRAIN_TEST_SPLIT_RATIO: float = 0.2
OTHER_ARTIFACTS = 'transformation'
TRANSFORMATION_OBJECT_NAME = 'mel_spectrogram.pkl'
CLASS_MAPPING_OBJECT_NAME = 'class_mappings.pkl'
S3_ARTIFACTS_URI: str = "s3://language-audio-data/transformation-artifacts/"

# Constants related to data transformations
SAMPLE_RATE: int = 4000
NUM_SAMPLES: int = 20000
FFT_SIZE: int = 1024
HOP_LENGTH: int = 512
N_MELS: int = 64