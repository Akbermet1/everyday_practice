from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


list_of_classes = ["Security of Computer Systems", "Computer Graphics",
                   "Team Project", "Basics of Enterpreneurship and Management"]


@app.get("/classes/")
async def root():
    return list_of_classes

