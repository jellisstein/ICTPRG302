#backup.py version 1.0 by Jareth Ellis-Stein at 30027143@students.sunitafe.edu.au
#MIT License Copyright (c) 2025 [See the License file for more details]

#Use this script to backup any files you want to keep safe
#You can change the config file to specify file and folder locations as needed


from datetime import datetime
import pathlib
import shutil
import smtplib

import backupcfg

import logging
logging.basicConfig(filename=backupcfg.LogFileLocation(), level = logging.DEBUG) 
logger=logging.getLogger()


current_datetime = datetime.now().strftime('%Y%m%d-%H%M%S')
smtp = backupcfg.EmailDetails()

def SendEmail(message):
    email = "To: " + smtp["recipient"] + "\n" + "From: " + smtp["sender"] + "\n" + "Subject: Backup Results Log\n\n" + "An error has occured with the backup.py program, please see below for details:" + "\n" + message + "\n" + 25*"~" + "\n" + "Backup target: " + source_file + "\n" + "Backup destination: " + destination_dir + "\n"
    try:
        smtp_server = smtplib.SMTP(smtp["server"],smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as err:
        print("Error: An error with the email has occured:", err)


#This is the location of the source
source_file = backupcfg.SourceFiles()
#This is the location of the destination directory
destination_dir = backupcfg.DestinationFolder()

#The config file will return False if an argument inputted into the CLI is not supported
if source_file == "Invalid CLI Argument: No source file defined":
    err = current_datetime + " [FAILED] TypeError - The argument entered into the command line is not supported."
    print(err)
    logger.error(err)
    SendEmail(err)
    quit()

#Check if the source can be found
if pathlib.Path(source_file).exists() == False:
    err = current_datetime + " [FAILED] FileNotFoundError - The source file could not be found: '" + str(source_file) + "'"
    print(err)
    logger.error(err)
    SendEmail(err)
    quit()

#Convert the source location using the PurePath class
source_loc = pathlib.PurePath(source_file)

#If the source is a directory, only copy the name. If the source is a file, extract the stem (file name) and suffix (file type)
if pathlib.Path(source_loc).is_dir():
    source_name = source_loc.name
    source_type = ""
else:
    source_name = source_loc.stem
    source_type = source_loc.suffix

#Check if the destionation directory can be found
if pathlib.Path(destination_dir).exists() == False:
    err = current_datetime + " [FAILED] FileNotFoundError - The backup folder could not be found: '" + str(destination_dir) + "'"
    print(err)
    logger.error(err)
    SendEmail(err)
    quit()

#Create the final location of the file to be backed up, while appending the file name with the time of the backup
destination_loc = destination_dir + "/" + source_name + "_backup_" + current_datetime + source_type


#Print the source location and the backup destination into the terminal to show the user
print("Source location :", source_loc)
print("Destination location :", destination_loc)

#Finally, attempt to copy the source into the destination
try:
    if pathlib.Path(source_loc).is_dir():
        shutil.copytree(source_loc, destination_loc)
    else:
        shutil.copy2(source_loc, destination_loc)
    print("[SUCCESS] The file has sucessfully been backed up at " + str(current_datetime))
    success_info = current_datetime + " [SUCCESS] '" + str(source_loc) + "' has been backed up succesfully to '" + str(destination_loc) + "'"
    logger.info(success_info)
except Exception as err:
    fail_info = current_datetime + " [FAILED] An error has occured: " + str(err)
    print(fail_info)
    logger.error(fail_info)
    SendEmail(fail_info)