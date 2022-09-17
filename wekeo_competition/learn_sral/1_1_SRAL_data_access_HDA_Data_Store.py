import configparser
import shutil
import os
import json
import zipfile
import glob

import eumdac  # for downloading via the eumetsat/data-store
from hda import Client  # for downloading via wekeo

# set defaults and overwrite with frameworks config if it exists
config = configparser.ConfigParser()
config["nbook"] = {"v_wd": "700", "v_ht": "450"}
if os.path.exists(os.path.join(os.path.dirname(os.getcwd()), "frameworks", "config.ini")):
    config.read(os.path.join(os.path.dirname(os.getcwd()), "frameworks", "config.ini"))

# Create a download directory for our SRAL products
download_dir = os.path.join(os.getcwd(), "products")
os.makedirs(download_dir, exist_ok=True)
