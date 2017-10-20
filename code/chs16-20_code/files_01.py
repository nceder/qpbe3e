import datetime
import pathlib

FILE_PATTERN = "*.txt"               #A
ARCHIVE = "archive"                  #B

if __name__ == '__main__':
    
    date_string = datetime.date.today().strftime("%Y-%m-%d")     #C

    cur_path = pathlib.Path(".")
    paths = cur_path.glob(FILE_PATTERN)

    for path in paths:
        new_filename = "{}_{}{}".format(path.stem, date_string, path.suffix)
        new_path = cur_path.joinpath(ARCHIVE, new_filename)         #D
        path.rename(new_path)                                      #E
