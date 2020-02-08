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
export mail_password="xxx"

python3 manage.py runserver
```

# gunicorn运行命令
```
gunicorn -w 1 -b 0.0.0.0:5000 manage:app -D
```

# uwsgi运行命令
```
pip install uwsgi

uwsgi --http :9999 -s /tmp/app.sock --manage-script-name --mount /test=route:app

uwsgi --http :9999 -s /tmp/app.sock --manage-script-name --mount /=main:app
上下等价
uwsgi --http :9999 -s /tmp/app.sock --manage-script-name --mount /=manage:app
# manger应用

uwsgi --ini uwsgi.ini -d /tmp/uwsgi.log
# 使用配置文件
pkill -f -9 uwsgi
# 停止 uwsgi
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

python3 manage.py create_db

```

# supervisor
```angular2html
sudo supervisord -c supervisord.conf

sudo supervisorctl status
```

# nginx
```bash
docker pull nginx 

docker run --name nginx -p 8070:80 -v /Users/xinxi/Documents/sndd/dockerflask/nginx/nginx.conf:/etc/nginx/nginx.conf -v /Users/xinxi/Documents/sndd/dockerflask/nginx:/usr/share/nginx/html --restart always -d nginx
```


# 生成本地依赖
```bash
pip freeze > requirements.txt

pip install pipreqs

pipreqs ./
```
  
