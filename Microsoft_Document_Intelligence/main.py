from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from dotenv import load_dotenv
import os
import logging
import json

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Load environment variables from .env file
try:
    load_dotenv()
    logger.info("Environment variables loaded successfully")
except Exception as e:
    logger.error(f"Error loading environment variables: {e}")

# DOC_PATH = "./data/ASOP/asop001_170.pdf"
DOC_PATH = "./data/harry_potter_and_the_philosophers_stone.pdf"


def main():

    endpoint = os.getenv("MICROSOFT_DOCUMENT_INTELLIGENCE_ENDPOINT")
    key = os.getenv("MICROSOFT_DOCUMENT_INTELLIGENCE_KEY")
    logger.info(f"Initializing Document Intelligence Client with endpoint: {endpoint}")

    client = DocumentIntelligenceClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    with open(DOC_PATH, "rb") as f:
        poller = client.begin_analyze_document(
            "prebuilt-layout", f, pages="1-3", content_type="application/pdf"
        )

    result = poller.result()
    logger.info(
        f"Document analysis completed successfully. Poller status: {poller.status()}"
    )

    # Save results to a file
    output_path = "./data/document_analysis_result.json"
    try:
        with open(output_path, "w") as f:
            json.dump(result.as_dict(), f, indent=4)
        logger.info(f"Document analysis results saved to {output_path}")
    except Exception as e:
        logger.error(f"Error saving document analysis results: {e}")


if __name__ == "__main__":
    main()
