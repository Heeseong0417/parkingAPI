import pymysql
from config.config import db as con
class parkingDAO:

    def __init__(self):
        pass
    
    def getAll(self,table):
        ret = []
        db = pymysql.connect(host=con['host'], user=con['user'], db= con['database'],port=con['port'], password=con['password'], charset='utf8')
        curs = db.cursor(pymysql.cursors.DictCursor)
        
        sql = "select * from {table}".format(table=table)
        curs.execute(sql)
        
        rows = curs.fetchall()
        for e in rows:
            #temp = {'empno':e[0],'name':e[1],'department':e[2],'phone':e[3] }
            ret.append(e)
        
        db.commit()
        db.close()
        return ret
    def get_list(self,table,key,value):
        ret = []
        db = pymysql.connect(host=con['host'], user=con['user'], db= con['database'],port=con['port'], password=con['password'], charset='utf8')
        curs = db.cursor(pymysql.cursors.DictCursor)
        
        sql = "select * from {table} where {key}='{value}'".format(table=table,key=key,value=value)
        print(sql)
        curs.execute(sql)
        
        rows = curs.fetchall()
        for e in rows:
            #temp = {'empno':e[0],'name':e[1],'department':e[2],'phone':e[3] }
            ret.append(e)
        
        db.commit()
        db.close()
        print(ret)
        return ret

    def siteIn(self,table,id_key,id):
        ret = []
        db = pymysql.connect(host=con['host'], user=con['user'], db= con['database'],port=con['port'], password=con['password'], charset='utf8')
        curs = db.cursor(pymysql.cursors.DictCursor)
        
        sql = "select * from {table} where {id_key}='{id}' ".format(table=table,id_key=id_key,id=id)
        print(sql)
        curs.execute(sql)
        
        rows = curs.fetchall()
        for e in rows:
            #temp = {'empno':e[0],'name':e[1],'department':e[2],'phone':e[3] }
            ret.append(e)
        
        db.commit()
        db.close()
       
        return ret
    def siteUp(self, table,keys,values):
        tf = False
        print("keys : ",keys," values : ",values)
        db = pymysql.connect(host=con['host'], user=con['user'], db= con['database'],port=con['port'], password=con['password'], charset='utf8')
        curs = db.cursor()
        
        sql = "insert into {table} ({keys}) values({values})".format(table=table,keys=keys,values=values)
        print(sql)

        try:
            tf=True
            curs.execute(sql)
            db.commit()
        except Exception as e:
            print(str(e))
            tf = False
        
        db.close()
        return tf

    def insEmp(self, empno, name, department,phone):
        db = pymysql.connect(host=con['host'], user=con['user'], db= con['database'],port=con['port' ], password=con['password'], charset='utf8')
        curs = db.cursor()
        
        sql = '''insert into emp (empno, name, department, phone) values(%s,%s,%s,%s)'''
        curs.execute(sql,(empno, name, department,phone))
        db.commit()
        db.close()
    
    def updEmp(self, empno, name, department,phone): 
        db = pymysql.connect(host=con['host'], user=con['user'], db= con['database'],port=con['port'], password=con['password'], charset='utf8')
        curs = db.cursor()
        
        sql = "update emp set name=%s, department=%s, phone=%s where empno=%s"
        curs.execute(sql,(name, department, phone, empno))
        db.commit()
        db.close()
    def delEmp(self, empno):
        db = pymysql.connect(host=con['host'], user=con['user'], db= con['database'],port=con['port'], password=con['password'], charset='utf8')
        curs = db.cursor()
        
        sql = "delete from emp where empno=%s"
        curs.execute(sql,empno)
        db.commit()
        db.close()
 
#if __name__ == '__main__':
    
    #MyEmpDao().insEmp('aaa', 'bb', 'cc', 'dd')
    #MyEmpDao().updEmp('aa', 'dd', 'dd', 'aa')
    #MyEmpDao().delEmp('aaa')

