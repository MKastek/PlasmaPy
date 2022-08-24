"""
Test`.h5` files came from
https://github.com/openPMD/openPMD-example-datasets/tree/b4f87b817629b99a048026a2724a5b265810d8be
"""
import glob

from pathlib import Path

data_dir = Path(__file__).parents[0]
data_files = glob.glob(str(data_dir.joinpath("*.[!p]*")))
