import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB Configuration
MONGODB_URI = os.getenv('MONGODB_URI')
DATABASE_NAME = 'portfolio'
COLLECTION_NAME = 'creations'

# File Paths
CATALOG_CSV = '/Volumes/2025/SynologyDrive/Operating/Catalogs/creations_catalog.csv'
CREATIONS_BASE = '/Volumes/2025/SynologyDrive/Creations'
MEDIA_OUTPUT = '/Volumes/2025/SynologyDrive/Operating/elliottandrew-website/media'

# Image Optimization Settings
IMAGE_SIZES = {
    'thumb': 400,    # Thumbnail width
    'medium': 1000,  # Medium/detail width
    'large': 1500    # Full-size width
}

IMAGE_QUALITY = {
    'thumb': 85,
    'medium': 90,
    'large': 92
}

# Supported file extensions
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.tiff', '.tif', '.webp']
VIDEO_EXTENSIONS = ['.mp4', '.mov', '.avi', '.mkv']
