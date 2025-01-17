## Overview

This repository was inspired by the [HashiCorp Terraform Spotify Playlist tutorial](https://developer.hashicorp.com/terraform/tutorials/community-providers/spotify-playlist). 
It demonstrates how to use Terraform with the Spotify API to manage playlists programmatically.

## Prerequisites

Before you begin, ensure you have the following set up:

1. **Create a Spotify App**  
   - Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and create an app.
   - Note down your **Client ID** and **Client Secret**.
   - Set a **Redirect URI** for your app. For example:  
     ```
     http://localhost:27228/callback
     ```

2. **Set up Environment Variables**  
   - Copy `.env.example` to `.env` and populate it with your Spotify app credentials:
     ```
     SPOTIFY_CLIENT_ID=<your-client-id>
     SPOTIFY_CLIENT_SECRET=<your-client-secret>
     SPOTIFY_REDIRECT_URI=<your-redirect-uri>
     ```

3. **Configure Terraform Variables**  
   - Copy `terraform.tfvars.example` to `terraform.tfvars` and customize it according to your needs.

## Installation

Follow these steps to set up the project:

1. Install `pipenv`:  
   ```pip install pipenv --user```

2. Install Python dependencies:  
   ```pipenv install```

3. Install the latest version of the `cdktf` CLI:  
   ```npm install --global cdktf-cli@latest```

## Usage

Use the following commands to manage your Terraform deployment:

1. **Deploy the Configuration**  
   Apply the configuration and create resources on Spotify:  
   ```cdktf deploy --var-file=terraform/terraform.tfvars```
2. **Destroy the Configuration**  
   Remove the resources managed by Terraform:  
   ```cdktf destroy --var-file=terraform/terraform.tfvars```
