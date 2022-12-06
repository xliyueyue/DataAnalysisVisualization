from config import db

class JhEdition(db.Model):
    __tablename__ = "jh_edition"
    id = db.Column(db.Integer, primary_key=True)
    edition = db.Column(db.String(50))
    count = db.Column(db.Integer)

class XdfType(db.Model):
    __tablename__ = "xdf_type"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    count = db.Column(db.Integer)
    per_price = db.Column(db.DECIMAL)

class Xdf(db.Model):
    __tablename__ = "xdf"
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(50))
    count = db.Column(db.Integer)
    price = db.Column(db.DECIMAL)

class Jh(db.Model):
    __tablename__ = "jh"
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(50))
    count = db.Column(db.Integer)
    price = db.Column(db.DECIMAL)

class TGrade(db.Model):
    __tablename__ = "t_grade"
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(50))
    count = db.Column(db.Integer)
    price = db.Column(db.DECIMAL)

class TCourse(db.Model):
    __tablename__ = "t_course"
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(50))
    count = db.Column(db.Integer)
    price = db.Column(db.DECIMAL)

class TMaterial(db.Model):
    __tablename__ = "t_material"
    id = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String(50))
    count = db.Column(db.Integer)
    download = db.Column(db.Integer)
    collection = db.Column(db.Integer)

