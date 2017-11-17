# mio_test.py

import mio

def main():
    mio.capture_output("myfile.txt")
    print("hello")
    print(1 + 3)
    mio.restore_output()
    
    mio.print_file("myfile.txt")
    
    
if __name__ == '__main__':
    main()
