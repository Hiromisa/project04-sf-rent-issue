# project: San Francisco rent issue

This is a project for Lede week4. I analyzed the rent trend in San Francisco and 20 metro areas in the U.S.
I use Zillow's Zillow Observed Rent Index (ZORI) and LinkedIn's Workforce Report for analysis.

## article based on this project
https://docs.google.com/document/d/1X0ma1w4W_0ZairvO2Ng232b3qRNsSIYZp1JSkan75Fs/edit?usp=sharing

---
## Data
"Metro_ZORI_AllHomesPlusMultifamily_SSA.csv" come from [Zillow](https://www.zillow.com/research/data/)

This file contains a table that shows Metro areas and the U.S. rent index which called Zillow Observed Rent Index (ZORI) from 2014 to 2021, monthly.
I used seasonally adjusted data for my analysis.

I also used [LinkedIn's Workforce Report July 2021](https://economicgraph.linkedin.com/resources/linkedin-workforce-report-july-2021).
It shows migration trend for each metro area past year. 

I merged/filtered some data on them with Jupyter/pandas, then created new CSV files called "covid_impact_rent.csv" and "SanFranciscoZORI.csv".
"covid_impact_rent.csv" shows the rent increase/deccrease since May 2019. "SanFranciscoZORI.csv" shows ZORI of San Francisco.

I also analyzed rent trend by zipcode in San Francisco bayarea. 
For this analysis, I used "Zip_ZORI_AllHomesPlusMultifamily_SSA.csv", 
which downloaded from [Zillow](https://www.zillow.com/research/data/) and "bayarea_zipcodes.csv" which is the zipcode list of San Francisco Bay area.
I merged/filtered some data on them with Jupyter/pandas, then created new a CSV file titled "sfzip_rent.csv"

---
## Analysis
"rent_trend.ipynb notebook" contains my analysis for metro areas rent trend, written in Python. Relevant outputs can be found there.
"bayarea_focused_rent.ipynb" contains my analysis for metro areas rent trend, written in Python.  

---
## Reproducibility
The code running the analysis is written in Python 3 and requires pandas．

pandas for data loading and analysis

Jupyter to run the notebook infrastructure
