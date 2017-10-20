from datetime import datetime, timedelta
import pathlib
import zipfile

FILE_PATTERN = "*.zip"
ARCHIVE = "archive"
ARCHIVE_WEEKDAY = 1      
if __name__ == '__main__':
    
    cur_path = pathlib.Path(".")
    zip_file_path = cur_path.joinpath(ARCHIVE)

    paths = zip_file_path.glob(FILE_PATTERN)
    current_date = datetime.today()     #A

    for path in paths:
        name = path.stem                 #B
        path_date = datetime.strptime(name, "%Y-%m-%d")     #C
        path_timedelta = current_date - path_date           #D
        if path_timedelta > timedelta(days=30) and path_date.weekday() != ARCHIVE_WEEKDAY:   #E
            path.unlink()
