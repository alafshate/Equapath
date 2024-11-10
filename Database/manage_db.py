import json
from datetime import datetime
import uuid
from Objects.post import Post
from Objects.user import User, Recruiter, Applicant


# Paths to JSON files
APPLICANT_TABLE_PATH = "applicant_table.json"
POSTS_TABLE_PATH = "posts_table.json"
RECRUITER_TABLE_PATH = "recruiter_table.json"

# Initialize JSON files if they don't exist
def initialize_json(file_path, default_data):
    try:
        with open(file_path, 'x') as f:
            json.dump(default_data, f)
    except FileExistsError:
        pass

initialize_json(APPLICANT_TABLE_PATH, [])
initialize_json(POSTS_TABLE_PATH, [])
initialize_json(RECRUITER_TABLE_PATH, [])

# Function to add a recruiter
def add_recruiter(recruiter: Recruiter):
    with open(RECRUITER_TABLE_PATH, 'r+') as f:
        recruiters = json.load(f)
        recruiters.append(recruiter.to_dict())
        f.seek(0)
        json.dump(recruiters, f)

# Function to verify recruiter email and password
def verify_recruiter(email, password):
    with open(RECRUITER_TABLE_PATH, 'r') as f:
        recruiters = json.load(f)
        for recruiter in recruiters:
            if recruiter["email"] == email and recruiter["password"] == password:
                return True
    return False

# Function to add an applicant
def add_applicant(applicant: Applicant):
    with open(APPLICANT_TABLE_PATH, 'r+') as f:
        applicants = json.load(f)
        applicants.append(applicant.to_dict())
        f.seek(0)
        json.dump(applicants, f)

# Function to verify applicant email and password
def verify_applicant(email, password):
    with open(APPLICANT_TABLE_PATH, 'r') as f:
        applicants = json.load(f)
        for applicant in applicants:
            if applicant["email"] == email and applicant["password"] == password:
                return True
    return False

# Function to add a post
def add_post(title, description, pay, due_date, location, owner):
    post_date = datetime.now().strftime("%Y-%m-%d")
    post_id = str(uuid.uuid4())  # Generate unique ID for the post
    post = Post(post_id, title, description, pay, post_date, due_date, location, owner)
    with open(POSTS_TABLE_PATH, 'r+') as f:
        posts = json.load(f)
        posts.append(post.to_dict())
        f.seek(0)
        json.dump(posts, f)
    return post.id

# Function to add applicant email to a post's applicant list
def add_applicant_to_post(post_id, applicant_email):
    with open(POSTS_TABLE_PATH, 'r+') as f:
        posts = json.load(f)
        for post in posts:
            if post["id"] == post_id:
                if applicant_email not in post["applicants"]:
                    post["applicants"].append(applicant_email)
                break
        f.seek(0)
        json.dump(posts, f)

# Function to get all applicant information for a specific post
def get_applicants_for_post(post_id):
    with open(POSTS_TABLE_PATH, 'r') as f:
        posts = json.load(f)
        for post in posts:
            if post["id"] == post_id:
                return post["applicants"]
    return []

# Testing and example usage (uncomment to run)
# recruiter = Recruiter("John", "Doe", "recruiter@example.com", "password123", "TechCorp", "123-456-7890")
# add_recruiter(recruiter)
# applicant = Applicant("Jane", "Smith", "applicant@example.com", "password456", "resume.pdf", "098-765-4321")
# add_applicant(applicant)
# post_id = add_post("Software Engineer", "Job description", "100000", "2024-12-31", "Toronto", "recruiter@example.com")
# add_applicant_to_post(post_id, "applicant@example.com")
# print(get_applicants_for_post(post_id))