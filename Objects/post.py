
class Post:
    def __init__(self, id, title, description, pay, post_date, due_date):
        self.id = id
        self.title = title
        self.description = description
        self.pay = pay
        self.post_date = post_date
        self.due_date = due_date
        self.applicants = ()

    def close_post(self):
        """ Close the post earlier than the "due_date". Post would automatically close in "due_date".
        """
        pass
