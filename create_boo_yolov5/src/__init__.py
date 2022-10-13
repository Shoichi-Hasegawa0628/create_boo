#!/usr/bin/env python
# -*- coding: utf-8 -*-
import roslib.packages
import yaml

SPCO_DATA_PATH = str(roslib.packages.get_pkg_dir("create_boo")) + "/data/output/test/"

PLACE_IMAGE_DATA = SPCO_DATA_PATH + "image/"
PLACE_IMG_DATA = SPCO_DATA_PATH + "img/"
PLACE_WORD_DATA = SPCO_DATA_PATH + "tmp/"
POSITION_DATA = SPCO_DATA_PATH
OBJECT_FREQUENCY_DATA = SPCO_DATA_PATH + "tmp_boo/"

                      
with open('./Objects365.yaml', 'r') as yml:
    config = yaml.load(yml)

object_dictionary = config['names']
