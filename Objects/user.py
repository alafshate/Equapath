
class User:
    def __init__(self, first_name, last_name, email, password) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class Applicant(User):
    def __init__(self, first_name, last_name, email, password, resume, phone_number) -> None:
        super().__init__(first_name, last_name, email, password)
        self.resume = resume
        self.phone_number = phone_number


class Recruiter(User):
    def __init__(self, first_name, last_name, email, password, company) -> None:
        super().__init__(first_name, last_name, email, password)
        self.company = company
        self.posts = ()
