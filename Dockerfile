FROM python:3-onbuild

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

COPY . /app

EXPOSE 3000

#ENTRYPOINT [ "python" ]

CMD [ "python3", "flaskgui.py" ]