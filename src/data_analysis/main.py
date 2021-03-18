from pathlib import Path

import input_output
import statistical

if __name__ == '__main__':

    data_dir = Path('..\..\data')

    data = input_output.read_files(data_dir)

    new_npop = statistical.filter_by_variance_pd(data['npop'])

    # TODO: plot and save

    euc_dist = statistical.euclidean_distance_pd([1, 2], [3, 4], data['table'])
