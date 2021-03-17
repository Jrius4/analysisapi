source ./env/Scripts/activate
pip freeze > requirements.txt
uvicorn main:app --reload
git add . && git commit -m "%%%phraze 2%%%"