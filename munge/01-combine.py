"""TO BE EDITED.

TO BE EDITED.

Available defs:
- f: TO BE EDITED.
"""
import os
import tarfile


def main():
    print("Started!")

    # Load data
    data_dir = os.path.abspath('../data/original')
    data_dir = os.path.abspath('./data/original')
    zipfile_name = 'gait-data.tar.gz'
    file = os.path.join(data_dir, zipfile_name)
    print(file)
    x = tarfile.open(file, 'r')
    for i in x:
        if '.txt' in i.name:
            print(i.name)

    # Create new features

    # Write out data
    print("Finished!")


if __name__ == '__main__':
    main()
