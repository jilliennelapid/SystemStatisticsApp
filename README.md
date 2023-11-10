# SystemStatisticsApp
Python tkinter program implementing fastapi and routing to push information about a system's CPU, disk, and memory usage.

## tools_config
    * Contains the drive path for macOS to the disk.
    * Put into a separate file so that it can be changed for the respective OS

## remote_tools.py
    * Contains the methods that attain the percent usage values of the CPU, disk, and memory.
    * Methods are contained in a class called Retrieval
    * Uses the library psutil and its integrated methods.
    * Reads the data from tools_config and parses for just the drive path.

## remote_api.py
    * Imports the class Retrieval from remote_tools.py.
    * Imports the module fastapi for the use of fastAPI and APIRouter.
    * Instantiates an objecty app from fastapi.
    * Contains decorated methods from Retrieval such that they route information to localhost:8000
    

## system_monitor.py
    * Contains the methods to GET the data from routing.
    * Contains the main function that contains the tkinter GUI.  
