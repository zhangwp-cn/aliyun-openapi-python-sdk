# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkros.endpoint import endpoint_data

class ContinueCreateStackRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ROS', '2019-09-10', 'ContinueCreateStack','ROS')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TemplateBody(self):
		return self.get_query_params().get('TemplateBody')

	def set_TemplateBody(self,TemplateBody):
		self.add_query_param('TemplateBody',TemplateBody)

	def get_StackId(self):
		return self.get_query_params().get('StackId')

	def set_StackId(self,StackId):
		self.add_query_param('StackId',StackId)

	def get_TemplateURL(self):
		return self.get_query_params().get('TemplateURL')

	def set_TemplateURL(self,TemplateURL):
		self.add_query_param('TemplateURL',TemplateURL)

	def get_Mode(self):
		return self.get_query_params().get('Mode')

	def set_Mode(self,Mode):
		self.add_query_param('Mode',Mode)

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_RamRoleName(self):
		return self.get_query_params().get('RamRoleName')

	def set_RamRoleName(self,RamRoleName):
		self.add_query_param('RamRoleName',RamRoleName)

	def get_Parameterss(self):
		return self.get_query_params().get('Parameterss')

	def set_Parameterss(self,Parameterss):
		for i in range(len(Parameterss)):	
			if Parameterss[i].get('ParameterValue') is not None:
				self.add_query_param('Parameters.' + str(i + 1) + '.ParameterValue' , Parameterss[i].get('ParameterValue'))
			if Parameterss[i].get('ParameterKey') is not None:
				self.add_query_param('Parameters.' + str(i + 1) + '.ParameterKey' , Parameterss[i].get('ParameterKey'))


	def get_RecreatingResourcess(self):
		return self.get_query_params().get('RecreatingResourcess')

	def set_RecreatingResourcess(self,RecreatingResourcess):
		for i in range(len(RecreatingResourcess)):	
			if RecreatingResourcess[i] is not None:
				self.add_query_param('RecreatingResources.' + str(i + 1) , RecreatingResourcess[i]);