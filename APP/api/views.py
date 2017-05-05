from flask_login import login_required
from flask import jsonify,redirect,url_for,request
from . import api
from ..models import Case
from datetime import datetime


@api.route('/map/data/recently<day>.json',methods=['GET'])
@login_required
def map_recently(day):
    return jsonify(
        Case().GetCase_time(int(day))
    )

#search
@api.route('/map/data/search',methods=['GET'])
@login_required
def search():
    Casetype=request.args.get('Casetype','')
    StartCasetime = request.args.get('StartCasetime')
    StartCasetime = datetime.strptime(StartCasetime, '%Y-%m-%dT%H:%M')
    StopCasetime = request.args.get('StopCasetime')
    StopCasetime = datetime.strptime(StopCasetime, '%Y-%m-%dT%H:%M')
    Casenote = request.args.get('Casenote','')
    return jsonify(Case().Advanced_search(Casetype,StartCasetime,StopCasetime,Casenote))


@api.route('/map/data/updata_img',methods=['POST'])
@login_required
def updataimg():
    return jsonify({
        'result':'1',
        'msg':'上传成功'
    })

@api.route('/map/data/updata_case',methods=['POST'])
@login_required
def updatacase():
    markerxy = request.form['markerxy']
    place = request.form['place']
    Casetype = request.form['Casetype']
    Casework = request.form['Casework']
    Casenote = request.form['Casenote']
    Casetime = request.form['Casetime']
    Casetime = datetime.strptime(Casetime, '%Y-%m-%dT%H:%M')
    case=Case(
        markerxy=markerxy,
        place=place,
        Casetype=Casetype,
        Casework=Casework,
        Casenote=Casenote,
        Casetime=Casetime)
    case.save()
    return jsonify({
        'result':'1',
        'msg':'上传成功'
    })
