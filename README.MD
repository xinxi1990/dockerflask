# 背景
使用python3 + flask + gunicorn + docker技术快速搭建后端FTP服务


## 创建虚拟环境
```angular2html
sudo easy_install pip
 
pip install virtualenv
 
virtualenv -p /usr/bin/python3 --no-site-packages venv 创建虚拟环境
 
source venv/bin/activate  激活虚拟环境
 
deactivate 退出虚拟环境
```

# 本地调试
```
python3 manage.py runserver
```

# gunicorn运行命令
```
gunicorn -w 1 -b 0.0.0.0:5000 manage:app -D
```

# docker构建
```angular2html
docker build -t docker_flask:v1 .
```

# docker运行
```angular2html
docker run -d -p 5000:5000 -v ${home}/files:/files  docker_flask:v1
```


# 创建数据库
```angular2html
python3 manage.py shell

from main import db

db.create_all()
```