from main import (
    count_chars,
)  # Example import to use the main module
import azure.functions as func
import logging


app = func.FunctionApp()  # Container for all functions in this file


# def count_chars(inputstr: str = "Hello") -> str:
#     # Count the number of characters in the input string
#     return f"The input string '{inputstr}' has {len(inputstr)} characters."


@app.function_name(name="HttpTriggerFunction")
@app.route(route="char_count")  # This is the endpoint after DomainURL/api/
def hello_world(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    try:
        inputstr = req.params.get("inputstr")
        return func.HttpResponse(count_chars(inputstr))
    except Exception as e:
        logging.error(f"Error retrieving inputstr: {e}")
        return func.HttpResponse(f"Error retrieving input string: {e}", status_code=400)
