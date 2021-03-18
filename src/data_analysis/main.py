from pathlib import Path

import input_output

if __name__ == '__main__':

    data_dir = Path('data')

    data = input_output.read_files(data_dir)