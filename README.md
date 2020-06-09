# employee_database
# employee_database
A user friendly web application used to maintain an employee database. This is my submission for the coding round of the Scientia Internship. As of now the application has not been deployed.

## Code Base Structure ##
+ **static** consists of all the css and media files.
  - *style.css* is the main style sheet for the web application.
  - *media* stores all the images used in the database.
+ **template** consists of all the html templates for the web pages.
  - *main_template.html* is the layout extended by all other templates.
  - *home_template.html* is the template for the home page.
  - *database_template.html* is the template for the page listing the employees in the database.
  - *employee_template.html* is the template for the page displays the data of a single employee in detail.
  - *input_template.html* is the template to input (add or update) employee infromation the database.
+ **venv** is the virtual environment used to keep the dependencies separate.
## Set-up ##
To use this web application, first create and activate a new virtual environment using virtualenv.
```
pip install virtualenv
virtualenv myproject source myproject/venv/bin/activate
```
Clone this repository and install the requirements.
```
git clone https://github.com/aryaapai/employee_database/
pip -r requirements.txt
```
Run the main.py script to start the application. 
```
python main.py
```
