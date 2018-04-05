#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:04:37 2018

@author: unityspace
"""

import re

class FileNameExtractor:
    def extract_file_name(dirty_file_name):
        patt = re.compile(r'\d+_([a-zA-Z_-]+\.\w+)')
        return(re.match(patt, dirty_file_name).group(1))





"""
https://www.codewars.com/kata/extract-file-name/train/python

You have to extract a portion of the file name as follows:

Assume it will start with date represented as long number
Followed by an underscore
Youll have then a filename with an extension
it will always have an extra extension at the end

Inputs
1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION

1_This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34

1231231223123131_myFile.tar.gz2

Outputs
FILE_NAME.EXTENSION

This_is_an_otherExample.mpg

myFile.tar


class FileNameExtractor:
    def extract_file_name(dirty_file_name):
        #your code here       
"""
