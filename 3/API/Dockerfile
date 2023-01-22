FROM redis:latest
RUN apt -y update
RUN apt -y install python3 python3-pip curl
RUN pip install redis flask

RUN mkdir /app
COPY app.py /app/app.py
COPY start.sh /app/start.sh
EXPOSE 5000
CMD ["/bin/bash","/app/start.sh"]
