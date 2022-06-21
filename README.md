# The Big Mac Index

## Table of contents

- [General info](#general-info)
- [Setup](#setup)
  - [Installing dependencies](#installing-dependencies)
  - [Run the project](#run-the-project)

## General info

The whole project consists of several steps.

1. Download data from [The Economist - Big Mac Index](https://data.nasdaq.com/data/ECONOMIST-the-economist-big-mac-index/usage/quickstart/api) and save it on AWS S3.
2. Implement email notification that data is in S3.
3. Data visualization within PowerBI with the top 5 countries with the highest Big Mac index in July 2021.

This project is about extracting data from [The Economist - Big Mac Index](https://data.nasdaq.com/data/ECONOMIST-the-economist-big-mac-index/usage/quickstart/api) within URL API and uploading it to the AWS S3.

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
