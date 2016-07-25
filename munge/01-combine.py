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
    # Load data
    print("Started!")
    data_dir = os.path.abspath('../data/original')
    zipfile_name = 'gait-data.tar.gz'
    file = os.path.join(data_dir, zipfile_name)
    data = pd.DataFrame()
    with tarfile.open(file) as tar:
        for member in tar.getmembers():
            if '.txt' in member.name:
                f = tar.extractfile(member)
                content = StringIO(f.read().decode('utf-8'))
                df = pd.read_csv(content, sep="\t",
                                 names=['time', 'stride_interval'])
                name = member.name
                name = name.replace('gait-data/', '')
                name = name.replace('-si.txt', '')
                if '-' in name:
                    trial = name[0]
                    participant = name[1]
                    age = int(name[3:6])
                else:
                    trial = name[0:2]
                    participant = name[2]
                    age = None

                df['trial'] = trial
                df['participant'] = participant
                df['age'] = age
                data = pd.concat([data, df], axis=0)

    # Write out data
    data.to_csv('../data/prepped/intervals.csv', index=False)
    print("Finished!")


if __name__ == '__main__':
    main()
