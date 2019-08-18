FROM node:9.6.1

LABEL version="1.0"
LABEL description="Web app Mongo-Python_flask-vueJs"
LABEL maintainer="Andres Felipe Villada M - avillada@eafit.edu.co"

ARG PORT=5000
ENV PORT $PORT

WORKDIR /pythonApp
COPY . ./

RUN cd cliente && npm install --test
RUN cd cliente && npm run build
RUN apt-get  update
RUN apt-get install -y python-pip
RUN apt-get install -y python-waitress
RUN pip install -U flask-cors
RUN pip install pymongo

EXPOSE 5000

CMD cd server && touch log.txt && python main.py
