#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os,hashlib,time

from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_uploads import UploadSet, configure_uploads, ALL
from oa_model import objMysql

app = Flask(__name__)


#*************up load file***********
strUploadPath = 'uploads/'
strUploadDir = 'NewPics'
files = UploadSet(strUploadDir, ALL)
app.config['UPLOADS_DEFAULT_DEST'] = strUploadPath

configure_uploads(app, files)


@app.before_request
def beforeRequest():
    #print "beforeRequest"
    isOK = objMysql.connect()
    if not isOK :
        return "error"

@app.teardown_request
def teardownRequest(exception):
    #print "teardown_request"
    objMysql.close()

@app.errorhandler(500)
def page_not_found(error):
    return "sorry,server_exception",500

@app.route('/')
@app.route('/index')
def home():
    return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    #print "login"
    if request.method == 'POST':
        strUserName = request.form['loginuser']
        strPW = request.form['loginpwd']
        userData = objMysql.getExecuteResult("select UserName,Password,Email,Phone,SigninDate,Activated,extend from users where UserName='%s';" % strUserName)

        if userData:
            if userData[0][1] == strPW:
                return make_response(render_template('index.html', title='首页'))
            else:
                return redirect(url_for('login'))
        else:
            pass
            #print "null"
    else:
        return make_response(render_template('login.html', title='login'))

@app.route('/dataStatistics',methods=['GET','POST'])
def dataStatistics():
    #print "datasss"
    return render_template('Download-pic.html',title='data')


@app.route('/head',methods=['GET'])
def headHtml():
    #print "head"
    return render_template('head.html',title='head')

@app.route('/left',methods=['GET'])
def leftHtml():
    #print "left"
    return render_template('left.html',title='left')

@app.route('/main',methods=['GET'])
def mainHtml():
    #print "main"
    return render_template('main.html',title='main')


#****************start***************
@app.route('/test',methods=['GET'])
def testHtml():
    #print "test"
    return render_template('test.html',title='test')
@app.route('/testOne',methods=['GET'])
def testOneHtml():
    #print "testOne"
    return render_template('test-one.html',title='test')
@app.route('/testTwo',methods=['GET'])
def testTwoHtml():
    #print "testTwo"
    return render_template('test-two.html',title='test')
#****************end***************


#****************start***************
@app.route('/Dangan',methods=['GET'])
def DanganHtml():
    #print "Dangan"
    return render_template('Dangan.html',title='Dangan')
@app.route('/DanganAdd',methods=['GET'])
def DanganAddHtml():
    #print "DanganAdd"
    return render_template('Dangan-add.html',title='Dangan')
@app.route('/DanganEdit',methods=['GET'])
def DanganEditHtml():
    #print "Dangan"
    return render_template('Dangan-edit.html',title='Dangan')
@app.route('/DanganLook',methods=['GET'])
def DanganLookHtml():
    #print "Dangan"
    return render_template('Dangan-look.html',title='Dangan')


@app.route('/ShujuOne',methods=['GET'])
def ShujuOneHtml():
    #print "Dangan"
    return render_template('Shuju-one.html',title='Dangan')
@app.route('/ShujuTwo',methods=['GET'])
def ShujuTwoHtml():
    #print "Dangan"
    return render_template('Shuju-two.html',title='Dangan')
#****************end***************



#****************start***************
@app.route('/UserManagement',methods=['GET'])
def UserManagementHtml():
    #print "Dangan"
    return render_template('User_management.html',title='UserManagement')

@app.route('/UserManagementAdd',methods=['GET'])
def UserManagementAddHtml():
    #print "Dangan"
    return render_template('user_management_add.html',title='UserManagement')
#****************end***************




#****************start***************
@app.route('/RoleManagement',methods=['GET'])
def RoleManagementHtml():
    #print "Dangan"
    return render_template('Role_management.html',title='RoleManagement')
@app.route('/RoleManagementAdd',methods=['GET'])
def RoleManagemenAddtHtml():
    #print "Dangan"
    return render_template('role_management_add.html',title='RoleManagement')
@app.route('/RoleManagementEdit',methods=['GET'])
def RoleManagementEditHtml():
    #print "Dangan"
    return render_template('role_management_edit.html',title='RoleManagement')
#****************end***************

@app.route('/WarningManagement',methods=['GET'])
def WarningManagementHtml():
    #print "Dangan"
    return render_template('Warning_management.html',title='Dangan')

@app.route('/DataManagement',methods=['GET'])
def DataManagementHtml():
    #print "Dangan"
    return render_template('Data_management.html',title='Dangan')

@app.route('/shujutongji',methods=['GET'])
def shujutongjiHtml():
    #print "Dangan"
    return render_template('shujutongji.html',title='Dangan')



#****************start***************

@app.route('/Home',methods=['GET'])
def HomeHtml():
    #print "Dangan"
    return render_template('Home.html',title='Dangan')
@app.route('/HomeAdd',methods=['GET'])
def HomeAddHtml():
    #print "Dangan"
    return render_template('home_add.html',title='Dangan')
#****************end***************


#****************start***************
@app.route('/AboutUs',methods=['GET'])
def AboutUsHtml():
    #print "Dangan"
    return render_template('About_us.html',title='Dangan')
@app.route('/AboutUsAdd',methods=['GET'])
def AboutUsAddHtml():
    #print "Dangan"
    return render_template('about_us_add.html',title='Dangan')
#****************end***************


#****************start***************

@app.route('/New',methods=['GET'])
def NewHtml():
    #print "NewHtml"
    newList = objMysql.getExecuteResult("select * from newList")
    return render_template('New.html',title='new',newList=newList)

@app.route('/NewAdd',methods=['GET','POST'])
def NewAddHtml():
    #print "NewAddHtml"
    return render_template('new_add.html',title='Dangan')

@app.route('/NewEdit/<int:oneNewID>',methods=['GET','POST'])
def NewEditHtml(oneNewID):
    #print "NewEditHtml"
    newOne = objMysql.getExecuteResult("select * from newList where NewID = %d" %oneNewID)
    return render_template('new_edit.html',title='Dangan',newOne=newOne[0])

@app.route('/update/<int:newID>', methods=['GET', 'POST'])
def update(newID):
    #print "update"
    if request.method == 'POST' :
        if "addModuleNew" in request.form and "addTitleNew" in request.form  :
            nAddModule = int(request.form['addModuleNew'])
            strAddTitle = request.form['addTitleNew']
            strAddContent = request.form['addContentNew']
            strSqlCMD = ""

            if  'media' in request.files:
                strAddPicName = request.files['media'].filename
                strAddPicNamemd5 = hashlib.md5(strAddPicName+str(int(time.time())).encode('utf-8')).hexdigest()
                strFilePath = os.getcwd()+'/'+strUploadPath+strUploadDir

                filename = files.save(request.files['media'],"",strAddPicNamemd5)
                strPicUrl = files.url(filename)

                strSqlCMD = "update newList set NewModule='%s',NewTitle='%s',NewPicName='%s',NewPicNameMD5='%s',NewPicPath='%s',NewPicUrl='%s',NewContent='%s' where NewID = %d" % \
                             (nAddModule,strAddTitle.encode('utf-8'), strAddPicName.encode('utf-8'),strAddPicNamemd5, strFilePath,strPicUrl,strAddContent.encode('utf-8'),newID)
            else:
                strSqlCMD = "update newList set NewModule='%s',NewTitle='%s',NewContent='%s' where NewID = %d" % \
                            (nAddModule,strAddTitle.encode('utf-8'),strAddContent.encode('utf-8'),newID)

            objMysql.commitExecute(strSqlCMD)

            return render_template('New.html')

        else:
            #print "read error........................"
            return render_template('new_edit.html')

@app.route('/delNew/<int:newID>', methods=['GET', 'POST'])
def delNew(newID):
    #print "delNew"

    strSqlCMD = "delete from newList where NewID = %d" % newID
    objMysql.commitExecute(strSqlCMD)

    return redirect(url_for('NewHtml'))

@app.route('/newDel', methods=['GET', 'POST'])
def newDel(newID):
    #print "newDel"
    return render_template('New.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' :
        if "addModuleNew" in request.form and "addTitleNew" in request.form and 'media' in request.files :

            nAddModule = int(request.form['addModuleNew'])
            strAddTitle = request.form['addTitleNew']
            strAddPicName = request.files['media'].filename
            strAddContent = request.form['addContentNew']
            strAddPicNamemd5 = hashlib.md5(strAddPicName+str(int(time.time())).encode('utf-8')).hexdigest()
            strFilePath = os.getcwd()+'/'+strUploadPath+strUploadDir

            filename = files.save(request.files['media'],"",strAddPicNamemd5)
            strPicUrl = files.url(filename)

            strSqlCMD = "insert into newList(NewModule,NewTitle,NewPicName,NewPicNameMD5,NewPicPath,NewPicUrl,NewContent,NewState) " + \
                        "value('%d','%s','%s','%s','%s','%s','%s',%d) " % (nAddModule, strAddTitle.encode('utf-8'), strAddPicName.encode('utf-8'), \
                                                                      strAddPicNamemd5, strFilePath,strPicUrl,strAddContent.encode('utf-8'),1)

            objMysql.commitExecute(strSqlCMD)
            return render_template('New.html')

        else:
            #print "read error"
            return render_template('new_add.html')


#****************end***************


#****************start***************
@app.route('/DownloadPic',methods=['GET'])
def DownloadPicHtml():
    #print "Dangan"
    return render_template('Download-pic.html',title='Dangan')
@app.route('/DownloadPicAdd',methods=['GET'])
def DownloadPicAddHtml():
    #print "Dangan"
    return render_template('download_picadd.html',title='Dangan')
@app.route('/DownloadPicEdit',methods=['GET'])
def DownloadPicEidtHtml():
    #print "Dangan"
    return render_template('download_picedit.html',title='Dangan')


@app.route('/DownloadBook',methods=['GET'])
def DownloadBookHtml():
    #print "Dangan"
    return render_template('Download-book.html',title='Dangan')
@app.route('/DownloadBookAdd',methods=['GET'])
def DownloadBookAddHtml():
    #print "Dangan"
    return render_template('download_bookadd.html',title='Dangan')
@app.route('/DownloadBookEdit',methods=['GET'])
def DownloadBookEditHtml():
    #print "Dangan"
    return render_template('download_bookedit.html',title='Dangan')


@app.route('/DownloadVoid',methods=['GET'])
def DownloadVoidHtml():
    #print "Dangan"
    return render_template('Download-void.html',title='Dangan')
@app.route('/DownloadVoidAdd',methods=['GET'])
def DownloadVoidAddHtml():
    #print "Dangan"
    return render_template('download_voidadd.html',title='Dangan')
@app.route('/DownloadVoidEdit',methods=['GET'])
def DownloadVoidEditHtml():
    #print "Dangan"
    return render_template('download_voidedit.html',title='Dangan')
#****************end***************

@app.route('/link',methods=['GET'])
def linkHtml():
    #print "link"
    return render_template('link.html',title='Dangan')


