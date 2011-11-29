""" This is a connection to a Couch. Do I maybe want
http://packages.python.org/CouchDB/client.html or couchdbkit?"""

class Couch():
  "Connection to a Couch"
  def __init__(self):
    self.couch='http://localhost:5984/socialvalue'
  def query_by_user(self,pk):
    "Query the appropriate couch view."
    return '[{"foo":"bar"},{"baz":{"haystack":["hay","hay","hay","needle","hay"]}}]'
  def insert(self,docs):
    "Insert bulk_docs."
    pass
  def query_by_uuid(self,uuid):
    "Query the appropriate couch document."
    return '{"baz":{"haystack":["hay","hay","hay","needle","hay"]}}'
