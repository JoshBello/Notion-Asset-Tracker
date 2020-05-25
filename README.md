## Notion Based Portfolio Tracker 
### Using Python,  Cloud Functions,  Pub/Sub and Cloud Scheduler 

![](notion.table.gif)

## Background:

After recently switching from Trello to Notion as my primary productivity tool, I wanted to see what was possible with Notion's API. A basic portfolio tracker seemed like a good start. 

This project uses `notion-py` which is an unofficial Python client for Notions API. For the current asset values, I'm using `yfinance` which allows easy access to data from Yahoo Finance. One thing to note with this is that the ticker values used have to correspond with values on the platform. 

## Google Cloud Platform Architecture:

<img src="flow.png" width="80%">

# Getting Started: 

## 1. Updating Variables: 

The following variabels require updating:

```
token_v2 =
page_url =
table_url =
```

## 2. Setting up Cloud Functions and Pub/Sub: 

<img src="cloud-functions.gif" width="60%">

## 3. Setting up Cloud Scheduler: 

<img src="scheduler.gif" width="60%">
