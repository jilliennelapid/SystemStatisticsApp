import psutil
import re

# To get the disk path, we read from tools_config
with open("tools_config") as f:
    read = f.read()
# The text from the file is parsed such that only the part of the
# string that is surrounded by quotes is saved.
reread = re.findall(r'"(.*?)"', read)
# Translates the data parsed from a list to a variable as a string
path = ""
for x in reread:
    path = x


# class Retrieval contains all the methods for retrieving data from the system.
# the module of psutil is mainly used to acquire the values.
class Retrieval:
    # method to retrieve statistics for cpu
    def getCPU(self):
        return psutil.cpu_percent(1)

    # method to retrieve statistics for disk
    def getDisk(self):
        # Uses the parsed data of the file path to get to the disk using psutil.
        # specifically returns the percent usage value from the psutil method
        disk = psutil.disk_usage(path)
        return disk.percent

    # method to retrieve statistics for memory
    def getMemory(self):
        return psutil.virtual_memory()[2]

