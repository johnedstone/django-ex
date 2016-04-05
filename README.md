# Openshift quickstart: Django

#### django-psql-redis-simple using the Origin Openshift VM
- This (master) currently is v3 merged into the master branch.  Simpler examples are in v1 and v2
- Notes from v4, work in progress:
    * django, openshift, postgresql, redis, celery
    * This works up to step 3, the feedback form, at https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/
    * The mail ends up in the celery pod, in /tmp, in a log file for the session.

- This is the a bit more complex than the original django-ex: django, openshift, postgresql, redis (just the pod), and including Windows and proxy information
- This version shows how to set the proxy in ```/etc/sysconfig/docker``` as well in the _template_

##### How to import a docker image and image stream - both of these two methods worked.  The second worked in the Windows env, that was proxy'd
- Put simply, it appears push creates the image stream 

    ```
   <as root>
   docker pull redis:2.8.19
   docker tag docker.io/redis:2.8.19 172.30.210.155:5000/openshift/redis:2.8.19
   docker push 172.30.210.155:5000/openshift/redis:2.8.19
   docker rmi -f 98706ddebd02 <remove image (id of redis pull and tagged image) to confirm it will be created in the build>
    ```

- This reference worked as well, but too complicated: http://www.opensourcerers.org/importing-an-external-docker-image-into-red-hat-openshift-v3/

    ```
    sudo docker pull redis:2.8.19
    sudo docker tag docker.io/redis:2.8.19 172.30.210.155:5000/openshift/redis:2.8.19

    <as root>
    oc login <admin>
    docker login -u admin -e a@b.com -p $(oc whoami -t) 172.30.210.155:5000
    docker push 172.30.210.155:5000/openshift/redis:2.8.19


    oc get is -n openshift |egrep redis <confirms image stream was created>
    docker rmi -f 98706ddebd02 <remove image (id of redis pull and tagged image) to confirm it will be created in the build>
    ```

##### Using the Origin Openshift VM on Windows and in a proxy'd environment
- Reference: https://www.openshift.org/vm/
  * Install Vagrant and Virtual Box for Windows
  * Instal 64 bit cygwin base plus openssh
- Open cygwin teminal, and make a dir to work in
- ```export PATH=/cygdrive/c/HashiCorp/Vagrant/bin:$PATH```
- export https_proxy=ip:port
- From the reference: ```vagrant init ....```
- From the reference: ```vagrant ssh ...```
- Once in the container, sudo su - add the following to /etc/sysconfig/docker and restart docker

    ```
    HTTPS_PROXY=https://ip address:port
    HTTP_PROXY=http://ip address:port
    NO_PROXY=172.30.210.155
    ```

- Continue to work, not as root, with the oc commands in the VM
- When finished, exit the VM and run ```vagrant suspend```
- When starting again, run ```vagrant resume```

### From the [cloned project](https://github.com/openshift/django-ex "django-ex")

This is a [Django](http://www.djangoproject.com) project that you can use as the starting point to develop your own and deploy it on an [OpenShift](https://github.com/openshift/origin) cluster.

The steps in this document assume that you have access to an OpenShift deployment that you can deploy applications on.

## What has been done for you

This is a minimal Django 1.8 project. It was created with these steps:

1. Create a virtualenv
2. Manually install Django and other dependencies
3. `pip freeze > requirements.txt`
4. `django-admin startproject project .`
3. Update `project/settings.py` to configure `SECRET_KEY`, `DATABASE` and `STATIC_ROOT` entries
4. `./manage.py startapp welcome`, to create the welcome page's app

From this initial state you can:
* create new Django apps
* remove the `welcome` app
* rename the Django project
* update settings to suit your needs
* install more Python libraries and add them to the `requirements.txt` file


## Special files in this repository

Apart from the regular files created by Django (`project/*`, `welcome/*`, `manage.py`), this repository contains:

```
openshift/         - OpenShift-specific files
├── scripts        - helper scripts
└── templates      - application templates

requirements.txt   - list of dependencies
```


## Local development

To run this project in your development machine, follow these steps:

1. (optional) Create and activate a [virtualenv](https://virtualenv.pypa.io/) (you may want to use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)).

2. Fork this repo and clone your fork:

    `git clone https://github.com/openshift/django-ex.git`

3. Install dependencies:

    `pip install -r requirements.txt`

4. Create a development database:

    `./manage.py migrate`

5. If everything is alright, you should be able to start the Django development server:

    `./manage.py runserver`

6. Open your browser and go to http://127.0.0.1:8000, you will be greeted with a welcome page.


## Deploying to OpenShift

To follow the next steps, you need to be logged in to an OpenShift cluster and have an OpenShift project where you can work on.


### Using an application template

The directory `openshift/templates/` contains OpenShift application templates that you can add to your OpenShift project with:

    oc create -f openshift/templates/<TEMPLATE_NAME>.json

The template `django.json` contains just a minimal set of components to get your Django application into OpenShift.

The template `django-postgresql.json` contains all of the components from `django.json`, plus a PostgreSQL database service and an Image Stream for the Python base image. For simplicity, the PostgreSQL database in this template uses ephemeral storage and, therefore, is not production ready.

After adding your templates, you can go to your OpenShift web console, browse to your project and click the create button. Create a new app from one of the templates that you have just added.

Adjust the parameter values to suit your configuration. Most times you can just accept the default values, however you will probably want to set the `GIT_REPOSITORY` parameter to point to your fork and the `DATABASE_*` parameters to match your database configuration.

Alternatively, you can use the command line to create your new app, assuming your OpenShift deployment has the default set of ImageStreams defined.  Instructions for installing the default ImageStreams are available [here](http://docs.openshift.org/latest/admin_guide/install/first_steps.html).  If you are defining the set of ImageStreams now, remember to pass in the proper cluster-admin credentials and to create the ImageStreams in the 'openshift' namespace:

    oc new-app openshift/templates/django.json -p SOURCE_REPOSITORY_URL=<your repository location>

Your application will be built and deployed automatically. If that doesn't happen, you can debug your build:

    oc get builds
    # take build name from the command above
    oc build-logs <build-name>

And you can see information about your deployment too:

    oc describe dc/django-example

In the web console, the overview tab shows you a service, by default called "django-example", that encapsulates all pods running your Django application. You can access your application by browsing to the service's IP address and port.  You can determine these by running

   oc get svc


### Without an application template

Templates give you full control of each component of your application.
Sometimes your application is simple enough and you don't want to bother with templates. In that case, you can let OpenShift inspect your source code and create the required components automatically for you:

```bash
$ oc new-app openshift/python-33-centos7~https://github.com/openshift/django-ex
imageStreams/python-33-centos7
imageStreams/django-ex
buildConfigs/django-ex
deploymentConfigs/django-ex
services/django-ex
A build was created - you can run `oc start-build django-ex` to start it.
Service "django-ex" created at 172.30.16.213 with port mappings 8080.
```

You can access your application by browsing to the service's IP address and port.


## Logs

By default your Django application is served with gunicorn and configured to output its access log to stderr.
You can look at the combined stdout and stderr of a given pod with this command:

    oc get pods         # list all pods in your project
    oc logs <pod-name>

This can be useful to observe the correct functioning of your application.


## Special environment variables

### APP_CONFIG

You can fine tune the gunicorn configuration through the environment variable `APP_CONFIG` that, when set, should point to a config file as documented [here](http://docs.gunicorn.org/en/latest/settings.html).

### DJANGO_SECRET_KEY

When using one of the templates provided in this repository, this environment variable has its value automatically generated. For security purposes, make sure to set this to a random string as documented [here](https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-SECRET_KEY).


## One-off command execution

At times you might want to manually execute some command in the context of a running application in OpenShift.
You can drop into a Python shell for debugging, create a new user for the Django Admin interface, or perform any other task.

You can do all that by using regular CLI commands from OpenShift.
To make it a little more convenient, you can use the script `openshift/scripts/run-in-container.sh` that wraps some calls to `oc`.
In the future, the `oc` CLI tool might incorporate changes
that make this script obsolete.

Here is how you would run a command in a pod specified by label:

1. Inspect the output of the command below to find the name of a pod that matches a given label:

        oc get pods -l <your-label-selector>

2. Open a shell in the pod of your choice. Because of how the images produced
  with CentOS and RHEL work currently, we need to wrap commands with `bash` to
  enable any Software Collections that may be used (done automatically inside
  every bash shell).

        oc exec -p <pod-name> -it -- bash

3. Finally, execute any command that you need and exit the shell.

Related GitHub issues:
1. https://github.com/GoogleCloudPlatform/kubernetes/issues/8876
2. https://github.com/openshift/origin/issues/2001


The wrapper script combines the steps above into one. You can use it like this:

    ./run-in-container.sh ./manage.py migrate          # manually migrate the database
                                                       # (done for you as part of the deployment process)
    ./run-in-container.sh ./manage.py createsuperuser  # create a user to access Django Admin
    ./run-in-container.sh ./manage.py shell            # open a Python shell in the context of your app

If your Django pods are labeled with a name other than "django", you can use:

    POD_NAME=name ./run-in-container.sh ./manage.py check

If there is more than one replica, you can also specify a POD by index:

    POD_INDEX=1 ./run-in-container.sh ./manage.py shell

Or both together:

    POD_NAME=django-example POD_INDEX=2 ./run-in-container.sh ./manage.py shell


## Data persistence

You can deploy this application without a configured database in your OpenShift project, in which case Django will use a temporary SQLite database that will live inside your application's container, and persist only until you redeploy your application.

After each deploy you get a fresh, empty, SQLite database. That is fine for a first contact with OpenShift and perhaps Django, but sooner or later you will want to persist your data across deployments.

To do that, you should add a properly configured database server or ask your OpenShift administrator to add one for you. Then use `oc env` to update the `DATABASE_*` environment variables in your DeploymentConfig to match your database settings.

Redeploy your application to have your changes applied, and open the welcome page again to make sure your application is successfully connected to the database server.


## Looking for help

If you get stuck at some point, or think that this document needs further details or clarification, you can give feedback and look for help using the channels mentioned in [the OpenShift Origin repo](https://github.com/openshift/origin), or by filling an issue.


## License

This code is dedicated to the public domain to the maximum extent permitted by applicable law, pursuant to [CC0](http://creativecommons.org/publicdomain/zero/1.0/).
