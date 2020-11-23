"""Generated client library for dns version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.dns.v1 import dns_v1_messages as messages


class DnsV1(base_api.BaseApiClient):
  """Generated client library for service dns version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://dns.googleapis.com/dns/v1/'
  MTLS_BASE_URL = ''

  _PACKAGE = 'dns'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/cloud-platform.read-only', 'https://www.googleapis.com/auth/ndev.clouddns.readonly', 'https://www.googleapis.com/auth/ndev.clouddns.readwrite']
  _VERSION = 'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'DnsV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new dns handle."""
    url = url or self.BASE_URL
    super(DnsV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.changes = self.ChangesService(self)
    self.dnsKeys = self.DnsKeysService(self)
    self.managedZoneOperations = self.ManagedZoneOperationsService(self)
    self.managedZones = self.ManagedZonesService(self)
    self.policies = self.PoliciesService(self)
    self.projects = self.ProjectsService(self)
    self.resourceRecordSets = self.ResourceRecordSetsService(self)

  class ChangesService(base_api.BaseApiService):
    """Service class for the changes resource."""

    _NAME = 'changes'

    def __init__(self, client):
      super(DnsV1.ChangesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create method for the changes service.

      Args:
        request: (DnsChangesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Change) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='dns.changes.create',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['clientOperationId'],
        relative_path='projects/{project}/managedZones/{managedZone}/changes',
        request_field='change',
        request_type_name='DnsChangesCreateRequest',
        response_type_name='Change',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get method for the changes service.

      Args:
        request: (DnsChangesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Change) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.changes.get',
        ordered_params=['project', 'managedZone', 'changeId'],
        path_params=['changeId', 'managedZone', 'project'],
        query_params=['clientOperationId'],
        relative_path='projects/{project}/managedZones/{managedZone}/changes/{changeId}',
        request_field='',
        request_type_name='DnsChangesGetRequest',
        response_type_name='Change',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List method for the changes service.

      Args:
        request: (DnsChangesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ChangesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.changes.list',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['maxResults', 'pageToken', 'sortBy', 'sortOrder'],
        relative_path='projects/{project}/managedZones/{managedZone}/changes',
        request_field='',
        request_type_name='DnsChangesListRequest',
        response_type_name='ChangesListResponse',
        supports_download=False,
    )

  class DnsKeysService(base_api.BaseApiService):
    """Service class for the dnsKeys resource."""

    _NAME = 'dnsKeys'

    def __init__(self, client):
      super(DnsV1.DnsKeysService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Get method for the dnsKeys service.

      Args:
        request: (DnsDnsKeysGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DnsKey) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.dnsKeys.get',
        ordered_params=['project', 'managedZone', 'dnsKeyId'],
        path_params=['dnsKeyId', 'managedZone', 'project'],
        query_params=['clientOperationId', 'digestType'],
        relative_path='projects/{project}/managedZones/{managedZone}/dnsKeys/{dnsKeyId}',
        request_field='',
        request_type_name='DnsDnsKeysGetRequest',
        response_type_name='DnsKey',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List method for the dnsKeys service.

      Args:
        request: (DnsDnsKeysListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DnsKeysListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.dnsKeys.list',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['digestType', 'maxResults', 'pageToken'],
        relative_path='projects/{project}/managedZones/{managedZone}/dnsKeys',
        request_field='',
        request_type_name='DnsDnsKeysListRequest',
        response_type_name='DnsKeysListResponse',
        supports_download=False,
    )

  class ManagedZoneOperationsService(base_api.BaseApiService):
    """Service class for the managedZoneOperations resource."""

    _NAME = 'managedZoneOperations'

    def __init__(self, client):
      super(DnsV1.ManagedZoneOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Get method for the managedZoneOperations service.

      Args:
        request: (DnsManagedZoneOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.managedZoneOperations.get',
        ordered_params=['project', 'managedZone', 'operation'],
        path_params=['managedZone', 'operation', 'project'],
        query_params=['clientOperationId'],
        relative_path='projects/{project}/managedZones/{managedZone}/operations/{operation}',
        request_field='',
        request_type_name='DnsManagedZoneOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List method for the managedZoneOperations service.

      Args:
        request: (DnsManagedZoneOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ManagedZoneOperationsListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.managedZoneOperations.list',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['maxResults', 'pageToken', 'sortBy'],
        relative_path='projects/{project}/managedZones/{managedZone}/operations',
        request_field='',
        request_type_name='DnsManagedZoneOperationsListRequest',
        response_type_name='ManagedZoneOperationsListResponse',
        supports_download=False,
    )

  class ManagedZonesService(base_api.BaseApiService):
    """Service class for the managedZones resource."""

    _NAME = 'managedZones'

    def __init__(self, client):
      super(DnsV1.ManagedZonesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create method for the managedZones service.

      Args:
        request: (DnsManagedZonesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ManagedZone) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='dns.managedZones.create',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['clientOperationId'],
        relative_path='projects/{project}/managedZones',
        request_field='managedZone',
        request_type_name='DnsManagedZonesCreateRequest',
        response_type_name='ManagedZone',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete method for the managedZones service.

      Args:
        request: (DnsManagedZonesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DnsManagedZonesDeleteResponse) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method='DELETE',
        method_id='dns.managedZones.delete',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['clientOperationId'],
        relative_path='projects/{project}/managedZones/{managedZone}',
        request_field='',
        request_type_name='DnsManagedZonesDeleteRequest',
        response_type_name='DnsManagedZonesDeleteResponse',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get method for the managedZones service.

      Args:
        request: (DnsManagedZonesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ManagedZone) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.managedZones.get',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['clientOperationId'],
        relative_path='projects/{project}/managedZones/{managedZone}',
        request_field='',
        request_type_name='DnsManagedZonesGetRequest',
        response_type_name='ManagedZone',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List method for the managedZones service.

      Args:
        request: (DnsManagedZonesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ManagedZonesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.managedZones.list',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['dnsName', 'maxResults', 'pageToken'],
        relative_path='projects/{project}/managedZones',
        request_field='',
        request_type_name='DnsManagedZonesListRequest',
        response_type_name='ManagedZonesListResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Patch method for the managedZones service.

      Args:
        request: (DnsManagedZonesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PATCH',
        method_id='dns.managedZones.patch',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['clientOperationId'],
        relative_path='projects/{project}/managedZones/{managedZone}',
        request_field='managedZoneResource',
        request_type_name='DnsManagedZonesPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Update method for the managedZones service.

      Args:
        request: (DnsManagedZonesUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PUT',
        method_id='dns.managedZones.update',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['clientOperationId'],
        relative_path='projects/{project}/managedZones/{managedZone}',
        request_field='managedZoneResource',
        request_type_name='DnsManagedZonesUpdateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class PoliciesService(base_api.BaseApiService):
    """Service class for the policies resource."""

    _NAME = 'policies'

    def __init__(self, client):
      super(DnsV1.PoliciesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create method for the policies service.

      Args:
        request: (DnsPoliciesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='dns.policies.create',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['clientOperationId'],
        relative_path='projects/{project}/policies',
        request_field='policy',
        request_type_name='DnsPoliciesCreateRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete method for the policies service.

      Args:
        request: (DnsPoliciesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DnsPoliciesDeleteResponse) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method='DELETE',
        method_id='dns.policies.delete',
        ordered_params=['project', 'policy'],
        path_params=['policy', 'project'],
        query_params=['clientOperationId'],
        relative_path='projects/{project}/policies/{policy}',
        request_field='',
        request_type_name='DnsPoliciesDeleteRequest',
        response_type_name='DnsPoliciesDeleteResponse',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get method for the policies service.

      Args:
        request: (DnsPoliciesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.policies.get',
        ordered_params=['project', 'policy'],
        path_params=['policy', 'project'],
        query_params=['clientOperationId'],
        relative_path='projects/{project}/policies/{policy}',
        request_field='',
        request_type_name='DnsPoliciesGetRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List method for the policies service.

      Args:
        request: (DnsPoliciesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PoliciesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.policies.list',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['maxResults', 'pageToken'],
        relative_path='projects/{project}/policies',
        request_field='',
        request_type_name='DnsPoliciesListRequest',
        response_type_name='PoliciesListResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Patch method for the policies service.

      Args:
        request: (DnsPoliciesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PoliciesPatchResponse) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PATCH',
        method_id='dns.policies.patch',
        ordered_params=['project', 'policy'],
        path_params=['policy', 'project'],
        query_params=['clientOperationId'],
        relative_path='projects/{project}/policies/{policy}',
        request_field='policyResource',
        request_type_name='DnsPoliciesPatchRequest',
        response_type_name='PoliciesPatchResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Update method for the policies service.

      Args:
        request: (DnsPoliciesUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PoliciesUpdateResponse) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PUT',
        method_id='dns.policies.update',
        ordered_params=['project', 'policy'],
        path_params=['policy', 'project'],
        query_params=['clientOperationId'],
        relative_path='projects/{project}/policies/{policy}',
        request_field='policyResource',
        request_type_name='DnsPoliciesUpdateRequest',
        response_type_name='PoliciesUpdateResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(DnsV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Get method for the projects service.

      Args:
        request: (DnsProjectsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Project) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.projects.get',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['clientOperationId'],
        relative_path='projects/{project}',
        request_field='',
        request_type_name='DnsProjectsGetRequest',
        response_type_name='Project',
        supports_download=False,
    )

  class ResourceRecordSetsService(base_api.BaseApiService):
    """Service class for the resourceRecordSets resource."""

    _NAME = 'resourceRecordSets'

    def __init__(self, client):
      super(DnsV1.ResourceRecordSetsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""List method for the resourceRecordSets service.

      Args:
        request: (DnsResourceRecordSetsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ResourceRecordSetsListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='dns.resourceRecordSets.list',
        ordered_params=['project', 'managedZone'],
        path_params=['managedZone', 'project'],
        query_params=['maxResults', 'name', 'pageToken', 'type'],
        relative_path='projects/{project}/managedZones/{managedZone}/rrsets',
        request_field='',
        request_type_name='DnsResourceRecordSetsListRequest',
        response_type_name='ResourceRecordSetsListResponse',
        supports_download=False,
    )
