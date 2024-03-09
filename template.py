import os
import logging
from pathlib import Path

project_name = "Instance_Segmentation"
list_of_files = [
    ".github/workflows/gitkeep",
    "setup.py",
    "requirements.txt",
    "params.yaml",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/logging/logger.py",
    f"src/{project_name}/exception/exception.py",
    f"src/{project_name}/components/dataingestion.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/utility/utils.py",
    f"src/{project_name}/configuration/config.py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/entity/entity.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")