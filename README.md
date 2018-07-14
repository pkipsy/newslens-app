# newslens-app

<p align="center"><img src="https://github.com/pkipsy/news-lens/blob/master/docs/images/newslens.png?raw=true" width=75%></p>

The AWS-hosted web application behind [news-lens.online](http://news-lens.online/). The front-end was built with HTML, CSS, Bootstrap, and Flask. The back-end runs on NGINX and Gunicorn.

## Quick Guide to File Structure

### Flask
* The [init.py](https://github.com/pkipsy/newslens-app/blob/master/app_folder/__init__.py) file creates the Flask application object. 
* The [routes.py](https://github.com/pkipsy/newslens-app/blob/master/app_folder/routes.py) module defines the Flask view functions.

### Backend
* The [sandbox.py](https://github.com/pkipsy/newslens-app/blob/master/app_folder/sandbox.py) file identifies the input URL, classifies it, and generates recommended articles to display.
* The [scattertext_url.py](https://github.com/pkipsy/newslens-app/blob/master/app_folder/scattertext_url.py) file produces the interactive visualization.

### HTML Templates
* The [base.html](https://github.com/pkipsy/newslens-app/blob/master/app_folder/templates/base.html) file contains the site design in Bootstrap.
* The [index.html](https://github.com/pkipsy/newslens-app/blob/master/app_folder/templates/index.html) file is responsible for the initial page load.
* The [results.html](https://github.com/pkipsy/newslens-app/blob/master/app_folder/templates/results.html) file specifies how the output is presented.
