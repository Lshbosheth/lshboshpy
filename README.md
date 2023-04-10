# lshboshpy
本地启动  
uvicorn main:app --reload  
服务器启动  
gunicorn -w 4 -b 0.0.0.0:3000 main:app