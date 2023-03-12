from gpt.chat_context import ChatContext

class User:
    '''User model'''

    username = None
    business_name = None
    bio = None
    services = []

    def __init__(self, username, business_name=None, bio=None, services=[]):
        self.username = username
        self.business_name = business_name
        self.bio = bio
        self.services = services

    def get_context(self):
        context = ChatContext()
        return context.add_question(f"""
My name is {self.username}
My business name is {self.business_name}
My bio is :
{self.bio}

My services are:    
{', '.join(self.services)}
        """
        )





        