import json
import logging

logging.basicConfig(
    filename="data/projectmill.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def save(data, path="data/db.json"):
    logger.debug(f"Saving data to {path}")
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load(path="data/db.json"):
    logger.debug(f"Loading data from {path}")    
    try:
        with open(path, "r") as f:
            content = f.read()
            if not content.strip():
                logger.debug("File is empty, returning empty dict")
                return {}
            return json.loads(content)
    except FileNotFoundError:
        logger.debug(f"File not found: {path}, returning empty dict")
        return {}  
    except json.JSONDecodeError:
        logger.debug(f"Malformed JSON in {path}, returning empty dict")
        return {}