import sys
import argparse
from zipfile import ZipFile


def extract(file_name):
    with ZipFile(file_name, 'r') as zf:
        for info in zf.infolist():
            cur_name = info.filename
            info.filename = cur_name.encode('cp437').decode('gbk')
            zf.extract(info)            
            print("File extracted to {}".format(info.filename))


def main(argv):
    parser = argparse.ArgumentParser(description='Extract GBK File Names')
    parser.add_argument('-f', '--file', required=True, type=str, help='Path of the compressed file.')
    args = parser.parse_args()
    file_name = args.file
    extract(file_name)


if __name__ == '__main__':
    main(sys.argv[1:])
