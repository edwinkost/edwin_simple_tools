#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

import pcraster as pcr
import netCDF4 as nc

import virtualOS as vos

# obtaining system arguments containing: clone_map, input_netcdf_filename, output_pcraster_filename, variable_name, date_yyyy_mm_dd
system_argument = sys.argv

#~ # TODO: help/hint about the system arguments needed to be provided 
#~ if sys.argv == "--help":  

# set clone map
clone_map_filename = sys.argv[1]
pcr.setclone(clone_map_filename)

# set input_netcdf_filename
input_netcdf_filename = sys.argv[2]

# set output_pcraster_filename
output_pcraster_filename = sys.argv[3]

# set variable_name
variable_name = None
if len(sys.argv) > 2: variable_name = sys.argv[4]
if variable_name == None: 
    # loop through variables keys and identify the first variable 
    variable_names = f.variables.keys()
    # ignoring some variable names
    variable_names.pop('lat','')
    variable_names.pop('lon','')
    variable_names.pop('latiudes','')
    variable_names.pop('longitudes','')
    variable_names.pop('latiude','')
    variable_names.pop('longitude','')
    variable_names.pop('time','')
    # use the first variable
    variable_name = str(variable_names[0])
msg = 'Converting '+variable_name+' from the pcraster file: '+input_netcdf_filename+' to '+output_pcraster_filename
print msg    

# set date_yyyy_mm_dd
date_yyyy_mm_dd = None
if len(sys.argv) > 3: date_yyyy_mm_dd = sys.argv[5]

# read netcdf file
if date_yyyy_mm_dd == None:
    map_value = vos.netcdf2PCRobjCloneWithoutTime(input_netcdf_filename,\
                                                  variable_name,\
                                                  clone_map_filename)
else:                                                  
    map_value = vos.netcdf2PCRobjCloneWithoutTime(input_netcdf_filename,\
                                                  variable_name,\
                                                  date_yyyy_mm_dd,\
                                                  clone_map_filename)
    
# save the map as pcraster map
pcr.report(map_value, output_pcraster_filename+".map")
