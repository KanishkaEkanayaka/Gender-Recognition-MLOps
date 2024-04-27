import os
from box.exceptions import BoxValueError
import yaml
from cnnGenderClassifier.utils import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ reads yaml file and returns

    Args:
        path_to_yaml(str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox Type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    """Create list of directories
    
    Args:
        path_to_directories(list): list of path of directories
        ignore_log (boolean, option): ignore if multiple dir to be created
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Save json data
    
    Args:
        path(Path): path to json file
        data(dict): data to be saved in json file
    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load json files data
    
    Args:
        path (Path): path to json
    Returns:
        ConfigBox: data as class attribute instead of dict
    """
    with open(path) as f:
        content = json.loads(f)

    logger.info(f"json file loaded successfully from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path:Path):
    """save binary file
    
    Args:
        data (Any): data to be saved as bin
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data
    
    Args:
        path (Path): path to binary file
    Returns:
        Any: object stored in file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in kb
    
    Args:
        path (Path): file path
    Returns:
        str: file size in kb
    """
    size_in_kb = round(os.path.getsize(path)/1024)

    return f"~ {size_in_kb} KB"

@ensure_annotations
def decodeImage(imgstring, filename):
    """decode the image 
    
    Args:
        imgstring: path of the image
        filename: file to image to be saved
    """
    imgdata = base64.b64decode(imgstring)
    with open(filename , "wb") as f:
        f.write(imgdata)
        f.close()

@ensure_annotations
def encodeImageIntobase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
