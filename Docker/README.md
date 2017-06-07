
**Steps to run docker image by pulling it from Docker hub:**

 1. You can pull docker image from docker hub by running following command:
>> docker pull bhanuteja/forecastdocker:latest

 2. To run the application on local host run the following command:
>> docker run -d -p 8081:80 bhanuteja/forecastdocker:latest

 3. Now go  to  :   http://localhost_IP:8081/  to verify the result.
The web application will run on local host with port number 8081 according to the given command.

			(or) 


**Steps to run uploaded Docker Image:**

You can download docker image from following URL:
https://drive.google.com/open?id=0B6Y1fvNRH6NwZHVGdjU5TG14UDA

 1. Load the docker image uisng the following command:
>> docker load -i bhanu_docker.tar.gz

 2. Now the docker image is loaded and returns the <ImageID>

 3. To test the application on local host run the following command:
>> docker run -d -p 8081:80 ImageID

 4. Now go  to  : http://localhost_IP:8081/  to verify the result.
The web application will run on local host with port number 8081 according to the given command.

 5. To stop the docker using following command:
>>docker stop containerID


**Dockerfile:**

FROM tiangolo/uwsgi-nginx-flask:flask-index

COPY ./app /app




**REST API:**  bhanurangaraju.pythonanywhere.com/weather/forecast/<DATE>








**Steps followed to create image:**

 1.Launched ubuntu instance and logged into it with user credentials.

 2.Install docker using the command: 
 
	>> sudo apt-get install docker

 3.Install git in the instance using below step: 
 
 	>> sudo apt-get install git

 4.Cloned my git project using the url as follows: 
 
 	>> git clone https://github.uc.edu/rangarba/Cloud-Computing/tree/master/UI 

 5.Created a docker hub account.

 6.Command to login to account:
 
    >>docker login http://hub.docker.com -u rangarba

 7.Command to search for base docker image:
 
    >>docker search "nginx python flask"

 8.Command to pull docker image:
 
    >>docker pull tiangolo/uwsgi-nginx-flask

 9.Create dynamic content as main.py which is also the main application.

 10.Command to create a uwsgi.ini file for Nginx - uwsgi:
 
    >> cat > uwsgi.ini
    [uwsgi]
    module = main
    callable = app
    
 11.Command to create Dockerfile:
 
    >> cat > Dockerfile
    FROM tiangolo/uwsgi-nginx-flask:flask-index
    COPY ./app /app

 12.Command to build Docker Image:
 
    >> docker build -t dockerforecast .

 13.Command to run Docker Image:   
 
    >> docker run -d --name Docker_bhanu -p 80:80 dockerforecast 
 
 14.Commands to push to the repository:
 
    >> docker commit <containerID> rangarba/<name>:latest
    
    >> docker push rangarba/<name/containerID>:latest

 15.Command to save docker images and create .tar file and zip it:
 
    >> docker save <image id/name> | gzip > bhanu_docker.tar.gz

