# Helsinki City Bike App (Backend)

## Project Description

This is the pre-assignment for Solita Dev Academy Finland 2023. This project uses dataset from Helsinki Region Transport (HSL). This project shows the list of stations HSL has and a front-end to view all the journey's to and from said stations. Detailed feature list is [here](https://github.com/shepherd-06/Solita-Backend#feature-list).

Backend (Deployed): <https://test.ibtehaz.xyz/ops/>

Full list of end points are given [here](https://github.com/shepherd-06/Solita-Backend#api-end-points)

Frontend (Github Repo): <https://github.com/shepherd-06/Solita-FrontEnd>

Frontend (Deployed): <https://jolly-platypus-a9a828.netlify.app/>

## Requirements

This project has been developed on MacOS and tested on Ubuntu 22.04 LTS, and `python3.10`. We will need `python3.*`, `postgreSQL` database pre-installed. [Here](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart) is a quick guide on how to install and create basic user on PostgreSQL. On MacOS, I have used `PostgreSQL 15` to test and on Ubuntu 22.04 LTS (server), it's `PostgreSQL`.

### Pre-Checklist

This `readme` file will not cover the installation phase of them. I have already taken it into account that they are pre-installed into the system and up-and-running.

* Check the current version of `python3` by running, `python3 --version`. Anything above `python3.5` should be fine (I think). This project used `Python 3.10.6` for both development phase and deployment phase.

* Check if PostgreSQL has already been installed and up-and-running.

* Install Pip; if it's not present.

    Ubuntu: `sudo apt install python3-pip`

    MacOS: `curl https://bootstrap.pypa.io/get-pip.py | python3`

    I didn't test the command for MacOS, pip's already installed in my system.

* (Additional) Check if your favorite server (nginx) is already installed and up-and-running.

### Steps (All commands are for <u>Unix/macOS System Only</u>)

First clone down this repository.

### Installing and Activating the VirtualEnv

1. Install python virtualenv package:

    For MacOS: `python3 -m pip install --user virtualenv`

    For Ubuntu/Debian System: `apt install python3.10-venv`

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

Now we are going to apply all the migrations by simply running:

```bash
python manage.py migrate
```

All migrations is going to be applied and the project is good to go!

### Download the CSV file on your machine

We need to download the base csv file from a URL.

1. Now we are going to download all the `csv` files using some `wget` magic. General format of the command is `wget URL -O filename`.

    1. Download the dataset from Helsinki Region Transport’s (HSL) of city bicycle stations:

    ```bash
    wget https://opendata.arcgis.com/datasets/726277c507ef4914b0aec3cbcfcbfafc_0.csv -O helsinki_station_list.csv
    ```

    2. Download three datasets of Journey data

        ```bash
        wget https://dev.hsl.fi/citybikes/od-trips-2021/2021-05.csv -O 2021-05.csv
        ```

        ```bash
        wget https://dev.hsl.fi/citybikes/od-trips-2021/2021-06.csv -O 2021-06.csv
        ```

        ```bash
        wget https://dev.hsl.fi/citybikes/od-trips-2021/2021-07.csv -O 2021-07.csv
        ```

    It's important that all the csv files have the correct name and downloading inside the `static` folder in the root directory. Otherwise, django won't be able to upload the data to server.

### Upload CSV data into database

Before running the server, you need to insert the data from the csv files. You will need to run both of these commands from the root directory of the project folder.

1. Run this from the root project directory to insert all the station data.

```bash
python3 manage.py shell < ops/scripts/script_stations.py
```

2. Now run this command to insert all the journeys. This will take a while.

```bash
python3 manage.py shell < ops/scripts/script_rides.py
```

For both these script, you will be able to see the progress and error on the terminal screen.

### Deploy

* To test locally,

    ```bash
    python3 manage.py runserver
    ```

    if you want to specify a port, you can do so

    ```bash
    python3 manage.py runserver <PORT>
    ```

* To test in detached mode/to deploy in server:

    ```bash
    nohup python3 manage.py runserver &
    ```

    All the outputs will be logged in `nohup.out` file. This part is <b> NOT </b> mandatory. I do it this way, do it however you like.

-----------

## API End Points

1. Get Station List:

`https://test.ibtehaz.xyz/ops/get_station/?page=1`

URL Parameter: `page`, default to 1

This end points sends the data in ascending order based on `station_id` (from the csv file). Items in pagination is fixed at this moment, 10 per request.

2. Get Single Station Data:

`https://test.ibtehaz.xyz/ops/station/?station_id=<station_id>`

URL Parameter (Mandatory): `station_id`.

This is a <b> <u>mandatory</u></b> parameter.

This API return the station data along with number of journey's started from this station and ended at this station.

3. List of Journey:

`https://test.ibtehaz.xyz/ops/get_journey/?page=1`

URL Parameter: `page`. Defaults to 1.

20 entries will be sent in each request and this is fixed at this moment. All the data will be sent in ascending order based on departure time.

## Technology Choice

This project used `Django` for backend and `postgreSQL` to store the data. I am familiar with both of these tech, so I choose them.

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
* [Completed] Running backend in Cloud
* [TODO] Implement E2E tests
* [TODO] Create UI for adding journeys or bicycle stations

-----------

Hyva! Happy hacking!
