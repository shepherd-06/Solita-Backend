# Dev Academy 2023 - Solita

## Requirements

This project has been developed on MacOS and tested on Ubuntu 22.04 LTS, and `python3.10`. We will need `python3.*`, `postgreSQL` database pre-installed. [Here](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart) is a quick guide on how to install and create basic user on PostgreSQL.

### Steps (All commands are for Unix/macOS system only)

### Installing and Activating the VirtualEnv

1. Install python virtualenv package: `python3 -m pip install --user virtualenv`

2. Create a `virtualenv`: `python3 -m venv path/to/env`

3. Activate the virtualenv: `source path/to/env/bin/activate`

4. Confirm if `env` has been activated: `which python
`, it should show `.../path/to/env/bin/python`

5. If all's good, run this command to install the requirements packages from the `requirements.txt` file: `pip install -r requirements.txt`.

### Creating Env file

There's a `.env.EXAMPLE` in the BASE directory.

Create a copy of the said file and name it `.env`. There should be some variables in the `.env` file. We will need to fill them up. Without them the project won't work.

After setting up the `.env` file, run `python manage.py runserver`. It should run successfully and will duly notify that there are multiple missing migrations.

### Running the Migration

Now we are going to apply all the migrations by simply running `python manage.py migrate`. All migrations is going to be applied and the project is good to go!

### Download the CSV file on your machine

Two more small things to complete. We need to download the base csv file from a URL.

1. Create a directory `static` in the BASE directory, `mkdir static`.
2. [TODO] Download the file using curl. Add commands later.

### Upload CSV data into database.
