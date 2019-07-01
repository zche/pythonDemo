FROM python:3.7-alpine
ADD . /code
WORKDIR /code
#RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  --trusted-host pypi.tuna.tsinghua.edu.cn -r requirements.txt
CMD ["python3", "./helloworld.py"]