from pathlib import Path

import numpy as np

import input_output
import numerical
import statistical
import plot

if __name__ == '__main__':

    data_dir = Path('data')
    output_dir = Path('output')
    if not output_dir.exists():
        output_dir.mkdir()

    data = input_output.read_files(data_dir)

    new_npop = statistical.filter_by_variance_pd(data['npop'])

    # TODO: plot and save

    euc_dist = statistical.euclidean_distance_pd([1, 2], [3, 4], data['table'])

    # do numerical analysis
    efield_filtered = statistical.filter_by_variance_pd(data['efield'])

    plot.plot_df(efield_filtered, output_dir / 'efield.pdf')

    efield_ft = numerical.fourier_transform(efield_filtered).apply(np.real)

    input_output.export_df(efield_ft, output_dir / 'efield_ft.csv')
    plot.plot_df(efield_ft, output_dir / 'efield_ft.pdf')

    nstate_filtered = statistical.filter_by_variance_pd(data['nstate_i'])
    nstate_autocorr = numerical.autocorr(nstate_filtered)

    input_output.export_df(nstate_autocorr, output_dir / 'nstate_i_autocorr.csv')
    plot.plot_df(nstate_autocorr, output_dir / 'nstate_i_autocorr.pdf')

    nstate_autocorr_dt = numerical.fourier_transform(nstate_autocorr)
    nstate_power = np.abs(nstate_autocorr_dt)**2

    input_output.export_df(nstate_power, output_dir / 'nstate_i_power_spectrum.csv')
    plot.plot_df(nstate_power, output_dir / 'nstate_power.pdf')
