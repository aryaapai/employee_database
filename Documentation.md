# Employee Database
A user friendly web application used to maintain an employee database created using Python, Flask and SQLAlchemy. This is my submission for the coding round of the Scientia Internship. As of now the application has not been deployed.
## Design Requirements ##
The web application was required to create a database to store employee name, phone, address and designation. It also needed to have the following features : 
+ List Employees from Database
+ Add Employee to Database
+ Delete Employee from Database
+ Search Employee Using name, designation or phone

Apart from the above features, the current web application also stores employee email address and picture. It also has features to update information of employees already in the database and view each employee's information on a different page. 
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
+ **main.py** script runs the Flask application and handles all the routes and requests.
+ **db.py** module contains the models [Employees].
+ **forms.py** contains classes for forms used in the application.
+ **requirements.txt** contains the dependencies required for the application. 

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
## User Guide ##
To access the employee database, *Request:* GET api/employees will dispaly the web page with the Employee Database Table. Only the Employee name, phone, address and designation is shown in this table. On hovering over a certain row, it will turn orange in indication. Clicking on the Employee's Name will display a webspage showing that Employee's Details. The search bar and button on top can be used to search for a particular employee, using either their full name, phone or designation. An appropriate message will be displayed if the Employee Database is empty or none of the employees matched the search category. 

A new employee can be added to the Employee Database by clicking on the "Add a New Employee" tab on the top navigation bar. The navigation bar tabs turn orange on hovering over them. The Add a New Employee page is a form where employee infromation can be added. The Employee name, desigantion and email are required fields. The email id provided needs to be a valid email id. The designation feild is a drop down menu from which the deisgnation, which is uniform for a given organization, can be chosen. The phone number and address are not required and will should up as Not Provided on the Database if left blank. If a phone number is entered, it should be 10 digits long (a valid mobile number). Similarly, an employee photo id can be uploaded as .png or .jpg file. A default id picture will be provided in its absence. The user will not be allowed to submit the form if any of these basic rules are not met and will be given warnings until valid data is provided. On submitting a valid form, the user wil be redirected to the Employee Database Table, to which the new employee has been added. A message will also be displayed stating the same.

The Employee's photo id and other details can be viewed by clicking on their name in the Employee Database Table. On this webpage with the specific Employee's data, the user can also chose to edit or delete this information. On clicking the "Edit Employee Information", the user is redirected to a page similar to the add page, excpet with the employee's information filled in. The procedure to edit the information is same as procedure to add a new employee's information. If the "Delete" button is clicked, the user will need to confirm the deletion of a data once again before it is deleted permanentaly. For both the action, after completetion the user is redirected to the Employee Database Table with an appropriate message on the screen.

## Backend Specification ##
+ Go to the home page *Request:* GET api/
+ Get all the employees *Request:* GET api/employees 
+ Search for specific employees *Request:* POST api/employees/
+ Add a new employee's information *Request:* GET api/employees/add 
+ Post a new employee's information *Request:* POST api/employees/add *Redirect:* GET api/employees if validated
+ Get a specific employees *Request:* GET api/employees/{employee_id}
+ Edit a specific employee's information *Request:* GET api/employees/{employee_id}/edit
+ Post a specific employee's edited information *Request:* POST api/employees/{employee_id}/edit *Redirect:* GET api/employees if validated
+ Delete a specific employee's information *Request:* POST api/employees/{employee_id}/delete *Redirect:* GET api/employees if confirmed deletion. 

## Tools Used ##
Flask was used to run the application. HTML and CSS were used to design the web pages displayed. Boostrap was also used for the same, to make platform responsive applications. Template Layouts were made for code reusablity. SQLAlchemy was used to create and query the employees database model. WTForms were used for user input. These were chosen instead of Forms because of the need to handle Form logic in Flask. A few other libraries were used to aide the development of the application. 
## Further Improvements ##
There were certain parts of the project that I did not have enough time to complete. Here is how I would like to improve them.
+ Use Python's Whoosh to search for employees as it provides full text indexing and searching. 
+ Use Pagination while displaying the employee database to save memory.
+ Order the employee database table based on user's preference. 
+ Enhance the input of employee data, eg. asking for phone number as 3 different fields cont-area-ext.
+ Use Java Script to enhance UX/UI and add animations.
+ Use Pydocs to document the application. 
