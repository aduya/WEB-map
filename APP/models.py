from APP import db
from datetime import datetime, timedelta

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username=db.Column(db.String(64),index = True,unique = True)#网站用户名
    password = db.Column(db.String(126))#网站密码

    def is_authenticated(self):
        return True
    #is_authenticated 方法有一个具有迷惑性的名称。一般而言，这个方法应该只返回 True，除非表示用户的对象因为某些原因不允许被认证。

    def is_active(self):
        return True
    #is_active 方法应该返回 True，除非是用户是无效的，比如因为他们的账号是被禁止。

    def is_anonymous(self):
        return False
    #is_anonymous 方法应该返回 True，除非是伪造的用户不允许登录系统。

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def verify_password(self, password):
        #对比用户密码
        if self.password==password:
            return True
        else:
            return False
    def __repr__(self):
        return '<User %r>' % (self.username)

class Case(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    markerxy=db.Column(db.String(64))#坐标
    place = db.Column(db.String(64))#地名
    Casetype = db.Column(db.String(64))#类型
    Casework = db.Column(db.String(64))#详细
    Casenote = db.Column(db.String(64))#备注
    Casetime = db.Column(db.DateTime)  #时间
    Showpic = db.Column(db.String(64),default='default.png')#备注

    def save(self):
        db.session.add(self)
        db.session.commit()

    def GetCase_time(self,day):
        NOW = datetime.now()
        case=Case.query.filter(Case.Casetime>NOW - timedelta(days=day)).order_by(Case.Casetime.desc())
        cases=[]
        for n in case:
            cases.append({
            "pic": n.Showpic,
            "price": '''
           <font color="#FF0000">%s</font>     <input value="上传图片" id="updatapic%s" type="button">
            '''%(n.place,n.id),
            "name": '%s   %s'%(n.Casetype,(n.Casetime).strftime("%m-%d %H:%M")),
            "address": '%s。备注:%s'%(n.Casework,n.Casenote),
            "id": "%s"%n.id,
            "latitude": (n.markerxy).split(',')[1],
            "longitude": (n.markerxy).split(',')[0]
            })
        return cases

    def Advanced_search(self,Casetype,StartCasetime,StopCasetime,Casenote):
        if Casetype!='' and Casenote!='':
           print(1)
           case=Case.query.filter(Case.Casetype==Casetype,Case.Casetime>StartCasetime,Case.Casetime<StopCasetime,Case.Casenote.like("%"+Casenote+"%")).order_by(Case.Casetime.desc())
        elif Casetype=='' and Casenote!='':
            print(2)
            case = Case.query.filter(Case.Casetime > StartCasetime,Case.Casetime < StopCasetime, Case.Casenote.like("%" + Casenote + "%")).order_by(Case.Casetime.desc())
        elif Casetype!='' and Casenote=='':
            print(3)
            case = Case.query.filter(Case.Casetype==Casetype,Case.Casetime > StartCasetime,Case.Casetime < StopCasetime).order_by(Case.Casetime.desc())
        else:
            case = Case.query.filter(Case.Casetime > StartCasetime,Case.Casetime < StopCasetime).order_by(Case.Casetime.desc())
        cases=[]
        for n in case:
            cases.append({
            "pic": n.Showpic,
            "price": '''
           <font color="#FF0000">%s</font>     <input value="上传图片" id="updatapic%s" type="button">
            '''%(n.place,n.id),
            "name": '%s   %s'%(n.Casetype,(n.Casetime).strftime("%m-%d %H:%M")),
            "address": '%s。备注:%s'%(n.Casework,n.Casenote),
            "id": "%s"%n.id,
            "latitude": (n.markerxy).split(',')[1],
            "longitude": (n.markerxy).split(',')[0]
            })
        return cases

    def __repr__(self):
        return '<Case %r>' % (self.id)
