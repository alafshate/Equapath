
class User:
    def __init__(self, first_name, last_name, email, password, phone_number) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number


class Applicant(User):
    def __init__(self, first_name, last_name, email, password, resume, phone_number) -> None:
        super().__init__(first_name, last_name, email, password, phone_number)
        self.resume = resume
        self.posts = []

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "phone_number": self.phone_number,
            "resume": self.resume,
            "posts": self.posts
        }


class Recruiter(User):
    def __init__(self, first_name, last_name, email, password, company, phone_number) -> None:
        super().__init__(first_name, last_name, email, password, phone_number)
        self.company = company
        self.posts = []

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "phone_number": self.phone_number,
            "company": self.company,
            "posts": self.posts
        }
