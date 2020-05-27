## Notion Based Portfolio Tracker 
### Using Python,  Cloud Functions,  Pub/Sub and Cloud Scheduler 

![](notion.table.gif)

## Background:

After recently switching from Trello to Notion as my primary productivity tool, I wanted to see what was possible with Notion's API. A basic portfolio tracker seemed like a good start. 

This project uses `notion-py` which is an unofficial Python client for Notions API. For the current asset values, I'm using `yfinance` which allows easy access to data from Yahoo Finance. One thing to note with this is that the ticker values used have to correspond with values on the platform. 

## Google Cloud Platform Architecture:

<img src="flow.png" width="80%">

## Getting Started: 

### Prerequisites:

```
notion == 0.0.25
yfinance == 0.1.54
forex_python == 1.5
```

## 1. Updating Variables: 

The following variabels require updating:

```
token_v2 =
page_url =
table_url =
```

## 2. Setting up Cloud Functions and Pub/Sub:

* Trigger - choose Pub/Sub and either create a new or use an exiting topic.
* Either upload or copy/paste the main.py and requrements.txt file.
* Set the function to execute as 'run'.
* The function can be tested using 'Test function' option under the actions menu once deployed.

<img src="cloud-functions.gif" width="60%">

## 3. Setting up Cloud Scheduler: 

* Set the target to the Pub/Sub topic.

<img src="scheduler.gif" width="60%">
