"""TO BE EDITED.

TO BE EDITED.

Available defs:
- f: TO BE EDITED.
"""
import os
from zipfile import ZipFile


def main():
    print("Started!")

    # Load data
    data_dir = os.path.abspath('../data/original')
    data_dir = os.path.abspath('./data/original')
    zipfile_name = 'gait-data.tar.gz'
    file = os.path.join(data_dir, zipfile_name)
    print(file)

    # Create new features

    # Write out data
    print("Finished!")


if __name__ == '__main__':
    main()
