# Config file for 'backup.py'
import sys

def SourceFiles():
    #This is the default source file to backup, if no arguments were specified in terminal OR if 'job1' was specified 
    if "job1" in sys.argv or len(sys.argv) <= 1:
        # Default = "/home/ec2-user/environment/ICTPRG302Assessment/Backup_Program/text.txt"
        return "/home/ec2-user/environment/ICTPRG302Assessment/Backup_Program/test_files/text.txt"
        
    elif "job2" in sys.argv:
        return "/home/ec2-user/environment/ICTPRG302Assessment/Backup_Program/test_files/foldertest"
        
    elif "job3" in sys.argv:
        return "/home/ec2-user/environment/ICTPRG302Assessment/Backup_Program/test_files/testpython.py"
        
    else:
        #The config file will return False if an argument inputted into the CLI is not supported
        return "Invalid CLI Argument: No source file defined"


def DestinationFolder():
    # Default = "/home/ec2-user/environment/ICTPRG302Assessment/Backup_Program/backups"
    return "/home/ec2-user/environment/ICTPRG302Assessment/Backup_Program/backups"
    
    
def LogFileLocation():
    # Default = "/home/ec2-user/environment/ICTPRG302Assessment/Backup_Program/backup.log"
    return "/home/ec2-user/environment/ICTPRG302Assessment/Backup_Program/backup.log"
    
def EmailDetails():
    apikey = "dd3e028f3beac83d8ace214e5effbd87"
    secretkey = "5745ef4fd95a7585283f4a3677e3f65f"
    
    return {
        "sender": "30027143@students.sunitafe.edu.au",
        "recipient": "jwellis.stein@gmail.com",
        "server": "in-v3.mailjet.com",
        "port": 587,
        "user": apikey,
        "password": secretkey}