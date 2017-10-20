import datetime
import pathlib
import zipfile              #A

FILE_PATTERN = "*.txt"
ARCHIVE = "archive"

if __name__ == '__main__':
    
    date_string = datetime.date.today().strftime("%Y-%m-%d")

    cur_path = pathlib.Path(".")
    paths = cur_path.glob(FILE_PATTERN)

    zip_file_path = cur_path.joinpath(ARCHIVE, date_string + ".zip")  #B
    zip_file = zipfile.ZipFile(str(zip_file_path), "w")               #C

    for path in paths:
        zip_file.write(str(path))                                     #D
        path.unlink()                              
