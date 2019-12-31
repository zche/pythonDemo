### 打包命令 会生成tar.gz格式的压缩包
python setup.py sdist
### 安装并记录所有安装的包
python setup.py install --record del.txt
### 删除所有安装的包
cat del.txt|xargs rm -rf


### 打包命令--这是一个扩展命令 bdist_wheel用于替换bdist_egg 
python setup.py bdist_wheel