from cassandra.cluster import Cluster
from datetime import datetime, timedelta

class CassieUtilities(object):

    def __init__(self, ip_addr='52.8.124.34', keyspace='outbound_cassandra'):
        cluster = Cluster([ip_addr])
        self.session = cluster.connect()
        self.session.set_keyspace(keyspace)

    def fetch_daterange(self, table):
        #record_lookup_stmt = "SELECT * FROM {}".format(table)
        record_lookup_stmt = "SELECT * FROM {}".format(table)
  	record_list=[]
	#i=0 
	#while(i<10):     
        record_list = self.session.execute(record_lookup_stmt)
	#	i+=1
        return record_list
         
