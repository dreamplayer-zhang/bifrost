"""
# test_guppi.py

This testbench tests a guppi gpuspec reader
"""

# Python2 compatibility
from __future__ import print_function

import os
import glob
import numpy as np
import bifrost.pipeline as bfp
from bifrost.blocks import GuppiRawSourceBlock

from scipy.fftpack import fft as scipy_fft

if __name__ == "__main__":
    # Setup pipeline
    filenames   = sorted(glob.glob('testdata/guppi_raw/*.raw'))
    filenames   = sorted(glob.glob('/bldata/gbt_raw/*.raw'))
    b_read      = GuppiRawSourceBlock(filenames, core=0)

    # Run pipeline
    pipeline = bfp.get_default_pipeline()
    print(pipeline.dot_graph())
    pipeline.run()
    
