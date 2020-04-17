[![Build Status](https://travis-ci.com/mkud/test_python_vin.svg?branch=master)](https://travis-ci.com/mkud/test_python_vin)

# test_python_VIN project

## task

Simple task description:
* create a simple REST service capable of retrieving data for one Vehicle Identification Number (VIN); 
* access to the REST server response that you will need to consume;
* then response JSON, with modified data from the main REST server.

Full task description you can find [here](TASK.md) 

## description of the project

REST service return HTTP 200 if all OK + JSON-object with the asked data.

REST service return HTTP 500 if any error + JSON-object with the error description.

Format of the JSON error:

{"error": `string with the error text from our REST service`,\
"internal_error": `string with the error text from the python exception`,\
"code": `integer code of the error`}

List of errors:

| Http code | code       | description                                                                                                                                  |
|-----------|------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| 500       | 1          | Unknown error. You can to understand what happened by "error" and "internal_error" parameters.                                               |
| 500       | 2          | This error occurs when the service has problems accessing the main server. for example, the URL of the main server is incorrectly specified. |
| 500       | 3          | This error occurs when a timeout is triggered for access to the main server (now 10 seconds).                                                |
| 500       | 4          | This error occurs if the main server returned a non-JSON response.                                                                           |
| 500       | 5          | This error occurs if the returned fields do not have the required fields.                                                                    |


## content description

* `test_python_vin` - Python eclipse project (the main solution):
    * `main.py` - the main solution Flask project;
    * `test.py` - the unittest module for testing the main module;
    * `test_data.py` - the test data for testing the main module, contains answers of the mock web-server and the target responses of our tested server;
* `docker` - contains Dockerfiles for creating containers for the main solution and test container.
* `1_make_docker_server.sh` - compile Docker container of the server from the Dockerfile;
* `2_make_docker_test.sh` - compile Docker container of the test module from the Dockerfile;
* `3_run_docker_server.sh` - run docker image of the server. you don't need to precompile the project by `1_make_docker_server.sh`;
* `4_run_docker_test.sh` - run docker image of the test module. you don't need to precompile the project by `2_make_docker_test.sh`;
* `5_stop_docker_server.sh` - stops an already running main container. You can also use Ctrl+C if you opened `3_run_docker_server.sh`;
* `docker_clean_ALL.sh` - be careful with this script. It remove all images of all containers on your computer. 

## testing part description

To test the project I created a Mock Web Server. Flask project get information from it. The flask does not create a connection through TCP. This type of testing was chosen on the recommendation of the Flask developers.

## how to use

* The most recommended way to use this project is by Docker. Just run `3_run_docker_server.sh`.  To access the test data you can run the following command: `wget http://127.0.0.1/get_info_by_vin/VSSZZZ6JZ9R056308`;
* if port 80 is busy on your host machine (or you plan to use another port), then change the file `3_run_docker_server.sh` in the part `... -p 80:80 ... ` to, for example, `... -p 5000:80 ... `;
* you don't need to precompile the project by `1_make_docker_server.sh`. I had uploaded the main container and the test container in the Docker Hub, so these containers will download from there;
* this project uses this REST-server with this URL `https://s3-eu-west-1.amazonaws.com/coding-challenge.carfax.eu/`. If you want to use another one you should define it in the `Dockerfile` by `TEST_SERVER_URL` parameter;
* when you start the test container (by `4_run_docker_test.sh`), everything happens inside that one. No TCP ports are out.
* if you decide to use this project as a standalone app, you need to know about these dependencies (Python modules) (you can install them by pip):
    * Flask;
    * ujson;
    * requests;
    * developed on Python3.
 
