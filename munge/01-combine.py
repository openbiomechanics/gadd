"""TO BE EDITED.

TO BE EDITED.

Available defs:
- f: TO BE EDITED.
"""
from io import StringIO
import pandas as pd
import os
import tarfile


def main():
    print("Started!")

    # Load data
    data_dir = os.path.abspath('../data/original')
    data_dir = os.path.abspath('./data/original')
    zipfile_name = 'gait-data.tar.gz'
    file = os.path.join(data_dir, zipfile_name)

    tar = tarfile.open(file)
    for member in tar.getmembers():
        print(member.name)
        if '.txt' in member.name:
            f = tar.extractfile(member)
            content = f.read()
            print(content)

            TESTDATA = StringIO(content.decode('utf-8'))

            df = pd.read_csv(TESTDATA, sep="\t")

    tar.close()

    # Create new features

    # Write out data
    print("Finished!")


if __name__ == '__main__':
    main()
