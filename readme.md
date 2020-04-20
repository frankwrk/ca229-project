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
*   css framework Tailwind https://tailwindcss.com/

Application file structure: 
- ca229_project/  (main project folder)
    - hse_site/   (Django Application folder)
    - static/     (CSS, Javascript and Images)
    - templates/  (HTML templates and pages) 

In order to install this version of the application: 
*  You will a GitHub account for this to work, because Gitlab is not working for me. Checkout https://github.com if you don't have an account.
*  Navigate to a place where you want to save and work on yout application, e.g C:\dcu\ca229 , or something similar
*  Download this repo on your development machine by running the following command in your terminal `git clone https://github.com/frankwrk/ca229-project.git`
*  Go to the folder just created name `ca229_project`
*  Install `pipenv` by running `curl https://raw.githubusercontent.com/pypa/pipenv/master/get-pipenv.py | python` (if you have problems you can check here for more details, https://pipenv-fork.readthedocs.io/en/latest/install.html)
*  Once previous task is done, run `pipenv install` to install all the dependecies of the app.
*  When finished, run `pipenv shell` which should turn on the virtual environment and then run `python manage.py migrate`
*  You now have the latest application installed and ready for more things to be added.
*  Check the application is running as it should by running `python manage.py runserver` 

*  Open your browser and navigate to http://127.0.0.1:8000/ where you should see the an application dashboard


Test all work, before pushing your changes to `dev` branch.
* To add some of your changes, first check your git by running `git status`
* Then add all files by running `git add .`
* Commit all changes `git commit -a -m "Change commit message to something relevant to your update"`
* Push all changes to the `your-name` branch by running `git checkout -b your-name` (you can have your own branch, which includes all the changes you make to the applciation)
* Run `git push --set-upstream origin your-name` to switch to your own branch and repeat the steps above to add, commit and `git push` your changes to your branch.
* change the template files related to your work and use Tailwind css framework (find examples and elements here https://tailwindcss.com/)