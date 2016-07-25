"""TO BE EDITED.

TO BE EDITED.

Available defs:
- f: TO BE EDITED.
"""
import matplotlib.pyplot as plt
import os
from scipy.io import wavfile
from zipfile import ZipFile


def main():
    print("Started!")

    # Load data
    data_dir = os.path.abspath('../data/original')
    data_dir = os.path.abspath('./data/original')
    zipfile_name = 'training.zip'
    file = os.path.join(data_dir, zipfile_name)
    print(file)
    myzip = ZipFile(file, 'r')
    with ZipFile(file, 'r') as myzip:
        myzip.write('eggs.txt')

    data_dir = os.path.abspath('./data/prepped/training/training-a')
    file_name = 'a0001.wav'
    file = os.path.join(data_dir, file_name)
    sampling_rate, data = wavfile.read(file)

    # Show image
    plt.figure()
    plt.plot(data)
    plt.show()

    # Create new features

    # Write out data
    print("Finished!")


if __name__ == '__main__':
    main()
