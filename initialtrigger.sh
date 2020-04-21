#!/bin/bash
curl https://covid.ourworldindata.org/data/owid-covid-data.csv > /Users/oliverbains/Documents/Important/COVIDTesting/owid-curl.csv
sleep 30
/Users/oliverbains/opt/anaconda3/bin/python /Users/oliverbains/Documents/Important/COVIDTesting/covid.py
echo "time to update dashboards"
