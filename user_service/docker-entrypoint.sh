#!/bin/bash

sleep 2

echo "Apply database migrations"
flask --app run db init
flask --app run db migrate -m "Initial Migrations"
flask --app run db upgrade

echo "Running Server"
python run.py