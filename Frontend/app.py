from flask import Flask, jsonify, render_template, request, redirect, url_for, flash, session
from flask_session import Session
import os
import re
from Database.manage_db import add_recruiter, add_applicant, verify_recruiter, verify_applicant, Recruiter, Applicant

app = Flask(__name__, static_folder='Interface/static', template_folder='Interface/templates')
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def home():
    return render_template('index.html')



# Applicant Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        resume = request.form.get('resume')  # Assume resume file is uploaded
        
        # Check if passwords match
        if password != confirm_password:
            flash("Passwords do not match. Please try again.", "error")
            return render_template('applicant_signup.html')
        
        # Check if password is strong
        # if not is_strong_password(password):
        #     flash("Password must be at least 8 characters long, with at least one uppercase letter, one lowercase letter, one digit, and one special character.", "error")
        #     return render_template('applicant_signup.html')
        
        # Create and add the applicant
        applicant = Applicant(first_name, last_name, email, password, resume, phone)
        add_applicant(applicant)
        
        # Set session and redirect
        session['user_email'] = email
        flash("Sign up successful! Welcome to the platform.", "success")
        return redirect(url_for('home'))
    
    return render_template('applicant_signup.html')

# Recruiter Signup Route
@app.route('/signup/recruiter', methods=['GET', 'POST'])
def signup_recruiter():
    if request.method == 'POST':
        company_name = request.form.get('company-name')
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        
        # Check if passwords match
        if password != confirm_password:
            flash("Passwords do not match. Please try again.", "error")
            return render_template('recruiter_signup.html')
        
        # Check if password is strong
        # if not is_strong_password(password):
        #     flash("Password must be at least 8 characters long, with at least one uppercase letter, one lowercase letter, one digit, and one special character.", "error")
        #     return render_template('recruiter_signup.html')
        
        # Create and add the recruiter
        recruiter = Recruiter(first_name, last_name, email, password, company_name, phone)
        add_recruiter(recruiter)
        
        # Set session and redirect
        session['user_email'] = email
        flash("Sign up successful! Welcome to the platform.", "success")
        return redirect(url_for('home'))
    
    return render_template('recruiter_signup.html')

# Applicant Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Verify applicant credentials
        if verify_applicant(email, password):
            session['user_email'] = email
            flash("Login successful! Welcome back.", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid email or password. Please try again.", "error")
    
    return render_template('applicant_login.html')

# Recruiter Login Route
@app.route('/login/recruiter', methods=['GET', 'POST'])
def login_recruiter():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Verify recruiter credentials
        if verify_recruiter(email, password):
            session['user_email'] = email
            flash("Login successful! Welcome back.", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid email or password. Please try again.", "error")
    
    return render_template('recruiter_signin.html')

# Logout Route for Both Applicant and Recruiter
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_email', None)
    flash("You have been logged out.", "success")
    return redirect(url_for('home'))

def is_strong_password(password):
    # Password strength criteria
    if (len(password) < 8 or
        not re.search(r"[A-Z]", password) or  # At least one uppercase letter
        not re.search(r"[a-z]", password) or  # At least one lowercase letter
        not re.search(r"[0-9]", password) or  # At least one digit
        not re.search(r"[!@#$%^&*()]", password)):  # At least one special character
        return False
    return True

if __name__ == "__main__":
    app.run(debug=True)
