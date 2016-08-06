import motor
from bson import ObjectId
from tornado.ioloop import IOLoop
from time import *

def _run(func):
    def _init(*args,**kargs):
        dbhelper.instance.result = None
        res =  func(*args,**kargs)
        IOLoop.instance().start()
        if '_id' in kargs:
            kargs['_id'] = ObjectId(kargs['_id'])
        if dbhelper.instance.result:
            return dbhelper.instance.result
    return _init

def _insert(func):
    def _init(*args,**kargs):
        time_struct = gmtime()
        kargs['time'] ={
            'year':time_struct.tm_year,
            'mon':time_struct.tm_mon,
            'day':time_struct.tm_yday,
            'week':time_struct.tm_wday,
            'date':ctime(mktime(time_struct))
        }
        return func(*args,**kargs)
    return _init



class dbhelper(object):
    connections = {}
    instance=None
    dbs = []
    def __init__(self,document,debug=False,ip="127.0.0.1"):
        self.client = motor.MotorClient('mongodb://%s:27017'%ip)
        self._db = self.client[document]
        
        dbhelper.instance  = self
        dbhelper.dbs.append(self._db)
        dbhelper.connections[document] =  self.client
        self.debug = debug

        self.document = document 
    def __del__(self):
        self.client.close()
        del dbhelper.connections[self.document]
        
        self.log("connection colosed ")

    @_run
    def find_one(self,document,**kargs):
        self._db[document].find_one(kargs,callback=self.callback)

    @_run
    @_insert
    def insert(self,document,**kargs):
        self._db[document].insert(kargs,callback=self.callback)

    @_run
    def find(self,document,length=10,**kargs):
        self.log(kargs)
        count = length
        self.log(document)
        self._db[document].find(kargs).to_list(length=count,callback=self.callback)


    @_run
    def remove(self,document,**kargs):
        self._db[document].remove(kargs,callback=self.callback)

    @_run
    def update(self,document,target,**kargs):
        self._db[document].update(target,kargs,callback=self.callback)
        

    # def to_list_callback(self,infos,error):
    def log(self,msg):
        if self.debug:
            print ("[{}] :{}".format(asctime(),msg))

    def callback(self,info,error):
        if error:
            print ("[err ]: {}".format(error))
        else:
            self.result = info

        IOLoop.instance().stop()

    def set_callback(self,ufun):
        self.callback = ufun
    

if __name__ == '__main__':
    main()
