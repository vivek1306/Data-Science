import os
# from pathlib import path # operating system independent
from pathlib import Path

import logging
#help us to debugging
logging.basicConfig(
    level=logging.INFO,  #all the info we need
    format="[%(asctime)s:%(levelname)s]:%(message)s"  #time 
    )
while True:
    project_name=input("Enter the project name: ")
    if project_name!='':
        break
logging.info(f"Creating the project by name: {project_name}")  # 

#list of files:
list_of_files=[
    ".github/workflows/.gitkeep",# gitkeep is dummy file 
    f"src/{project_name}/__init__.py", #source repository/file containting all my scripts
 #init tells its a project    
 f"tests/__init__.py",
 f"tests/unit/__init__.py",
 f"tests/integration/__init__.py",
 "init_setup.sh",  # help us to set up environment,
 "requirements.txt", 
 "requirements_dev.txt", #only used for testing
 "setup.py", 
 "pyproject.toml",
 'setup.cfg',
 "tox.ini"
]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(Path(filepath))
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating a directory at:{filedir} for file:{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w")as f:
            pass
        logging.info(f"creating a new file:{filename} at Path:{filepath}")
    else:
        logging.info(f"file is already exist at{filepath}")

