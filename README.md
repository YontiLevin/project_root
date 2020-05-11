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
use_absolute_path=True
absolute_path=/home/project/absolute/path
folder_level=0
```
---

example project structure:
```
MyProject
|- .git
|- .gitignore
|- .project_root.ini
|- src
|    |- .project_root.ini
|    |- app.py
|    |- utils.py
```

make sure that you use global imports in your files.  
e.g,  
```
# app.py

import os
import project_root
import src.utils

---
# util.py

print('utils was imported!!!')
```

now you can run your code from anywhere inside the package
```
~ > cd MyProject 
~/MyProject > python -m src.app
utils was imported!!!

~/MyProject > python src/app.py
utils was imported!!!

~/MyProject > cd src
~/MyProject/src > python -m app
utils was imported!!!

~/MyProject/src > python app.py
utils was imported!!!
```

### project root on shared projects  
In this case the absolute path of the project changes between users.  
Therefore, use the folder_level option.  
  
ini files for the example above:
```
# .project_root.ini   

[Project_Root] 
use_absolute_path=False
absolute_path=None
folder_level=o


# src/.project_root.ini   

[Project_Root] 
use_absolute_path=False
absolute_path=None
folder_level=1
```
---
