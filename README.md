# The Big Mac Index

## Table of contents

- [General info](#general-info)
- [Setup](#setup)
  - [Installing dependencies](#installing-dependencies)
  - [Run the project](#run-the-project)

## General info

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
