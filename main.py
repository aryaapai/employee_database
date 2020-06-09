from flask import Flask, render_template, url_for, redirect, flash, request
from db import db, Employees
from forms import InputEmployeeForm, SearchEmployeeForm
import os
import secrets
from PIL import Image

app = Flask(__name__)
db_filename = 'EMPLOYEES.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'l3ir4yh2o38fuhncedjcwoeu82983u3l'

db.init_app(app)
with app.app_context():
    db.create_all()


# Routes


@app.route('/')
def home():
    return render_template('home_template.html')


@app.route('/employees', methods=['GET','POST'])
def employees():
    search_form = SearchEmployeeForm()
    if request.method == 'POST':
        keywords = search_form.keywords.data
        if(keywords==''):
            raw_employees = Employees.query.all()
        else:
            name_query = Employees.query.filter_by(name=keywords).all()
            phone_query = Employees.query.filter_by(phone=keywords).all()
            designation_query = Employees.query.filter_by(designation=keywords).all()
            raw_employees = name_query + phone_query + designation_query
    else:
        raw_employees = Employees.query.all()
    employees = [ employee.serialize() for employee in raw_employees ]
    return render_template('database_template.html', employees=employees, form=search_form)


@app.route('/employees/add', methods=['GET','POST'])
def add_employee():
    add_form = InputEmployeeForm()
    if add_form.validate_on_submit():
        if add_form.picture.data :
            file = store_image(add_form.picture.data)
        else :
            file = 'media/default_picture.png'
        new_employee = Employees(
            name = add_form.name.data,
            designation = add_form.designation.data,
            address = ('Not Provided', add_form.address.data) [bool(add_form.address.data)],
            phone = ('Not Provided', add_form.phone.data) [bool(add_form.phone.data)],
            email = add_form.email.data,
            picture = file
        )
        db.session.add(new_employee)
        db.session.commit()
        flash('The New Employee Has Been Added To The Database', 'success')
        return redirect(url_for('employees'))
    elif (add_form.picture.data) and (not add_form.picture.errors):
        add_form.picture.data = store_image(add_form.picture.data)
    else:
        add_form.picture.data = 'media/default_picture.png'
    return render_template('input_template.html', form=add_form, title='Add Employee', legend='ADD A NEW SCIENTIA EMPLOYEE')


@app.route('/employees/<int:employee_id>')
def employee(employee_id):
    employee = Employees.query.get_or_404(employee_id)
    return render_template('employee_template.html', employee=employee, title=employee.name)


@app.route('/employees/<int:employee_id>/edit', methods=['GET','POST'])
def edit_employee(employee_id):
    employee = Employees.query.get_or_404(employee_id)
    edit_form = InputEmployeeForm()
    if edit_form.validate_on_submit():
        employee.name = edit_form.name.data
        employee.designation = edit_form.designation.data
        employee.address =('Not Provided', edit_form.address.data) [bool(edit_form.address.data)]
        employee.email = edit_form.email.data
        employee.phone = ('Not Provided', edit_form.phone.data) [bool(edit_form.phone.data)]
        if edit_form.picture.data:
            os.unlink(os.path.join( app.root_path, 'static', employee.picture))
            employee.picture = store_image(edit_form.picture.data)
            print(employee.picture)
        db.session.commit()
        flash('The Employee Information Has Been Added Updated', 'success')
        return redirect(url_for('employee', employee_id=employee_id))
    elif request.method == 'GET':
        edit_form.name.data = employee.name
        edit_form.designation.data = employee.designation
        edit_form.address.data = (employee.address, None) [employee.address == 'Not Provided']
        edit_form.email.data = employee.email
        edit_form.phone.data = (employee.phone, None) [employee.phone == 'Not Provided']
        edit_form.picture.data = employee.picture
    elif (edit_form.picture.data) and (not edit_form.picture.errors):
        image_file = store_image(edit_form.picture.data)
        employee.picture = image_file
        edit_form.picture.data = image_file
    else:
        edit_form.picture.data = employee.picture
    return render_template('input_template.html', form=edit_form, title='Edit Employee Information', legend='EDIT SCIENTIA EMPLOYEE INFORMATION')


@app.route('/employees/<int:employee_id>/delete', methods=['GET','POST'])
def delete_employee(employee_id):
    employee = Employees.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()
    flash('The Employee Information Has Been Deleted Sucessfully', 'success')
    return redirect(url_for('employees'))


# Helper Functions


def store_image(form_picture):
    """
        Stores form_picture in the static/media directory and returns the file
        name.
        Parameter form_picture: url of a .jpg or .png file to be stored.
    """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/media', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return os.path.join( 'media', picture_fn)


if __name__ == '__main__':
    app.run(debug=True)
