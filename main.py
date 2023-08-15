from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "Hello world"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}