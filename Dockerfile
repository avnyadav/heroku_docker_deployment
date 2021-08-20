FROM jjanzic/docker-python3-opencv:latest

RUN pip3 install --upgrade pip 

WORKDIR /
COPY . /
RUN pip3 --no-cache-dir install -r requirements.txt

#EXPOSE 5000

#ENTRYPOINT ["python3"]
#CMD ["main.py"]
#RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
