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

    for file in folder_path.iterdir():
        if file.is_dir():
            continue
        category = FILE_CATEGORIES.get(file.suffix)

        destination_folder = folder_path / category

        destination_folder.mkdir(exist_ok=True) 

        shutil.move(str(file), str(destination_folder / file.name))
        
        logger.info(f'Moved {file.name} --> {category}')