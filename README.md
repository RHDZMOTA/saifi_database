# SAIFI_DATABASE

This proyect is a collaboration between the Financial Engineering Student Union and the Academic Council at Western Institute of Technology and Higher Education (ITESO).
The main objective is to make availabe general information about the Student Union and to familiarize the students with the python language and git programming.
Please feel free to contribure to this proyect. Meetups or consultancy can be given at the University (contact _saifi@iteso.mx_ for more information). 

Authors:
* Rodrigo Herández Mota: @rhdzmota
* add...


## Requirements
- Python 3.5 or current version
- Packages: numpy, pandas, matplotlib
- git and a github account

## Instructions
1. Clone or download this proyect
2. Depending your OS, run the files:
    * **run_in_windows.bat** for Windows.
    * **run_in_mac...** for Mac (not availabe).
    * **run_in_dev...** for Ubuntu or Debian (not available).
3. Explore and modify the database at will. **Recommended**: see 'to do' section for helping
        building this proyect. 
4. _git push_ if you have a valuable contribution. 
5. Enjoy. 

## Contents

### Databases
The information of the Student Union is stored in the following files:
* **members.csv**: id_members,name,surname,mobile_phone,email
* **roles.csv**: id_roles,roles
* **status.csv**: id_status,status
* **eyecolor.csv**: id_eyecolor,color
* **members_roles.csv**: id_members, id_roles,id_status,since,until
* **physical_charact.csv**: id_members,age,birthday,gender,height,weight,id_eyecolor

### Python scrypts
* **load.py**: facilitates the data loading in other scrypts.
* **explorative.py**: statistical analysis and visualization tests.
* **python_program.py**: general program to explore database, add new data, analyze (statistics) and visualize. 

### Bash scrypts
* **run_in_windows.bat**: automatically runs _python_program.py_.


## To do:

- Enhance statistical analysis *(explorative.py to test, when 'good enough' add to python_program.py)*.
- Provide good visualizations. 
- Add some python functions to _python_program.py_:
    - Show processed tables (summary).
    - Add basic descriptive stats.
    - Capability to add new data. 
    - Update age with birthday information
    - ...
- Make batch file for:
    - Mac
    - Ubuntu / Debian

