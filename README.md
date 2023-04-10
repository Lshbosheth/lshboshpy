# lshboshpy
本地启动  
uvicorn main:app --reload  
服务器启动  
gunicorn -w 4 -b 127.0.0.1:3000 main:app  
虚拟环境内包生成文件  
pip freeze >requirements.txt   