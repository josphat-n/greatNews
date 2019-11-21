
# Project Name: greatNews

# Name of author
Josphat Njoroge. <br>
Email: josphatnjoroge254@gmail.com

# Project Description
This application allows a user to view several sources of news articles. The user can then select the source, and navigate to view all the articles under that source name or domain.<br> 

Under a particular article, the user is able is see an image related to the news article, the topic and a description of the news article. The date of creation of the article is also visible. When a user is interested in any particular topic, they can read about it directly from the host url via the click of a button.<br>

The web application manages to do so by consuming an API (newsapi.org). By the use of urllib functionality, the application can loop through the jason format data, convert it to python dictionaries and thereafter loop through the list of objects returned as news source or news articles. 

# Development Methodology
Both BDD and TDD were used, with Bdd determining what test cases were designed and implemented. In a summary, this is the bdd: <br>

Given a user wants to read news via this application, when they interract with the app, they will see all the news sources and then they can click on the source that they are interested in.<br>

Given that the user has already clicked on a news source, then they can view all the news articles of that source and when they want to read more on a particular topic, then they can click on the "read more" button and navigate to the source url.

# Live-link 
The project is live at: https://jn-greatnews.herokuapp.com

# Technology used
1. Python flask.<br>
2. Some third party modules such as Jinja2 and gunicorn.

# Setup Instructions
A user may interact with the app that is hosted in the live-link as indicated above, and in that case no setup is required but a functioning web-browser and internet connection.<br>

To run the application in a local machine, the basic requirement is to have python installed on the local machine that you are working with. If not, install python by running the following commands consequtively via terminal: "$ sudo add-apt-repository ppa:jonathonf/python-3.6", "$ sudo apt-get update" and finally "$ sudo apt-get install python3.6". Confirm that the intallation was successful by typing the following command  $ python3.6 <br>

If python is up and runnning, next you need to install some third party modules. All the other required modules are as indicated in the requirements.txt file available in this repo.

### License
MIT &copy; Josephat Njoroge <br>
Anyone is free to fork, reuse, upgrade or do whatever partains this program without a prior request for permission.