import os
import sys
import configparser
config = configparser.ConfigParser()


project_root = None
project_root_file = '.project_root.ini'
if os.path.exists(project_root_file):
    config.read(project_root_file)
    if config['Project_Root']['use_absolute_path']:
        project_root = config['Project_Root']['absolute_path']
    else:
        project_root = os.path.abspath(__name__)
        for i in range(int(config['Project_Root']['folder_level'])):
            project_root = project_root.parent
 
if project_root is not None and project_root not in sys.path:  
    package_absolute_path = str(os.path.abspath(__name__))
    project_root = project_root.rstrip("\'").lstrip("\'")
    if not package_absolute_path.startswith(str(project_root)):
        print('possible security vulnerability - project root not added to path')
        print(f'project root: {project_root} not part of the package absolute path({package_absolute_path})')
    else:
        sys.path.append(project_root)
