from pathlib import Path

from src.organizer import organize_files

folder_path = Path("test_folder")

if __name__ == "__main__":
    organize_files(folder_path)