# Ship Git
Simple Flask web app to automatically pull updates on a remote server. Inspired by [Git-Auto-Deploy](https://github.com/olipo186/Git-Auto-Deploy).

## How does it work?
In `scripts/`, whenever you push to `GITHUB_REPO`, the bash script `GITHUB_REPO.sh` will be run. For each `GITHUB_REPO` you wish to use Ship Git with, you can create a new executable. Make sure the file has the correct permissions to run: `chmod 755 GITHUB_REPO.sh`.

## Deploying
1. Clone repository onto the server hosting your websites
1. Create and activate python3 virtual environment
1. `cp sample-config.json config.json`
1. Edit config file as needed
1. Run the app
1. Make sure the app is available through some URL
1. Add the URL to the list of GitHub webhooks in your repository