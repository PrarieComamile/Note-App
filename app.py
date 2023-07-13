from flask import Flask, render_template, request, flash, redirect, url_for, session, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from validate_email import validate_email
from functools import wraps
import datetime


#Kullanıcı giriş Decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Please login to view!", "danger")
            return redirect(url_for("login"))
            
    return decorated_function

class RegisterForm(Form):
    name = StringField("First and Last name", validators=[validators.input_required("Please write your first and last name!"), validators.Length(2, 25)])
    email = StringField("E-mail", validators=[validators.email("Please enter a valid e-mail address!"), validators.DataRequired("Please enter a e-mail")])
    username = StringField("Username", validators=[validators.input_required("Please write a username!")])
    password = PasswordField("Password", validators=[validators.input_required("Please write a password!"), validators.EqualTo(fieldname="confirm", message="Password didn't match")])
    confirm = PasswordField("Confirm Password")

class LoginForm(Form):
    email = StringField("E-mail", validators=[validators.email("Please enter a valid e-mail address!"), validators.DataRequired("Please enter a e-mail")])
    password = PasswordField("Password")
    
class NoteForm(Form):
    title = StringField("", validators=[validators.Length(min=2, max=40), validators.DataRequired()])
    content = TextAreaField("", validators= [validators.DataRequired()])

app = Flask(__name__)
app.secret_key = "enter_secret_key"

#Mysql Config
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "your_username"
app.config["MYSQL_PASSWORD"] = "your_password"
app.config["MYSQL_DB"] = "your_dbname"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

def notlar():
    cursor = mysql.connection.cursor()
    sorgu = "Select * From table_{0}".format(session["id"])
    result = cursor.execute(sorgu)
    words = ("year", "month", "week", "day", "hour", "minute", "seconds")
    
    
    if result > 0:
        notes = cursor.fetchall()
        created_time = []
        
        for time in reversed(notes):
            _created_time = time["created_date"]
            
            _result = datetime.datetime.now() - _created_time
            _result = (_result.days // 365), (_result.days // 12), (_result.days // 7), _result.days, (_result.seconds // 3600), (_result.seconds // 60) % 60, _result.seconds
            

            for index, i in enumerate(_result):
                if i > 0:
                    result = (f"{i} {words[index]} ago")
                    break
                    
            created_time.append(result)
            
        return created_time, notes
    
    else:
        return False
    
def create_db(id):
    cursor = mysql.connection.cursor()
    
    table_name = f"table_{id}"

    create_table_query = f'''
    CREATE TABLE {table_name} (
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        title VARCHAR(40),
        content TEXT,
        created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    '''
    
    cursor.execute(create_table_query)
    
    mysql.connection.commit()
    cursor.close()


@app.route("/dashboard")
@login_required
def dashboard():
    try:
        if notlar() == False:
            return render_template("dashboard.html", active_page = "dashboard", _donguIsEmpty=True)
        else:
            return render_template("dashboard.html", active_page = "dashboard", _donguIsEmpty=False, notes=notlar()[1], created_time=notlar()[0])
    except Exception as error:
        return render_template("error.html", message = error)
        

@app.route("/", methods=["POST", "GET"])
@login_required
def main():
    try:
        if notlar() == False:
            return render_template("index.html", active_page = "home", _donguIsEmpty=True)
        else:
            return render_template("index.html", active_page = "home", _donguIsEmpty=False, notes=notlar()[1], created_time=notlar()[0])
    except Exception as error:
        return render_template("error.html", message = error)


@app.route("/createnote", methods=["GET", "POST"])
@login_required
def addnote():
    try:
        form = NoteForm(request.form)
        
        if request.method == "POST":
            title = form.title.data
            content = form.content.data
            
            cursor = mysql.connection.cursor()
            
            sorgu = "INSERT INTO table_{0} (title, content) VALUES(%s, %s)".format(session["id"])
            cursor.execute(sorgu, (title, content))
            mysql.connection.commit()
            cursor.close()

            flash("Note added...", "success")
            
            return redirect(url_for("dashboard"))
        
        else:
            return render_template("createnote.html", form=form)
    except Exception as error:
        return render_template("error.html", message = error)
    
@app.route("/delete/<string:id>")
@login_required
def delete(id):
    try:
        cursor = mysql.connection.cursor()
        
        sorgu = "Select * from table_{0} where id = %s".format(session["id"])
        result = cursor.execute(sorgu, (id,))
        
        if result > 0:
            sorgu1 = "Delete from table_{0} where id = %s".format(session["id"])
            cursor.execute(sorgu1, (id,))
            mysql.connection.commit()
            
            return redirect(url_for("dashboard"))
        
        else:
            flash("Note Not Found!", "danger")
            return redirect(url_for("main"))
    except Exception as error:
        return render_template("error.html", message = error)


@app.route("/dashboard/notes/<string:id>", methods=["GET", "POST"])
@login_required
def notes(id):
    try:
        if request.method == "GET":
            cursor = mysql.connection.cursor()

            sorgu = "Select * from table_{0} where id = %s".format(session["id"])
            result = cursor.execute(sorgu, (id,))
            
            if result == 0:
                flash("Note Not Found!", "danger")
                return redirect(url_for("main"))
            else:
                note = cursor.fetchone()
                form = NoteForm()
                
                form.title.data = note["title"]
                form.content.data = note["content"]
                
                return render_template("note.html", form=form)
            
        else:
            form = NoteForm(request.form)
            
            newTitle = form.title.data
            newContent = form.content.data
            
            sorgu1 = "Update table_{0} Set title=%s, content=%s where id=%s".format(session["id"])
            cursor = mysql.connection.cursor()
            cursor.execute(sorgu1, (newTitle, newContent, id))
            mysql.connection.commit()
            
            flash("Note Successfully Updated!", "success")
            return redirect(url_for("dashboard"))
    except Exception as error:
        return render_template("error.html", message = error)
    
@app.route("/about")
@login_required
def about():
    return render_template("about.html", active_page = "about")

#Email Control
def control_email(email):
    
    cursor = mysql.connection.cursor()
    sorgu = "Select * From users where email = %s"
    result = cursor.execute(sorgu, (email,))
    
    return result
        
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    
    if request.method == "POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)
        
        result = control_email(email)
        print("RESULT: ", result, type(result))
        if result > 0:
            flash("A user with this email already exists!", "danger")
            return redirect(url_for("login"))
        else:
            cursor = mysql.connection.cursor()
            
            sorgu = "Insert into users(name, email, username, password) VALUES(%s,%s,%s,%s)"
            cursor.execute(sorgu, (name, email, username, password))
            mysql.connection.commit()
            
            
            cursor.execute("Select * From users where email = %s", (email, ))
            data = cursor.fetchone()
            id = data["id"]
            
            #Create a database for user
            create_db(id)
        
            cursor.close()
            
            flash("You have successfully registered!", "success")
            return redirect(url_for("login"))
        
    else:
        return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    try:
        form = LoginForm(request.form)

        if request.method == "POST":
            email = form.email.data
            password_entered = form.password.data
            
            cursor = mysql.connection.cursor()
            
            sorgu = "Select * From users where email = %s"
            result = cursor.execute(sorgu, (email,))
            
            if result > 0:
                data = cursor.fetchone()
                real_password = data["password"]
                name = data["name"]
                id = data["id"]
                
                if sha256_crypt.verify(password_entered, real_password):
                    flash("You have successfully logged in!", "success")
                    
                    session["id"] = id
                    session["logged_in"] = True
                    session["email"] = email
                    session["name"] = name
                    
                    return redirect(url_for("main"))
                else:
                    flash("Wrong password!", "danger")
                    return redirect(url_for("login"))
                                
            else: 
                flash("User not found!", "danger")
                return redirect(url_for("login"))
            
        return render_template("login.html", form=form)

    except Exception as error:
        return render_template("error.html", message = error)

@app.route("/logout")
def logout():
    session.clear()
    
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)