# Plotly Dash Workshop
## https://github.com/PolymathVentures/wids2019_cali

## Prerequisites

### GIT version control

Linux: https://www.atlassian.com/git/tutorials/install-git#linux

Windows: https://www.atlassian.com/git/tutorials/install-git#windows

OSX: https://www.atlassian.com/git/tutorials/install-git#mac-os-x


## Basic setup

```
git clone https://github.com/PolymathVentures/wids2019_cali.git
cd wids2019_cali
python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt
```

## Run dashboard

```
python3 app.py
```

## What is Plotly Dash

https://plot.ly/python/
https://dash.plot.ly/gallery

## Deployment


### Deploy on heroku

Sign up on heroku.com

```
git add .
git commit -m 'first dashbard'
curl https://cli-assets.heroku.com/install.sh | sh
heroku create wids2019_cali
git push heroku master
```




