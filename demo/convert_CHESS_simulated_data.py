# -*- coding: utf-8 -*-
"""
.. module:: convert_CHESS.py
   :platform: Unix
   :synopsis: Convert CHESS TIFF files in data exchange.

Example on how to use the `series_of_images`_ module to read CHESS TIFF raw tomographic data and save them as Data Exchange

:Author:
  `Francesco De Carlo <mailto: decarlof@gmail.com>`_

:Organization:
  Argonne National Laboratory, Argonne, IL 60439 USA

:Version: 2014.08.15


Examples
--------

>>> add example here 
>>> add example here 
>>> add example here 
>>> add example here 
>>> add example here 

.. _series_of_images: dataexchange.xtomo.xtomo_importer.html
"""

import dataexchange.xtomo.xtomo_importer as dx
import dataexchange.xtomo.xtomo_exporter as ex

def main():

    file_name = '/local/dataraid/databank/CHESS/Dummy001_.tif'
    hdf5_file_name = '/local/dataraid/databank/dataExchange/microCT/CHESS_01.h5'
    sample_name = 'Dummy'

    projections_start = 1
    projections_end = 181
    white_start = 0
    white_end = 10
    white_step = 1
    dark_start = 0
    dark_end = 10
    dark_step = 1

    mydata = dx.Import()
    # Read series of images
    data, white, dark, theta = mydata.series_of_images(file_name,
                                                       projections_start = projections_start,
                                                       projections_end = projections_end,
                                                       sample_name = sample_name,
                                                       projections_digits = 4,
                                                       projections_zeros = True,
                                                       log='INFO'
                                                    )    
    mydata = ex.Export()
    # Create minimal data exchange hdf5 file
    mydata.xtomo_exchange(data = data,
                          data_white = white,
                          data_dark = dark,
                          theta = theta,
                          hdf5_file_name = hdf5_file_name,
                          data_exchange_type = 'tomography_raw_projections'
                          )

if __name__ == "__main__":
    main()

