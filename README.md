# Project Root
Run your python code from any nested module.

Got tired of import errors when running from the terminal/ide/from inside a nested module.  
Plus can't stand "import os, sys ... sys.path.app...".

This project solves it for me.  
I'm sure there are other/better ways - hit me in the issue tab with suggestions.

Meanwhile,  
```
pip install project-root
```  
then add a '.project_root.ini' file to every relevant folder.  
the stracture of the ini file should be:  
```
# .project_root.ini   

[Project_Root]   
absolute_path=/home/project/absolute/path
```
