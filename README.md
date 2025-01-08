# Modules_Packages_Libraries_Python
- Python programs become more complex as they expand in their size and fuctionality.
- Modules and packages come handy in organizing code into reusable components. 
## Modules
- Is a python file (.py) containing functions, classes, and variables.
- You can import the functionalities of a module into a program for use.
Check how `math_functions.py` module has been imported in the file `main.py` for use of the functions in the module.
## Packages
- Is a directory containing multiple modules and potentially subdirectories (more packages).
- Provides a hierarchical way/structure for organizing related code in a meaningful way.
## How to Use Packages
**(a) Create a Package**
- create a directory (folder) and place an empty file named `__init__.py` inside it. This file indicates that the directory is a Python package.
**(b) Add Modules**
- Inside the packages directory, you can add Python modules (.py files) that contain code.
**(c) Import Modules**
- You can import modules from packages into Python scripts using the import statement, specifying the package name and module name as:
```
from package_name import module_name
```
## Working with Python Libraries
(a) **Standard Libraries** collection of built-in Python modules commonly used for file handling, networking, and data manipulation. <br> <br>
(b)  **External Libraries** Many powerful third-party libraries extend Python's capabilities beyond standard library. Installed using the `pip` package manager.
## Example Libraries
- **requests**: enables making HTTP requests to web APIs and servers.
- **numpy**: provides powerful tools for numerical computing and scientific data analysis.
- **pandas**: Offer data structures and analysis tools for working with tabular data.
