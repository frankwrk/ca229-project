# CA229_2020-Group_107 Project

**Health & Safety Django Website**

HSE Locations in Ireland, using data and API's 

1.  https://data.smartdublin.ie/dataset/health-centres
2.  https://data.gov.ie/dataset/health-and-wellbeing

Project **Trello board**: https://trello.com/b/L4UZbrlh/groupproject

Project **Gitlab URL**: https://github.com/frankwrk/ca229-project

Project dependencies: 
*   python 3.8.2 
*   django 3.0.5
*   pip 20.0.2

Application file structure: 
- hse_site/  (main project folder)
    - site-root/   (Django Application folder)
        - hsesite/    (Application settings folder)

In order to install this version of the application: 
*  Download this repo on your development machine by clicking on the following link (https://gitlab.computing.dcu.ie/furduif2/ca229_2020-group_project/-/archive/master/ca229_2020-group_project-master.zip)
*  Unzip the archive, open your terminal and navigate to the project folder: `cd ca229_2020-group_project-master`
*  Verify your python version by running: `python3 --version` (if your result is different than 3.8.2, install the latest version from https://python.org/downloads/)
*  Activate your virtual environment: - on macOS: `source env_hseloc/bin/activate`
                                      - on windows: `env_hseloc/scripts/activate`
                                      - your terminal command prompt should start with `(env_hseloc)`
*  Verify your django version by running `python -m django --version`, which should give you version 3.0.5
*  Test your instance of the application by running the following commands: `cd site_root` and `python manage.py runserver`
*  Open your browser and navigate to http://127.0.0.1:8000/ where you should see the flying rocket

This is the end of the initial version of the application.

Follow the tutorials in the Django Book https://loop.dcu.ie/pluginfile.php/3029104/mod_resource/content/2/Django2Book_v02.pdf to add your pages

Test all work, before pushing your changes to `dev` branch (https://gitlab.computing.dcu.ie/furduif2/ca229_2020-group_project/tree/dev)