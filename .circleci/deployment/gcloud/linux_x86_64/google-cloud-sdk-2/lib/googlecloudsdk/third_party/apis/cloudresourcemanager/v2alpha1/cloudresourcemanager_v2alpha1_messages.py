"""Generated message classes for cloudresourcemanager version v2alpha1.

Creates, reads, and updates metadata for Google Cloud Platform resource
containers.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'cloudresourcemanager'


class AuditConfig(_messages.Message):
  r"""Specifies the audit configuration for a service. The configuration
  determines which permission types are logged, and what identities, if any,
  are exempted from logging. An AuditConfig must have one or more
  AuditLogConfigs. If there are AuditConfigs for both `allServices` and a
  specific service, the union of the two AuditConfigs is used for that
  service: the log_types specified in each AuditConfig are enabled, and the
  exempted_members in each AuditLogConfig are exempted. Example Policy with
  multiple AuditConfigs: { "audit_configs": [ { "service": "allServices",
  "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [
  "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" }, { "log_type":
  "ADMIN_READ" } ] }, { "service": "sampleservice.googleapis.com",
  "audit_log_configs": [ { "log_type": "DATA_READ" }, { "log_type":
  "DATA_WRITE", "exempted_members": [ "user:aliya@example.com" ] } ] } ] } For
  sampleservice, this policy enables DATA_READ, DATA_WRITE and ADMIN_READ
  logging. It also exempts jose@example.com from DATA_READ logging, and
  aliya@example.com from DATA_WRITE logging.

  Fields:
    auditLogConfigs: The configuration for logging of each type of permission.
    service: Specifies a service that will be enabled for audit logging. For
      example, `storage.googleapis.com`, `cloudsql.googleapis.com`.
      `allServices` is a special value that covers all services.
  """

  auditLogConfigs = _messages.MessageField('AuditLogConfig', 1, repeated=True)
  service = _messages.StringField(2)


class AuditLogConfig(_messages.Message):
  r"""Provides the configuration for logging a type of permissions. Example: {
  "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [
  "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" } ] } This enables
  'DATA_READ' and 'DATA_WRITE' logging, while exempting jose@example.com from
  DATA_READ logging.

  Enums:
    LogTypeValueValuesEnum: The log type that this config enables.

  Fields:
    exemptedMembers: Specifies the identities that do not cause logging for
      this type of permission. Follows the same format of Binding.members.
    logType: The log type that this config enables.
  """

  class LogTypeValueValuesEnum(_messages.Enum):
    r"""The log type that this config enables.

    Values:
      LOG_TYPE_UNSPECIFIED: Default case. Should never be this.
      ADMIN_READ: Admin reads. Example: CloudIAM getIamPolicy
      DATA_WRITE: Data writes. Example: CloudSQL Users create
      DATA_READ: Data reads. Example: CloudSQL Users list
    """
    LOG_TYPE_UNSPECIFIED = 0
    ADMIN_READ = 1
    DATA_WRITE = 2
    DATA_READ = 3

  exemptedMembers = _messages.StringField(1, repeated=True)
  logType = _messages.EnumField('LogTypeValueValuesEnum', 2)


class Binding(_messages.Message):
  r"""Associates `members` with a `role`.

  Fields:
    bindingId: A string attribute.
    condition: The condition that is associated with this binding. If the
      condition evaluates to `true`, then this binding applies to the current
      request. If the condition evaluates to `false`, then this binding does
      not apply to the current request. However, a different role binding
      might grant the same role to one or more of the members in this binding.
      To learn which resources support conditions in their IAM policies, see
      the [IAM
      documentation](https://cloud.google.com/iam/help/conditions/resource-
      policies).
    members: Specifies the identities requesting access for a Cloud Platform
      resource. `members` can have the following values: * `allUsers`: A
      special identifier that represents anyone who is on the internet; with
      or without a Google account. * `allAuthenticatedUsers`: A special
      identifier that represents anyone who is authenticated with a Google
      account or a service account. * `user:{emailid}`: An email address that
      represents a specific Google account. For example, `alice@example.com` .
      * `serviceAccount:{emailid}`: An email address that represents a service
      account. For example, `my-other-app@appspot.gserviceaccount.com`. *
      `group:{emailid}`: An email address that represents a Google group. For
      example, `admins@example.com`. *
      `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique
      identifier) representing a user that has been recently deleted. For
      example, `alice@example.com?uid=123456789012345678901`. If the user is
      recovered, this value reverts to `user:{emailid}` and the recovered user
      retains the role in the binding. *
      `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address
      (plus unique identifier) representing a service account that has been
      recently deleted. For example, `my-other-
      app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the
      service account is undeleted, this value reverts to
      `serviceAccount:{emailid}` and the undeleted service account retains the
      role in the binding. * `deleted:group:{emailid}?uid={uniqueid}`: An
      email address (plus unique identifier) representing a Google group that
      has been recently deleted. For example,
      `admins@example.com?uid=123456789012345678901`. If the group is
      recovered, this value reverts to `group:{emailid}` and the recovered
      group retains the role in the binding. * `domain:{domain}`: The G Suite
      domain (primary) that represents all the users of that domain. For
      example, `google.com` or `example.com`.
    role: Role that is assigned to `members`. For example, `roles/viewer`,
      `roles/editor`, or `roles/owner`.
  """

  bindingId = _messages.StringField(1)
  condition = _messages.MessageField('Expr', 2)
  members = _messages.StringField(3, repeated=True)
  role = _messages.StringField(4)


class CloudresourcemanagerFoldersCreateRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersCreateRequest object.

  Fields:
    folder: A Folder resource to be passed as the request body.
    parent: The resource name of the new Folder's parent. Must be of the form
      `folders/{folder_id}` or `organizations/{org_id}`.
  """

  folder = _messages.MessageField('Folder', 1)
  parent = _messages.StringField(2)


class CloudresourcemanagerFoldersDeleteRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersDeleteRequest object.

  Fields:
    foldersId: Part of `name`. the resource name of the Folder to be deleted.
      Must be of the form `folders/{folder_id}`.
  """

  foldersId = _messages.StringField(1, required=True)


class CloudresourcemanagerFoldersGetIamPolicyRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersGetIamPolicyRequest object.

  Fields:
    foldersId: Part of `resource`. REQUIRED: The resource for which the policy
      is being requested. See the operation documentation for the appropriate
      value for this field.
    getIamPolicyRequest: A GetIamPolicyRequest resource to be passed as the
      request body.
  """

  foldersId = _messages.StringField(1, required=True)
  getIamPolicyRequest = _messages.MessageField('GetIamPolicyRequest', 2)


class CloudresourcemanagerFoldersGetRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersGetRequest object.

  Fields:
    foldersId: Part of `name`. The resource name of the Folder to retrieve.
      Must be of the form `folders/{folder_id}`.
  """

  foldersId = _messages.StringField(1, required=True)


class CloudresourcemanagerFoldersListRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersListRequest object.

  Fields:
    pageSize: The maximum number of Folders to return in the response. This
      field is optional.
    pageToken: A pagination token returned from a previous call to
      `ListFolders` that indicates where this listing should continue from.
      This field is optional.
    parent: The resource name of the Organization or Folder whose Folders are
      being listed. Must be of the form `folders/{folder_id}` or
      `organizations/{org_id}`. Access to this method is controlled by
      checking the `resourcemanager.folders.list` permission on the `parent`.
    showDeleted: Controls whether Folders in the [DELETE_REQUESTED} state
      should be returned.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3)
  showDeleted = _messages.BooleanField(4)


class CloudresourcemanagerFoldersMoveRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersMoveRequest object.

  Fields:
    foldersId: Part of `name`. The resource name of the Folder to move. Must
      be of the form folders/{folder_id}
    moveFolderRequest: A MoveFolderRequest resource to be passed as the
      request body.
  """

  foldersId = _messages.StringField(1, required=True)
  moveFolderRequest = _messages.MessageField('MoveFolderRequest', 2)


class CloudresourcemanagerFoldersSetIamPolicyRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersSetIamPolicyRequest object.

  Fields:
    foldersId: Part of `resource`. REQUIRED: The resource for which the policy
      is being specified. See the operation documentation for the appropriate
      value for this field.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  foldersId = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class CloudresourcemanagerFoldersTestIamPermissionsRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersTestIamPermissionsRequest object.

  Fields:
    foldersId: Part of `resource`. REQUIRED: The resource for which the policy
      detail is being requested. See the operation documentation for the
      appropriate value for this field.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  foldersId = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class CloudresourcemanagerFoldersUndeleteRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersUndeleteRequest object.

  Fields:
    foldersId: Part of `name`. The resource name of the Folder to undelete.
      Must be of the form `folders/{folder_id}`.
    undeleteFolderRequest: A UndeleteFolderRequest resource to be passed as
      the request body.
  """

  foldersId = _messages.StringField(1, required=True)
  undeleteFolderRequest = _messages.MessageField('UndeleteFolderRequest', 2)


class CloudresourcemanagerFoldersUpdateRequest(_messages.Message):
  r"""A CloudresourcemanagerFoldersUpdateRequest object.

  Fields:
    folder: A Folder resource to be passed as the request body.
    foldersId: Part of `folder.name`. Output only. The resource name of the
      Folder. Its format is `folders/{folder_id}`, for example:
      "folders/1234".
  """

  folder = _messages.MessageField('Folder', 1)
  foldersId = _messages.StringField(2, required=True)


class CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperation(_messages.Message):
  r"""Metadata describing a long running folder operation

  Enums:
    OperationTypeValueValuesEnum: The type of this operation.

  Fields:
    destinationParent: The resource name of the folder or organization we are
      either creating the folder under or moving the folder to.
    displayName: The display name of the folder.
    operationType: The type of this operation.
    sourceParent: The resource name of the folder's parent. Only applicable
      when the operation_type is MOVE.
  """

  class OperationTypeValueValuesEnum(_messages.Enum):
    r"""The type of this operation.

    Values:
      OPERATION_TYPE_UNSPECIFIED: Operation type not specified.
      CREATE: A create folder operation.
      MOVE: A move folder operation.
    """
    OPERATION_TYPE_UNSPECIFIED = 0
    CREATE = 1
    MOVE = 2

  destinationParent = _messages.StringField(1)
  displayName = _messages.StringField(2)
  operationType = _messages.EnumField('OperationTypeValueValuesEnum', 3)
  sourceParent = _messages.StringField(4)


class CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperation(_messages.Message):
  r"""Metadata describing a long running folder operation

  Enums:
    OperationTypeValueValuesEnum: The type of this operation.

  Fields:
    destinationParent: The resource name of the folder or organization we are
      either creating the folder under or moving the folder to.
    displayName: The display name of the folder.
    operationType: The type of this operation.
    sourceParent: The resource name of the folder's parent. Only applicable
      when the operation_type is MOVE.
  """

  class OperationTypeValueValuesEnum(_messages.Enum):
    r"""The type of this operation.

    Values:
      OPERATION_TYPE_UNSPECIFIED: Operation type not specified.
      CREATE: A create folder operation.
      MOVE: A move folder operation.
    """
    OPERATION_TYPE_UNSPECIFIED = 0
    CREATE = 1
    MOVE = 2

  destinationParent = _messages.StringField(1)
  displayName = _messages.StringField(2)
  operationType = _messages.EnumField('OperationTypeValueValuesEnum', 3)
  sourceParent = _messages.StringField(4)


class Expr(_messages.Message):
  r"""Represents a textual expression in the Common Expression Language (CEL)
  syntax. CEL is a C-like expression language. The syntax and semantics of CEL
  are documented at https://github.com/google/cel-spec. Example (Comparison):
  title: "Summary size limit" description: "Determines if a summary is less
  than 100 chars" expression: "document.summary.size() < 100" Example
  (Equality): title: "Requestor is owner" description: "Determines if
  requestor is the document owner" expression: "document.owner ==
  request.auth.claims.email" Example (Logic): title: "Public documents"
  description: "Determine whether the document should be publicly visible"
  expression: "document.type != 'private' && document.type != 'internal'"
  Example (Data Manipulation): title: "Notification string" description:
  "Create a notification string with a timestamp." expression: "'New message
  received at ' + string(document.create_time)" The exact variables and
  functions that may be referenced within an expression are determined by the
  service that evaluates it. See the service documentation for additional
  information.

  Fields:
    description: Optional. Description of the expression. This is a longer
      text which describes the expression, e.g. when hovered over it in a UI.
    expression: Textual representation of an expression in Common Expression
      Language syntax.
    location: Optional. String indicating the location of the expression for
      error reporting, e.g. a file name and a position in the file.
    title: Optional. Title for the expression, i.e. a short string describing
      its purpose. This can be used e.g. in UIs which allow to enter the
      expression.
  """

  description = _messages.StringField(1)
  expression = _messages.StringField(2)
  location = _messages.StringField(3)
  title = _messages.StringField(4)


class Folder(_messages.Message):
  r"""A Folder in an Organization's resource hierarchy, used to organize that
  Organization's resources.

  Enums:
    LifecycleStateValueValuesEnum: The lifecycle state of the folder. Updates
      to the lifecycle_state must be performed via [DeleteFolder] and
      [UndeleteFolder].

  Fields:
    createTime: Output only. Timestamp when the Folder was created. Assigned
      by the server.
    displayName: The folder's display name. A folder's display name must be
      unique amongst its siblings, e.g. no two folders with the same parent
      can share the same display name. The display name must start and end
      with a letter or digit, may contain letters, digits, spaces, hyphens and
      underscores and can be no longer than 30 characters. This is captured by
      the regular expression: `[\p{L}\p{N}]({\p{L}\p{N}_-
      ]{0,28}[\p{L}\p{N}])?`.
    lifecycleState: The lifecycle state of the folder. Updates to the
      lifecycle_state must be performed via [DeleteFolder] and
      [UndeleteFolder].
    name: Output only. The resource name of the Folder. Its format is
      `folders/{folder_id}`, for example: "folders/1234".
    parent: Output only. The Folder's parent's resource name. Updates to the
      folder's parent must be performed via [MoveFolders].
  """

  class LifecycleStateValueValuesEnum(_messages.Enum):
    r"""The lifecycle state of the folder. Updates to the lifecycle_state must
    be performed via [DeleteFolder] and [UndeleteFolder].

    Values:
      LIFECYCLE_STATE_UNSPECIFIED: Unspecified state.
      ACTIVE: The normal and active state.
      DELETE_REQUESTED: The folder has been marked for deletion by the user.
    """
    LIFECYCLE_STATE_UNSPECIFIED = 0
    ACTIVE = 1
    DELETE_REQUESTED = 2

  createTime = _messages.StringField(1)
  displayName = _messages.StringField(2)
  lifecycleState = _messages.EnumField('LifecycleStateValueValuesEnum', 3)
  name = _messages.StringField(4)
  parent = _messages.StringField(5)


class FolderOperation(_messages.Message):
  r"""Metadata describing a long running folder operation

  Enums:
    OperationTypeValueValuesEnum: The type of this operation.

  Fields:
    destinationParent: The resource name of the folder or organization we are
      either creating the folder under or moving the folder to.
    displayName: The display name of the folder.
    operationType: The type of this operation.
    sourceParent: The resource name of the folder's parent. Only applicable
      when the operation_type is MOVE.
  """

  class OperationTypeValueValuesEnum(_messages.Enum):
    r"""The type of this operation.

    Values:
      OPERATION_TYPE_UNSPECIFIED: Operation type not specified.
      CREATE: A create folder operation.
      MOVE: A move folder operation.
    """
    OPERATION_TYPE_UNSPECIFIED = 0
    CREATE = 1
    MOVE = 2

  destinationParent = _messages.StringField(1)
  displayName = _messages.StringField(2)
  operationType = _messages.EnumField('OperationTypeValueValuesEnum', 3)
  sourceParent = _messages.StringField(4)


class FolderOperationError(_messages.Message):
  r"""A classification of the Folder Operation error.

  Enums:
    ErrorMessageIdValueValuesEnum: The type of operation error experienced.

  Fields:
    errorMessageId: The type of operation error experienced.
  """

  class ErrorMessageIdValueValuesEnum(_messages.Enum):
    r"""The type of operation error experienced.

    Values:
      ERROR_TYPE_UNSPECIFIED: The error type was unrecognized or unspecified.
      ACTIVE_FOLDER_HEIGHT_VIOLATION: The attempted action would violate the
        max folder depth constraint.
      MAX_CHILD_FOLDERS_VIOLATION: The attempted action would violate the max
        child folders constraint.
      FOLDER_NAME_UNIQUENESS_VIOLATION: The attempted action would violate the
        locally-unique folder display_name constraint.
      RESOURCE_DELETED_VIOLATION: The resource being moved has been deleted.
      PARENT_DELETED_VIOLATION: The resource a folder was being added to has
        been deleted.
      CYCLE_INTRODUCED_VIOLATION: The attempted action would introduce cycle
        in resource path.
      FOLDER_BEING_MOVED_VIOLATION: The attempted action would move a folder
        that is already being moved.
      FOLDER_TO_DELETE_NON_EMPTY_VIOLATION: The folder the caller is trying to
        delete contains active resources.
      DELETED_FOLDER_HEIGHT_VIOLATION: The attempted action would violate the
        max deleted folder depth constraint.
    """
    ERROR_TYPE_UNSPECIFIED = 0
    ACTIVE_FOLDER_HEIGHT_VIOLATION = 1
    MAX_CHILD_FOLDERS_VIOLATION = 2
    FOLDER_NAME_UNIQUENESS_VIOLATION = 3
    RESOURCE_DELETED_VIOLATION = 4
    PARENT_DELETED_VIOLATION = 5
    CYCLE_INTRODUCED_VIOLATION = 6
    FOLDER_BEING_MOVED_VIOLATION = 7
    FOLDER_TO_DELETE_NON_EMPTY_VIOLATION = 8
    DELETED_FOLDER_HEIGHT_VIOLATION = 9

  errorMessageId = _messages.EnumField('ErrorMessageIdValueValuesEnum', 1)


class GetIamPolicyRequest(_messages.Message):
  r"""Request message for `GetIamPolicy` method.

  Fields:
    options: OPTIONAL: A `GetPolicyOptions` object for specifying options to
      `GetIamPolicy`.
  """

  options = _messages.MessageField('GetPolicyOptions', 1)


class GetPolicyOptions(_messages.Message):
  r"""Encapsulates settings provided to GetIamPolicy.

  Fields:
    requestedPolicyVersion: Optional. The policy format version to be
      returned. Valid values are 0, 1, and 3. Requests specifying an invalid
      value will be rejected. Requests for policies with any conditional
      bindings must specify version 3. Policies without any conditional
      bindings may specify any valid value or leave the field unset. To learn
      which resources support conditions in their IAM policies, see the [IAM
      documentation](https://cloud.google.com/iam/help/conditions/resource-
      policies).
  """

  requestedPolicyVersion = _messages.IntegerField(1, variant=_messages.Variant.INT32)


class ListFoldersResponse(_messages.Message):
  r"""The ListFolders response message.

  Fields:
    folders: A possibly paginated list of Folders that are direct descendants
      of the specified parent resource.
    nextPageToken: A pagination token returned from a previous call to
      `ListFolders` that indicates from where listing should continue. This
      field is optional.
  """

  folders = _messages.MessageField('Folder', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class MoveFolderRequest(_messages.Message):
  r"""The MoveFolder request message.

  Fields:
    destinationParent: The resource name of the Folder or Organization to
      reparent the folder under. Must be of the form `folders/{folder_id}` or
      `organizations/{org_id}`.
  """

  destinationParent = _messages.StringField(1)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success. If
      the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
    response: The normal response of the operation in case of success. If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation. It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata. Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success. If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`. If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource. For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name. For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class Policy(_messages.Message):
  r"""An Identity and Access Management (IAM) policy, which specifies access
  controls for Google Cloud resources. A `Policy` is a collection of
  `bindings`. A `binding` binds one or more `members` to a single `role`.
  Members can be user accounts, service accounts, Google groups, and domains
  (such as G Suite). A `role` is a named list of permissions; each `role` can
  be an IAM predefined role or a user-created custom role. For some types of
  Google Cloud resources, a `binding` can also specify a `condition`, which is
  a logical expression that allows access to a resource only if the expression
  evaluates to `true`. A condition can add constraints based on attributes of
  the request, the resource, or both. To learn which resources support
  conditions in their IAM policies, see the [IAM
  documentation](https://cloud.google.com/iam/help/conditions/resource-
  policies). **JSON example:** { "bindings": [ { "role":
  "roles/resourcemanager.organizationAdmin", "members": [
  "user:mike@example.com", "group:admins@example.com", "domain:google.com",
  "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role":
  "roles/resourcemanager.organizationViewer", "members": [
  "user:eve@example.com" ], "condition": { "title": "expirable access",
  "description": "Does not grant access after Sep 2020", "expression":
  "request.time < timestamp('2020-10-01T00:00:00.000Z')", } } ], "etag":
  "BwWWja0YfJA=", "version": 3 } **YAML example:** bindings: - members: -
  user:mike@example.com - group:admins@example.com - domain:google.com -
  serviceAccount:my-project-id@appspot.gserviceaccount.com role:
  roles/resourcemanager.organizationAdmin - members: - user:eve@example.com
  role: roles/resourcemanager.organizationViewer condition: title: expirable
  access description: Does not grant access after Sep 2020 expression:
  request.time < timestamp('2020-10-01T00:00:00.000Z') - etag: BwWWja0YfJA= -
  version: 3 For a description of IAM and its features, see the [IAM
  documentation](https://cloud.google.com/iam/docs/).

  Fields:
    auditConfigs: Specifies cloud audit logging configuration for this policy.
    bindings: Associates a list of `members` to a `role`. Optionally, may
      specify a `condition` that determines how and when the `bindings` are
      applied. Each of the `bindings` must contain at least one member.
    etag: `etag` is used for optimistic concurrency control as a way to help
      prevent simultaneous updates of a policy from overwriting each other. It
      is strongly suggested that systems make use of the `etag` in the read-
      modify-write cycle to perform policy updates in order to avoid race
      conditions: An `etag` is returned in the response to `getIamPolicy`, and
      systems are expected to put that etag in the request to `setIamPolicy`
      to ensure that their change will be applied to the same version of the
      policy. **Important:** If you use IAM Conditions, you must include the
      `etag` field whenever you call `setIamPolicy`. If you omit this field,
      then IAM allows you to overwrite a version `3` policy with a version `1`
      policy, and all of the conditions in the version `3` policy are lost.
    version: Specifies the format of the policy. Valid values are `0`, `1`,
      and `3`. Requests that specify an invalid value are rejected. Any
      operation that affects conditional role bindings must specify version
      `3`. This requirement applies to the following operations: * Getting a
      policy that includes a conditional role binding * Adding a conditional
      role binding to a policy * Changing a conditional role binding in a
      policy * Removing any role binding, with or without a condition, from a
      policy that includes conditions **Important:** If you use IAM
      Conditions, you must include the `etag` field whenever you call
      `setIamPolicy`. If you omit this field, then IAM allows you to overwrite
      a version `3` policy with a version `1` policy, and all of the
      conditions in the version `3` policy are lost. If a policy does not
      include any conditions, operations on that policy may specify any valid
      version or leave the field unset. To learn which resources support
      conditions in their IAM policies, see the [IAM
      documentation](https://cloud.google.com/iam/help/conditions/resource-
      policies).
  """

  auditConfigs = _messages.MessageField('AuditConfig', 1, repeated=True)
  bindings = _messages.MessageField('Binding', 2, repeated=True)
  etag = _messages.BytesField(3)
  version = _messages.IntegerField(4, variant=_messages.Variant.INT32)


class ProjectCreationStatus(_messages.Message):
  r"""A status object which is used as the `metadata` field for the Operation
  returned by CreateProject. It provides insight for when significant phases
  of Project creation have completed.

  Fields:
    createTime: Creation time of the project creation workflow.
    gettable: True if the project can be retrieved using GetProject. No other
      operations on the project are guaranteed to work until the project
      creation is complete.
    ready: True if the project creation process is complete.
  """

  createTime = _messages.StringField(1)
  gettable = _messages.BooleanField(2)
  ready = _messages.BooleanField(3)


class SetIamPolicyRequest(_messages.Message):
  r"""Request message for `SetIamPolicy` method.

  Fields:
    policy: REQUIRED: The complete policy to be applied to the `resource`. The
      size of the policy is limited to a few 10s of KB. An empty policy is a
      valid policy but certain Cloud Platform services (such as Projects)
      might reject them.
    updateMask: OPTIONAL: A FieldMask specifying which fields of the policy to
      modify. Only the fields in the mask will be modified. If no mask is
      provided, the following default mask is used: `paths: "bindings, etag"`
  """

  policy = _messages.MessageField('Policy', 1)
  updateMask = _messages.StringField(2)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details. You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details. There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class TestIamPermissionsRequest(_messages.Message):
  r"""Request message for `TestIamPermissions` method.

  Fields:
    permissions: The set of permissions to check for the `resource`.
      Permissions with wildcards (such as '*' or 'storage.*') are not allowed.
      For more information see [IAM
      Overview](https://cloud.google.com/iam/docs/overview#permissions).
  """

  permissions = _messages.StringField(1, repeated=True)


class TestIamPermissionsResponse(_messages.Message):
  r"""Response message for `TestIamPermissions` method.

  Fields:
    permissions: A subset of `TestPermissionsRequest.permissions` that the
      caller is allowed.
  """

  permissions = _messages.StringField(1, repeated=True)


class UndeleteFolderRequest(_messages.Message):
  r"""The UndeleteFolder request message."""


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
