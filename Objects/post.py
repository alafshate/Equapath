
class Post:
    def __init__(self, id, title, description, pay, post_date, due_date, location, owner):
        self.id = id
        self.title = title
        self.description = description
        self.pay = pay
        self.post_date = post_date
        self.due_date = due_date
        self.applicants = []
        self.location = location
        self.owner = owner

    def close_post(self):
        """ Close the post earlier than the "due_date". Post would automatically close in "due_date".
        """
        pass

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "pay": self.pay,
            "post_date": self.post_date,
            "due_date": self.due_date,
            "applicants": self.applicants,
            "location": self.location,
            "owner_email": self.owner_email
        }