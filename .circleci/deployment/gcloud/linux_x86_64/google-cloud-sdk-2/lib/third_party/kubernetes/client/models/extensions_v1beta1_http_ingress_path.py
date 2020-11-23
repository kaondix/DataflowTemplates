# coding: utf-8
"""
    Kubernetes

    No description provided (generated by Swagger Codegen
    https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.14.4

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class ExtensionsV1beta1HTTPIngressPath(object):
  """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
  """
    Attributes:
      swagger_types (dict): The key is attribute name and the value is attribute
        type.
      attribute_map (dict): The key is attribute name and the value is json key
        in definition.
  """
  swagger_types = {'backend': 'ExtensionsV1beta1IngressBackend', 'path': 'str'}

  attribute_map = {'backend': 'backend', 'path': 'path'}

  def __init__(self, backend=None, path=None):
    """
        ExtensionsV1beta1HTTPIngressPath - a model defined in Swagger
        """

    self._backend = None
    self._path = None
    self.discriminator = None

    self.backend = backend
    if path is not None:
      self.path = path

  @property
  def backend(self):
    """
        Gets the backend of this ExtensionsV1beta1HTTPIngressPath.
        Backend defines the referenced service endpoint to which the traffic
        will be forwarded to.

        :return: The backend of this ExtensionsV1beta1HTTPIngressPath.
        :rtype: ExtensionsV1beta1IngressBackend
        """
    return self._backend

  @backend.setter
  def backend(self, backend):
    """
        Sets the backend of this ExtensionsV1beta1HTTPIngressPath.
        Backend defines the referenced service endpoint to which the traffic
        will be forwarded to.

        :param backend: The backend of this ExtensionsV1beta1HTTPIngressPath.
        :type: ExtensionsV1beta1IngressBackend
        """
    if backend is None:
      raise ValueError('Invalid value for `backend`, must not be `None`')

    self._backend = backend

  @property
  def path(self):
    """
        Gets the path of this ExtensionsV1beta1HTTPIngressPath.
        Path is an extended POSIX regex as defined by IEEE Std 1003.1, (i.e this
        follows the egrep/unix syntax, not the perl syntax) matched against the
        path of an incoming request. Currently it can contain characters
        disallowed from the conventional \"path\" part of a URL as defined by
        RFC 3986. Paths must begin with a '/'. If unspecified, the path defaults
        to a catch all sending traffic to the backend.

        :return: The path of this ExtensionsV1beta1HTTPIngressPath.
        :rtype: str
        """
    return self._path

  @path.setter
  def path(self, path):
    """
        Sets the path of this ExtensionsV1beta1HTTPIngressPath.
        Path is an extended POSIX regex as defined by IEEE Std 1003.1, (i.e this
        follows the egrep/unix syntax, not the perl syntax) matched against the
        path of an incoming request. Currently it can contain characters
        disallowed from the conventional \"path\" part of a URL as defined by
        RFC 3986. Paths must begin with a '/'. If unspecified, the path defaults
        to a catch all sending traffic to the backend.

        :param path: The path of this ExtensionsV1beta1HTTPIngressPath.
        :type: str
        """

    self._path = path

  def to_dict(self):
    """
        Returns the model properties as a dict
        """
    result = {}

    for attr, _ in iteritems(self.swagger_types):
      value = getattr(self, attr)
      if isinstance(value, list):
        result[attr] = list(
            map(lambda x: x.to_dict() if hasattr(x, 'to_dict') else x, value))
      elif hasattr(value, 'to_dict'):
        result[attr] = value.to_dict()
      elif isinstance(value, dict):
        result[attr] = dict(
            map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], 'to_dict') else item, value.items()))
      else:
        result[attr] = value

    return result

  def to_str(self):
    """
        Returns the string representation of the model
        """
    return pformat(self.to_dict())

  def __repr__(self):
    """
        For `print` and `pprint`
        """
    return self.to_str()

  def __eq__(self, other):
    """
        Returns true if both objects are equal
        """
    if not isinstance(other, ExtensionsV1beta1HTTPIngressPath):
      return False

    return self.__dict__ == other.__dict__

  def __ne__(self, other):
    """
        Returns true if both objects are not equal
        """
    return not self == other
