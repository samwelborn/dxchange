# -*- coding: utf-8 -*-
"""
.. module:: import_tomoPy_Elettra.py
   :platform: Unix
   :synopsis: reconstruct Elettra Synchrotron Facility data with TomoPy
   :INPUT
       series of tiff or data exchange 

.. moduleauthor:: Francesco De Carlo <decarlof@gmail.com>


""" 
# tomoPy: https://github.com/tomopy/tomopy
import tomopy 

# Data Exchange: https://github.com/data-exchange/data-exchange
import dataexchange.xtomo.xtomo_importer as dx


def main():
    # read a series of tiff

    file_name = '/media/DISK_01/databank/dataExchange/microCT/Elettra_OK.h5'
    file_name = '/media/DISK_01/databank/dataExchange/microCT/Sangid_ShortFiber.h5' 
    file_name = '/media/DISK_01/databank/dataExchange/microCT/Elettra_LAST.h5'
    # to reconstruct slices from slices_start to slices_end
    # if omitted all data set is recontructed
    
    slices_start = 150    
    slices_end = 154    

    slices_start = 1365
    slices_end = 1367

    slices_start = 150    
    slices_end = 154    

    mydata = dx.Import()
    # Read series of images
    data, white, dark, theta = mydata.series_of_images(file_name,
                                                       slices_start = slices_start,
                                                       slices_end = slices_end,
                                                       data_type='h5',
                                                       log='INFO'
                                                       )
    # TomoPy xtomo object creation and pipeline of methods.  
    d = tomopy.xtomo_dataset(log='debug')
    d.dataset(data, white, dark, theta)
    d.normalize()
    #d.correct_drift()
    d.optimize_center()
    #d.phase_retrieval()
    #d.correct_drift()
    #d.center=1096.375
    d.gridrec()


    # Write to stack of TIFFs.
    tomopy.xtomo_writer(d.data_recon, 'tmp/ELETTRA_LAST_', axis=0)

if __name__ == "__main__":
    main()

