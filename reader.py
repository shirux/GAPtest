
import json

def read_file(file_name) -> list:
    """Read a .json file

    Returns:
        dict: Read JSON
    """
    try:
        with open(file_name, "r") as f:
            data = json.load(f)
            return data
    except:
        raise

    
  