source ./env/Scripts/activate
pip freeze > requirements.txt
uvicorn main:app --reload