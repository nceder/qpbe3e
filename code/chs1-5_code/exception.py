class EmptyFileError(Exception):
    pass
filenames = ["myfile1","nonExistent", "emptyFile", "myfile2"]
for file in filenames:
    try:
        f = open(file,'r')
        line = f.readline()
        if line == "":
            f.close()
            raise EmptyFileError("%s: is empty" % (file))
    except IOError as error:
        print("%s: could not be opened: %s" % (file, error.strerror))
    except EmptyFileError as error:
        print(error)
    else:
        print("%s: %s" % (file, f.readline())) 
    finally:
        print("Done processing", file)
