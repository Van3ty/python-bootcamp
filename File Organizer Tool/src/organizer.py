from pathlib import Path
import shutil
from src.logger_config import logger

FILE_CATEGORIES = {
    ".jpg": "images",
    ".png": "images",
    ".pdf": "documents",
    ".txt": "text",
    ".mp3": "music",
    ".py": "code"
}



def organize_files(folder_path):
    print(f"Organizing files in: {folder_path}")
    for file in folder_path.iterdir():
        print(f"Processing: {file.name}")
        if file.is_dir():
            print(f"Skipping directory: {file.name}")
            continue
        category = FILE_CATEGORIES.get(file.suffix)

        print(f"Category: {category}")
        destination_folder = folder_path / category
        print(f"Destination folder: {destination_folder}")
        destination_folder.mkdir(exist_ok=True) 
        print(f"Moving {file.name} to {destination_folder}")
        shutil.move(str(file), str(destination_folder / file.name))
        print(f"Moved {file.name} --> {category}")
        logger.info(f'Moved {file.name} --> {category}')

