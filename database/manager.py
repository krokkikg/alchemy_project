from .models import StudentGroup, Student



class StudentGroupManager():

    def __init__(self, session):
        self.session = session
        self.model = StudentGroup

    def insert_group(self, data):
        group = StudentGroup(
            name=data["name"]
        )
        self.session.add(group)
        self.session.commit()