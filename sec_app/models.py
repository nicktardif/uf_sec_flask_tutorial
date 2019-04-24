from sec_app import db

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    def __init__(self, name):
        self.name = name

    def toJSON(self):
        return {
            'id': self.id,
            'name': self.name
        }
