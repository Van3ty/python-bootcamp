from pathlib import Path

from src.organizer import organize_files

folder_path = Path("test_folder")

organize_files(folder_path)