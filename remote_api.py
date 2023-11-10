from fastapi import APIRouter, FastAPI
from remote_tools import Retrieval

# Creating an instance of FastAPI() to have an accessible app for uvicorn.
app = FastAPI()
# Creating an instance of APIRouter() to allow routing.
router = APIRouter()
# Creating an instance of the Retrieval class from remote_tool
# so that the data retrieving functions can be used.
retrieve = Retrieval()

# Methods that establish that the sent information will be called by GET.
# Each method uses a function from the Retrieval class using the object retrieve.
# Each method is written to get the percent usage of either the CPU, disk, or memory.
# That value is returned and then routed to the url http://localhost:8000
@router.get("/cpu")
async def retrieve_cpu():
    cpuUsage = retrieve.getCPU()
    return cpuUsage

@router.get("/disk")
async def retrieve_disk():
    diskUsage = retrieve.getDisk()
    return diskUsage

@router.get("/mem")
async def retrieve_memory():
    memUsage = retrieve.getMemory()
    return memUsage

# includes the router into the app
app.include_router(router)