import os
from flask import Blueprint, current_app, flash, jsonify, redirect, render_template, request, session, url_for, abort

from werkzeug.utils import secure_filename



views = Blueprint('views', __name__)

ADMIN_PASSWORD = 'admin123'
ADMIN_EMAIL = 'admin@easylink.ac.za'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", Hello='Welcome to EasyLink ')





@views.route('/set_theme', methods=['POST'])
def set_theme():
    data = request.get_json()
    session['theme'] = data['theme']
    return '', 204


@views.route('/about')
def about():
    return render_template("about.html")


@views.route('/help')
def help():
    return render_template("help.html")


@views.route('/login')
def login():
    return render_template("login.html")


@views.route('/sign-up')
def sign_up():
    return render_template("sign-up.html")



@views.route('/admin_home')
def admin_home():
    # Ensure only logged-in admin can access this page
    if 'admin_logged_in' not in session:
        return redirect(url_for('views.adm_login'))
    return render_template('admin_home.html')


@views.route('/adm_login', methods=['GET', 'POST'])
def adm_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the input matches hardcoded admin details
        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True  # Set session variable
            flash('Login successful!', 'success')
            return redirect(url_for('views.admin_home'))
        else:
            flash('Invalid email or password', 'error')
            return redirect(url_for('views.adm_login'))

    return render_template('adm_login.html')


@views.route('/some_protected_page')
def some_protected_page():
    if 'admin_logged_in' not in session:
        flash('Please log in to access this page', 'error')
        return redirect(url_for('views.adm_login'))

    return render_template('protected_page.html')


@views.route('/admin_base', methods=['GET', 'POST'])
def admin_base():
    return render_template('admin_home.html')


@views.route('/admin_sign-up', methods=['GET', 'POST'])
def adminsignup():
    return render_template('admin_sign-up.html')


# SECTOR A
@views.route('/manage_sectorA', methods=['GET', 'POST'])
def manage_sectorA():
    return render_template('manage_sectorA.html')

@views.route('/sectorA')
def sectorA():
    return render_template("sectorA.html")




# SECTOR B
@views.route('/manage_sectorB', methods=['GET', 'POST'])
def manage_sectorB():
   return render_template('manage_sectorB.html')

   

@views.route('/sectorB')
def sectorB():
    return render_template("sectorB.html")


@views.route('/manage_sectorC')
def manage_sectorC():
    return render_template('manage_sectorC.html')

@views.route('/sectorC')
def sectorC():
    return render_template("sectorC.html")

@views.route('/sectorD')
def sectorD():
    return render_template("sectorD.html")

@views.route('/manage_sectorD')
def manage_sectorD():
    return render_template('manage_sectorD.html')

@views.route('/manage_sectorE')
def manage_sectorE():
    return render_template('manage_sectorE.html')

@views.route('/sectorE')
def sectorE():
    return render_template("sectorE.html")

@views.route('/sectorF')
def sectorF():
    return render_template("sectorF.html")

@views.route('/manage_sectorF')
def manage_sectorF():
    return render_template('manage_sectorF.html')

@views.route('/manage_sectorG')
def manage_sectorG():
    return render_template('manage_sectorG.html')

@views.route('/sectorG')
def sectorG():
    return render_template("sectorG.html")

@views.route('/nex')
def nex():
    return render_template('nex.html')

@views.route('/nexus')
def nexus():
    return render_template('nexus.html')

UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def save_image_locally(image_file):
    if image_file:
        filename = secure_filename(image_file.filename)
        image_path = os.path.join(UPLOAD_FOLDER, filename)
        image_file.save(image_path)
        return filename
    return None

# QUESTIONS
@views.route('/manage_questions', methods=['GET', 'POST'])
def manage_questions():
        return render_template('manage_questions.html')

@views.route('/questions')
def questions():
    return render_template("questions.html")


# MEMOS
@views.route('/manage_memo', methods=['GET', 'POST'])
def manage_memo():
    return render_template("questions.html")

@views.route('/memo')
def memo():
    return render_template("memo.html")


@views.route('/engineer')
def engineer():
    return render_template('engineer.html')

@views.route('/robotics')
def robotics():
    return render_template('robotics.html')

@views.route('/physics')
def physics():
    return render_template('physics.html')

@views.route('/iot')
def iot():
    return render_template('iot.html')

@views.route('/math')
def math():
    return render_template('math.html')

@views.route('/accounting')
def accounting():
    return render_template('accounting.html')

@views.route('/entrepreneurship')
def entrepreneurship():
    return render_template('entrepreneurship.html')

@views.route('/agric')
def agric():
    return render_template("agric.html")

@views.route('/networks')
def networks():
    return render_template('networks.html')

@views.route('/numbers')
def numbers():
    return render_template('numbers.html')

@views.route('/science')
def science():
    return render_template('science.html')

@views.route('/code')
def code():
    return render_template('code.html')

@views.route('/ict')
def ict():
    return render_template('ict.html')

@views.route('/kca')
def kca():
    return render_template('kca.html')


@views.route('/manage_learners')
def manage_learners():
    return render_template('manage_learners.html')


@views.route('/manage_nexus')
def manage_nexus():
    return render_template('manage_nexus.html')






