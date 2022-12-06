import json
from flask import Blueprint
from config import db
from dbmode.modes import JhEdition, XdfType, TCourse, TGrade, TMaterial

data = Blueprint("data", __name__)

@data.route("/get_jh_edition", endpoint="get_jh_edition")
def get_jh_edition():
    data = db.session.query(JhEdition).all()
    view_data ={}
    view_data["series"] = []

    def build_view_data(item):
        tmp_dic={}
        tmp_dic["value"] = item.count
        tmp_dic["name"] = item.edition
        view_data["series"].append(tmp_dic)

    [build_view_data(item) for item in data]
    return json.dumps(view_data, ensure_ascii=False)

@data.route("/get_xdf_type", endpoint="get_xdf_type")
def get_xdf_type():
    data = db.session.query(XdfType).all()
    view_data ={}
    view_data["series_data"] = []

    def build_view_data(item):
        tmp_dic={}
        tmp_dic["type"] = item.type
        tmp_dic["price"] = item.per_price
        tmp_dic["count"] = item.count
        if item.type != "None":
            view_data["series_data"].append(tmp_dic)

    [build_view_data(item) for item in data]
    return json.dumps(view_data, ensure_ascii=False)

@data.route("/get_all", methods=["GET"])
def get_all():
    data1 = db.session.query(TCourse).all()
    view_data ={}
    view_data["series_data"] = []

    def build_view_data(item):
        tmp_dic = {}
        tmp_dic["course"] = item.course
        tmp_dic["price"] = item.price
        tmp_dic["count"] = item.count
        view_data["series_data"].append(tmp_dic)

    [build_view_data(item) for item in data1]
    return json.dumps(view_data, ensure_ascii=False)

@data.route("/get_name", methods=["GET"])
def get_name():
    data1 = db.session.query(TCourse).all()
    view_data ={}
    view_data["series"] = []

    def build_view_data(item):
        view_data["series"].append(item.course)

    [build_view_data(item) for item in data1]
    return json.dumps(view_data, ensure_ascii=False)

@data.route("/get_grade_count", methods=["GET"])
def get_grade_count():
    data1 = db.session.query(TGrade).all()
    view_data ={}
    view_data["series_data"] = []

    def build_view_data(item):
        tmp_dic = {}
        tmp_dic["grade"] = item.grade
        tmp_dic["count"] = item.count
        view_data["series_data"].append(tmp_dic)

    [build_view_data(item) for item in data1]
    return json.dumps(view_data, ensure_ascii=False)

@data.route("/get_course_count", methods=["GET"])
def get_course_count():
    data1 = db.session.query(TCourse).all()
    view_data ={}
    view_data["series"] = []

    def build_view_data(item):
        tmp_dic = {}
        tmp_dic["name"] = item.course
        tmp_dic["value"] = item.count
        view_data["series"].append(tmp_dic)

    [build_view_data(item) for item in data1]
    return json.dumps(view_data, ensure_ascii=False)

@data.route("/get_grade_price", methods=["GET"])
def get_grade_price():
    data1 = db.session.query(TGrade).all()
    view_data ={}
    view_data["series"] = []

    def build_view_data(item):
        tmp_dic = {}
        tmp_dic["name"] = item.grade
        tmp_dic["value"] = item.price
        view_data["series"].append(tmp_dic)

    [build_view_data(item) for item in data1]
    return json.dumps(view_data, ensure_ascii=False)

@data.route("/get_material_count", methods=["GET"])
def get_material_count():
    data1 = db.session.query(TMaterial).all()
    view_data ={}
    view_data["series"] = []

    def build_view_data(item):
        tmp_dic = {}
        tmp_dic["name"] = item.material
        tmp_dic["value"] = item.count
        view_data["series"].append(tmp_dic)

    [build_view_data(item) for item in data1]
    return json.dumps(view_data, ensure_ascii=False)
