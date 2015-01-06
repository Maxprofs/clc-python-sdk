"""
Server related functions.  

These server related functions generally align one-for-one with published API calls categorized in the account category

API v2 - https://t3n.zendesk.com/forums/21613150-Servers

Server object variables:

	#group.id
	#group.name
	#group.description
	#group.type
	#group.status
	#group.serverCount

"""



import json
import clc

class Server(object):

	@staticmethod
	def GetAll(root_group_id,alias=None):  
		"""Gets a list of groups within a given account.

		"""

		if not alias:  alias = clc.v2.Account.GetAlias()

		groups = []
		for r in clc.v2.API.Call('GET','groups/%s/%s' % (alias,root_group_id),{})['groups']:
			groups.append(Group(id=r['id'],alias=alias,group_obj=r))
		
		return(groups)



	def __init__(self,id,alias=None,group_obj=None):
		"""Create Group object.

		If parameters are populated then create object location.  
		Else if only id is supplied issue a Get Policy call

		>>> clc.v2.Group(id="wa1-1798")
		<clc.APIv2.group.Group object at 0x109188b90>

		"""

		self.id = id

		if alias:  self.alias = alias
		else:  self.alias = clc.v2.Account.GetAlias()

		if group_obj:  self.data = group_obj
		else:  self.data = clc.v2.API.Call('GET','groups/%s/%s' % (self.alias,self.id),{})


	def __getattr__(self,var):
		if var in self.data:  return(self.data[var])
		else:  raise(AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__,var)))


	def Create(self,name,description=None):  
		"""Creates a new group

		*TODO* API not yet documented

		>>> clc.v2.Datacenter(location="WA1").RootGroup().Create("Test3","Description3")
		Request: https://api.tier3.com/v2/groups/BTDI
		payload={'parentGroupId': u'wa1-837', 'name': 'Test3', 'description': 'Description3'}
		Response: status_code: 400
		{"message":"The 'name' property is required."}

		"""

		if not description:  description = name

		#clc.v2.API.Call('POST','groups/%s' % (self.alias),{'name': name, 'description': description, 'parentGroupId': self.id},debug=True)
		raise(Exception("Not implemented"))


	def Update(self):
		"""Update group

		*TODO* API not yet documented

		"""
		raise(Exception("Not implemented"))


	def Delete(self):
		"""Delete group."""
		#status = {u'href': u'/v2/operations/btdi/status/wa1-126437', u'id': u'wa1-126437', u'rel': u'status'}
		status = clc.v2.API.Call('DELETE','groups/%s/%s' % (self.alias,self.id),{})


	def __str__(self):
		return(self.data['name'])

