# Project Root

I got tired of import errors when running from the terminal/ide/from inside a nested module.  
Plus I can't stand the "import os, sys ... sys.path.app..." fix.

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
