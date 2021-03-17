import os
import shutil
from fastapi import FastAPI,File,UploadFile
from fastapi.responses import FileResponse
from typing import List

app = FastAPI()
cwd = os.getcwd()


@app.get('/')
def index():
    return {'data':{'name':'kazibwe'}}

@app.get('/about')
def about():
    return {'data':'about page'}

@app.get("/farmer",responses={200:{'description':'picture of a man','content':{'image/jpeg':{'example':'No examplae. Just imagine a picture of a farmer.'}}}})
def farmer():
    img_path = 'assets/imgs/man.JPG'
    file_path = os.path.join(cwd,img_path)
    if os.path.exists(file_path):
        return FileResponse(file_path,media_type='image/jpeg',filename='farmer.jpg')
        # return FileResponse(file_path)
    return {'error':'file not found!'}

@app.post('/post_farmer/')
def post_farmer(
    name:str,files:List[UploadFile] = File(...)
            ):
            url = []
            for file in files:
                with open('assets/uploads/'+file.filename,'wb') as buffer:
                    shutil.copyfileobj(file.file,buffer)
                url.append(file)


            return {'name':name,'file':file,'url':url}
