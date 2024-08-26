# Welcome to pplox_web! 

## Commands
### Running Locally
* `pip install -r requirements.txt` - Install dependencies.
* `python manage.py runserver` - Run locally.

### Running with Docker
* `docker run ghcr.io/karlcaga/pplox_web:main` - Pulls and runs the pplox_web container.

## Structure
```
pplox_web       # Django project 
    settings.py # The project configuration (Secrets, database, security, etc.)
    urls.py     # This routes to the apps in the project
    ...         # Auto-generated server configuration

interpreter     # The Django app
    urls.py     # Maps URLs to function views
    views.py    # Defines functions to handle HTTP requests and return responses
    ...         # Auto-generated modules for unused features

docs            # Project documentation
    index.md    # This page 
    blog/posts/ # Changelogs
```

## Deployments
### Render <https://pl0x.onrender.com> 

This deployment uses Render's free tier to build and host pplox_web.
Render's build pipeline uses `build.sh` which is triggered by pushes to the `main` branch.
Successful builds are then deployed to <https://pl0x.onrender.com> with the deployment being configured with `render.yaml`.

PROS: 

- Simple to use
- Don't have to think about infrastructure
- Generous free tier

CONS:

- Pricey beyond free tier
- No control over underlying infrastructure
- Render takes app down after period of inactivity
    - First load can be slow from cold boot

### Google Cloud Platform (GCP) <http://34.170.207.9> 

The GCP deployment leverages a custom Docker container and is automatically deployed with GitHub Actions. 
The container image build is defined in `Dockerfile`.
GitHub Actions listens for pushes to the `main` branch, builds the Docker image, pushes it to GitHub Container Registry (GHCR), and deploys it to a free tier Google Compute Engine (GCE) `e2-micro` instance.
The GitHub Action uses a service account using SSH to stop the Docker container, pull the latest image that was just built, and start a new container

PROS:

- Control over underlying infrastructure
- Doesn't go down after inactivity

CONS:

- Free tier is limited to 30 days per month
- Machine is weak and needs to be bootstrapped with Docker

## URLs
### `/interpreter/` 

Method: `GET`

Displays the form to the user which submits it to `/interpreter/runcode/`

### `/interpreter/runcode/`
Method: `POST`

Arguments:

- `code` The code to be run. 

Runs the code against the pplox interpreter and displays the result.
