### 0. set up repo with uv

- `uv init`
- `uv venv`
- `source .venv/bin/activate`
- (to exit the venv: `deactivate`)
- `uv add <package_name>`
- (to remove package: `uv remove <package_name>`)

### 1. push that folder to a github repo

We're going to use a cloud service to schedule our deployments (i.e., to schedule
remote run-throughs of our script without us pressing or entering anything in the CLI.)
To make sure the service has access to the code it needs to run, we'll have to make
the code available. 

For simplicity, we'll push our code to a public GitHub repository. 
In GitHub, create a new repo, then run:
- `git remote add origin <github_https_path_to_the_repo>`
- `git branch -M main`
- `git push -u origin main`


### 1. set up prefect cloud

- `prefect cloud login`: log into the prefect cloud (possible via GitHub and free)
- (in the UI, create a work pool)
- `prefect deploy`: select a flow, work pool, and schedule to deploy