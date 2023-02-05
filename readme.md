# Helsinki City Bike App (Backend)

## Project Description

This is the pre-assignment for Solita Dev Academy Finland 2023. This project uses dataset from Helsinki Region Transport (HSL). This project shows the list of stations HSL has and a front-end to view all the journey's to and from said stations. Detailed feature list is [here](https://github.com/shepherd-06/Solita-Backend#feature-list).

Backend (Deployed): [TODO Add URL]

Frontend (Github Repo): <https://github.com/shepherd-06/Solita-FrontEnd>

Frontend (Deployed): [TODO Add URL]

## Requirements

This project has been developed on MacOS and tested on Ubuntu 22.04 LTS, and `python3.10`. We will need `python3.*`, `postgreSQL` database pre-installed. [Here](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart) is a quick guide on how to install and create basic user on PostgreSQL. On MacOS, I have used `PostgreSQL 15` to test and on Ubuntu 22.04 LTS (server), it's `PostgreSQL`.

### Steps (All commands are for Unix/macOS system only)

### Installing and Activating the VirtualEnv

1. Install python virtualenv package: `python3 -m pip install --user virtualenv`

2. Create a `virtualenv`: `python3 -m venv path/to/env`

3. Activate the virtualenv: `source path/to/env/bin/activate`

4. Confirm if `env` has been activated: `which python`, it should show `.../path/to/env/bin/python`

5. If all's good, run this command to install the requirements packages from the `requirements.txt` file: `pip install -r requirements.txt`. This should install all the requirements file.

### Creating Env file

There's a `.env.EXAMPLE` in the BASE directory.

Create a copy of the said file and name it `.env`. There should be some variables in the `.env` file. We will need to fill them up. Without them the project won't work.

Here's the list of the variable from the `.env.EXAMPLE` file:

```text
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
SECRET_KEY=
```

After setting up the `.env` file, run `python manage.py runserver`. It should run successfully and will duly notify that there are multiple missing migrations.

### Running the Migration

Now we are going to apply all the migrations by simply running `python manage.py migrate`. All migrations is going to be applied and the project is good to go!

### Download the CSV file on your machine

Two more small things to complete. We need to download the base csv file from a URL.

1. Create a directory `static` in the BASE directory, `mkdir static`.
2. Now we are going to download all the `csv` files using some `wget` magic. General format of the command is `wget URL -O filename`.

    1. Download the dataset from Helsinki Region Transport’s (HSL) of city bicycle stations: `wget https://opendata.arcgis.com/datasets/726277c507ef4914b0aec3cbcfcbfafc_0.csv -O helsinki_station_list.csv`
    2. Download three datasets of Journey data

        `wget https://dev.hsl.fi/citybikes/od-trips-2021/2021-05.csv -O 2021-05.csv`

        `wget https://dev.hsl.fi/citybikes/od-trips-2021/2021-06.csv -O 2021-06.csv`

        `wget https://dev.hsl.fi/citybikes/od-trips-2021/2021-07.csv -O 2021-07.csv`

    It's important that all the csv files have the correct name and downloading inside the `static` folder in the root directory. Otherwise, django won't be able to upload the data to server.

### Upload CSV data into database

I have written two dummy views that will insert all the data into the database, it's a brute-force process, in my opinion. I didn't have enough time to covert this process into some simple scripts. This is a limitation of this version, for this phase.

You would need to configure our server (if you are testing on the server) to listen to `port 8000`, default django port, unless you want to change it to something else.

1. Send a CURL request to `http://localhost:8000/ops/<TODO>` to insert all the Station data from CSV to database. This will take couple of minutes.

2. Now, you will have to insert all the journey data into the database. Its going to take a while. `http://localhost:8000/ops/<TODO>`, send a GET request via CURL or hit that URL from your browser. Don't run this request multiple times because then every data will be inserted that many times. We don't want it to happen

It took me 20 minutes to populate the database, so get yourself some coffee and wait for it. Both of the requests will return a status. Again, this is a very bad way to populate data into the system. If I have time, I will update it.

### Deploy

Run `python3 manage.py runserver`. By default, Django will run the backend in `port 8000`. You can change to your port of choice by running `python3 manage.py runserver <PORT>`

-----------

## Technology Choice

This project used `Django` for front-end and `postgreSQL` to store the data. I am familiar with both of these tech, so I choose them. Besides, I love Django's ORM support.

-----------

## Feature List

### Data Import

* [Completed] Import data from the CSV files to a database or in-memory storage.

* [Completed] Validate data before importing.

* [Completed] Don't import journeys that lasted for less than ten seconds

* [Completed] Don't import journeys that covered distances shorter than 10 meters

### Journey List View

* [Completed] List Journeys
* [Completed] For each journey show departure and return stations, covered distance in kilometers and duration in minutes
* [Pagination] Pagination
* [TODO] Ordering per column
* [TODO] Searching
* [TODO] Filtering

### Station list

* [Completed] List all the stations
* [Completed] Pagination
* [TODO] Searching

### Single station view

* [Completed] Station name
* [Completed] Station address
* [Completed] Total number of journeys starting from the station
* [Completed] Total number of journeys ending at the station
* [TODO] Station location on the map
* [TODO] The average distance of a journey starting from the station
* [TODO] The average distance of a journey ending at the station
* [TODO] Top 5 most popular return stations for journeys starting from the station
* [TODO] Top 5 most popular departure stations for journeys ending at the station
* [TODO] Ability to filter all the calculations per month

### Additional Features

* [TODO] Endpoints to store new journeys data or new bicycle stations
* [TODO] Running backend in Docker
* [TODO] Running backend in Cloud
* [TODO] Implement E2E tests
* [TODO] Create UI for adding journeys or bicycle stations

-----------

Hyva! Happy hacking!
