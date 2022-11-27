# The Big Mac Index

## Table of contents

- [General info](#general-info)
- [Setup](#setup)
  - [Installing dependencies](#installing-dependencies)
  - [Run the project](#run-the-project)

## General info

Brief project information:

- Extracted country codes from the CSV file to nextly use them in requests to API to obtain data from [The Economist - Big Mac Index](https://data.nasdaq.com/data/ECONOMIST-the-economist-big-mac-index/usage/quickstart/api)
- Saved data locally to make data visualization within PowerBI with the top 5 countries with the highest Big Mac index in July
  2021
- Uploaded the data to AWS S3 within the boto3 client. Implemented email notification that data is in S3
- The whole application is divided into separate modules to group related code to make it easier to understand and use. Everything
  executes in the main.py file which imports functionality from the scripts from the src folder

## Setup

These are the crucial steps to configuring and running the project.

### Installing dependencies

```bash
# To create a folder for downloaded CSV files from API
$ mkdir bigmac_index

# To download all the necessarily Python packages needed for the project
$ pip install -r requirements.txt
```

### Run the project

```python
python .\main.py
```
