from datetime import datetime
import backupcfg
import pathlib
from pathlib import Path
import shutil
import sys

import logging
logging.basicConfig(filename=backupcfg.LogFileLocation(), level = logging.DEBUG) 
logger=logging.getLogger()


current_datetime = datetime.now().strftime('%Y%m%d-%H%M%S')

#This is the location of the source file
src_file = backupcfg.SourceFiles()
if src_file == False: #The config file will return False if an argument inputted into the CLI is not supported
    err = "[TypeError] The argument entered into the command line is not supported."
    print(err)
    logger.error(err)
    quit()

if Path(src_file).exists() != True:
    err = "[FileNotFoundError] The source file could not be found: '" + str(src_file) + "'"
    print(err)
    logger.error(err)
    quit()

#Convert it using the class PurePath and extract the name of the file
src_loc = pathlib.PurePath(src_file)
src_name = src_loc.stem
src_type = src_loc.suffix

#This is the location of the destination directory

dst_dir = backupcfg.DestinationFolder()
if Path(dst_dir).exists() != True:
    err = "[FileNotFoundError] The backup folder could not be found: '" + str(dst_dir) + "'"
    print(err)
    logger.error(err)
    quit()

dst_loc = dst_dir + "/" + src_name + "_backup_" + current_datetime + src_type
# if "job01" in sys.argv:
#     print("Job 1")

try:
    #Fully copy the source file to the destination, only changing the name to append the datetime of operation
    print("src_loc : ", src_loc)
    print("dst_loc : ", dst_loc)
    shutil.copy2(src_loc, dst_loc)
    logger.info("Success")
except Exception as err:
    print("error for copy:", err)
    logger.error(err)
    # logger.fo()