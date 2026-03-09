import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="testaichatbot")
def testaichatbot(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    return func.HttpResponse(
        "HTTP triggered function executed successfully.",
        status_code=200
    )