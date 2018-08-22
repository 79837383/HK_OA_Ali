#-*- coding: utf-8 -*-

from setting import objConfig
import MySQLdb

class MysqlControl():
    def __init__(self,strSQLIP, strDBUserName, strDBPassword, strDBName):
        self.strSQLIP=strSQLIP
        self.strDBUser = strDBUserName
        self.strDBPWD = strDBPassword
        self.strDBName = strDBName
        self.IsConnected = False

    def connect(self):
        try:
            #print "connect db"
            self.sqlConn = MySQLdb.connect(self.strSQLIP, self.strDBUser, self.strDBPWD, self.strDBName)
            self.sqlConn.set_character_set('utf8')
            self.sqlCur = self.sqlConn.cursor()
            self.sqlCur.execute('set names utf8mb4;')
            self.sqlCur.execute('set character_set_connection=utf8;')
            self.IsConnected = True
            return self.IsConnected,"ok"
        except MySQLdb.Error, e:
            self.IsConnected = False
            return self.IsConnected,e

    def getExecuteResult(self,strCMD):
        if self.IsConnected:
            self.sqlCur.execute(strCMD)
            return self.sqlCur.fetchall()
        else:
            return ""

    def commitExecute(self,strCMD):
        if self.IsConnected:
            self.sqlCur.execute(strCMD)
            self.sqlConn.commit()
            return True
        else:
            return False


    def close(self):
        if self.IsConnected:
            try:
                #print "close db"
                self.sqlCur.close()
                self.sqlConn.close()
            except MySQLdb.Error, e:
                pass
        self.IsConnected = False

objMysql = MysqlControl(objConfig.strSQLIP,objConfig.strDBUserName,objConfig.strDBPassword,objConfig.strDBName)