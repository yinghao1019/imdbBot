<h1 aling="left">Imdb_prac</h1>
<p >ImdbBot is  a  web application that receive & reply  message  from line.This web application is used</p>

## **Project Articture**
### **Main part & flow**
![IMDB lineBot project articture](https://i.imgur.com/pyczZFX.jpg)

* LinePlatform : Used to send HTTP POST rquest with webhook event object to web server.

* Django web application/LineReply view: verify the signature in the x-line-signature request header to <br>
                                        confirm Lineplatform.And use Line message API for reply text sentiment message.

* GCP endpoint : Use GCP vertex ai with custom docker container to process request that come from django web view.


### **Built with**
* Django
* GCP Vertex Endpoint API
* Heroku
* Ngrok

<h1 aling="left">Getting started</h1>

#### **Prerequisites**
* **Heroku** : for create account & app,see this [doc](https://devcenter.heroku.com/articles/git#prerequisites-install-git-and-the-heroku-cli)

* **Google cloud Service** : See [doc](https://cloud.google.com/vertex-ai/docs/predictions/getting-predictions) for how to build endpoint to serve prediction.
* **Django**
* **LineBot offical channel** : build offical account
#### **Installation**

1. clone this repository

   ```bash
   git clone https://github.com/yinghao1019/imdbBot.git

   ```
2. Modified value of LINE_CHANNEL_SECRET & ACCESS TOKEN in project base setting module


### **Usage**
#### **Locally**
1. set Environment varaible

    ```bash
    export PROJECT_ID=${your project id}
    export ENDPOINT_ID=${your endpoint id}
    export Location=${your location}
    export GOOGLE_APPLICATION_CREDENTIALS=${your crendential path}
    ```

2. get ngrok authentication

    ```bash
    ./ngrok authtoken ${your secret key}
    ```
    And activate it with 8000 port.

    ```bash
    ./ngrok http 8000
    ```
3. cd your project root dir and activate local web server
    ```bash
    python manage.py runserver
    ```

4. copy https url that ngrok provided to Line webhook url in your bot message api.



#### **Production**
1. get heroku authentication
    ```bash
    heroku login
    ```
2. set Environment
    ```bash
    heroku config:set DJANGO_SETTINGS_MODULE=imdbBot.settings.production
    heroku config:set PROJECT_ID=${your_project_id}
    heroku config:set LOCATION=${location}
    heroku config:set ENDPOINT_ID=${your_endpoint_id}
    heroku config:set GOOGLE_APPLICATION_CREDENTIALS=${your crendential path}
    ```

3. push to your heroku app

4. fill **${your_heroku_domain}/message/reply** to Bot weebhook url


## **DEMO**
Use linebot to get movie review's sentiment <br>
Offical line account : @989mavgh

![Demo](https://i.imgur.com/0Z6UXX6.jpg)


## **Learn More**
Know how to deploy & train model with custom container on GCP,see below link<br>
1. [Deploy trained model service with Vertex Ai](https://github.com/yinghao1019/imdb_infer)<br>
2. [Train custom model on Vertex AI](https://github.com/yinghao1019/imdb_prac)<br>

## **Contact**
Ying Hao Hung-1104137203@gmail.com <br>
Project link : https://github.com/yinghao1019/imdb_prac



