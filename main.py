# Importing the framework
from fastapi import FastAPI


# Importing the routers
import routers.router_tasks



# Initializing the API
app = FastAPI(
    title="TacheSync",
    docs_url='/'
)

# Including routers dedicated to managing tasks
app.include_router(routers.router_tasks.router)




