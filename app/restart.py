import os

os.system("killall -9 uwsgi")
os.system("nginx -s stop")
os.system("nginx")
