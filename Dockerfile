FROM node:latest as nodebuild
WORKDIR /node/open-bar
COPY client/ ./
RUN npm install 
RUN npm install -g rollup 
RUN npm run build

FROM python:3.9.1-alpine
WORKDIR /code
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY --from=nodebuild /node/open-bar ./client
EXPOSE 5000
COPY . .
CMD ["flask","run"]