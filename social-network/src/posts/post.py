class Post:

    user = None
    text = None
    created_at = None

    def __init__(self, user, text):
        self.user = user
        self.text = text
