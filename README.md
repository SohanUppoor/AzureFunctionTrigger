# Azure Function – HTTP Trigger (Python)

## Overview

This repository contains a **Python-based Azure Function** that exposes an **HTTP-triggered endpoint**. The function processes incoming HTTP requests and returns a simple success message.

The function is implemented using the **Azure Functions Python v2 programming model** and is configured with **anonymous access**, allowing it to be invoked without authentication.

---

## Function Endpoint

Route:

```
/api/testaichatbot
```

Example Response:

```
HTTP triggered function executed successfully.
```

---

## Project Structure

```
azure-function-http-trigger/
│
├── function_app.py        # Azure Function application
├── requirements.txt       # Python dependencies
├── host.json              # Azure Functions host configuration
├── local.settings.json    # Local development configuration
└── README.md
```

---

## Prerequisites

Before running or deploying the function, ensure the following tools are installed:

* Python 3.9 or later
* Azure CLI
* Azure Functions Core Tools
* Azure Subscription
* Node.js (required for Functions Core Tools)

Install Azure Functions Core Tools if not already installed:

```
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```

Login to Azure:

```
az login
```

---

## Install Dependencies

Create a `requirements.txt` file if not already present.

```
azure-functions
```

Install dependencies:
```
pip install -r requirements.txt
```
---

## Run Function Locally

Start the Azure Functions runtime:

```
func start
```

The function will run locally at:

```
http://localhost:7071/api/testaichatbot
```

Test the endpoint:

```
curl http://localhost:7071/api/testaichatbot
```

Expected output:

```
HTTP triggered function executed successfully.
```

---

## Deploy to Azure Functions

### 1. Create Resource Group

```
az group create --name rg-ai-functions --location eastus
```

### 2. Create Storage Account

```
az storage account create \
--name aifunctionsstorage \
--location eastus \
--resource-group rg-ai-functions \
--sku Standard_LRS
```

### 3. Create Azure Function App

```
az functionapp create \
--resource-group rg-ai-functions \
--consumption-plan-location eastus \
--runtime python \
--runtime-version 3.9 \
--functions-version 4 \
--name ai-chatbot-http-func \
--storage-account aifunctionsstorage
```

### 4. Deploy the Function

From the root project directory:

```
func azure functionapp publish ai-chatbot-http-func
```

---

## Test Deployed Function

After deployment, the function will be accessible at:

```
https://ai-chatbot-http-func.azurewebsites.net/api/testaichatbot
```

Test using curl or browser:

```
curl https://ai-chatbot-http-func.azurewebsites.net/api/testaichatbot
```

---

## Logging

Logs are generated using Python logging and can be viewed in Azure Portal.

Example log:
```
logging.info("Python HTTP trigger function processed a request.")
```
View logs in:
Azure Portal → Function App → **Log Stream**

---

## Authentication

The function currently uses:
```
func.AuthLevel.ANONYMOUS
```
This allows public access without a key.

For production environments, consider using:
```
func.AuthLevel.FUNCTION
```
or
```
func.AuthLevel.ADMIN
```

---
## Notes
* This function is intended as a **basic HTTP trigger example**.
* It can be extended to integrate with APIs, AI services, or backend systems.
* CI/CD pipelines such as **Azure DevOps or GitHub Actions** can be used for automated deployments.

---
