# QmongoHelper
simplify the  motor for python to use  

##useage
	

	$from mongoHelper import Mongo
	
	$db = Mongo("db_name",ip="127.0.0.1") # default parameter ip is "127.0.0.1" can connect to remote directly

	$db.find("collection_name",**{
			"name":"test",
			# this is whole mongo 's language 	
		})

	$db.insert(collection_name , [,**searcher_option]) #same as find

	$db.update(collection_name, [,**searcher_option])  #same as find

	$db.remove  #same as find 


