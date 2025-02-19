# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models_py3 import (  # type: ignore
    AccessPolicy,
    AccountImmutabilityPolicyProperties,
    AccountSasParameters,
    ActiveDirectoryProperties,
    AzureEntityResource,
    AzureFilesIdentityBasedAuthentication,
    BlobContainer,
    BlobInventoryCreationTime,
    BlobInventoryPolicy,
    BlobInventoryPolicyDefinition,
    BlobInventoryPolicyFilter,
    BlobInventoryPolicyRule,
    BlobInventoryPolicySchema,
    BlobRestoreParameters,
    BlobRestoreRange,
    BlobRestoreStatus,
    BlobServiceItems,
    BlobServiceProperties,
    ChangeFeed,
    CheckNameAvailabilityResult,
    CloudErrorBody,
    CorsRule,
    CorsRules,
    CustomDomain,
    DateAfterCreation,
    DateAfterModification,
    DeleteRetentionPolicy,
    DeletedAccount,
    DeletedAccountListResult,
    DeletedShare,
    Dimension,
    Encryption,
    EncryptionIdentity,
    EncryptionScope,
    EncryptionScopeKeyVaultProperties,
    EncryptionScopeListResult,
    EncryptionService,
    EncryptionServices,
    Endpoints,
    ErrorAdditionalInfo,
    ErrorDetail,
    ErrorResponse,
    ErrorResponseAutoGenerated,
    ErrorResponseBody,
    ExecutionTarget,
    ExecutionTrigger,
    ExecutionTriggerUpdate,
    ExtendedLocation,
    FileServiceItems,
    FileServiceProperties,
    FileShare,
    FileShareItem,
    FileShareItems,
    GeoReplicationStats,
    IPRule,
    Identity,
    ImmutabilityPolicy,
    ImmutabilityPolicyProperties,
    ImmutableStorageAccount,
    ImmutableStorageWithVersioning,
    KeyCreationTime,
    KeyPolicy,
    KeyVaultProperties,
    LastAccessTimeTrackingPolicy,
    LeaseContainerRequest,
    LeaseContainerResponse,
    LeaseShareRequest,
    LeaseShareResponse,
    LegalHold,
    LegalHoldProperties,
    ListAccountSasResponse,
    ListBlobInventoryPolicy,
    ListContainerItem,
    ListContainerItems,
    ListQueue,
    ListQueueResource,
    ListQueueServices,
    ListServiceSasResponse,
    ListTableResource,
    ListTableServices,
    LocalUser,
    LocalUserKeys,
    LocalUserRegeneratePasswordResult,
    LocalUsers,
    ManagementPolicy,
    ManagementPolicyAction,
    ManagementPolicyBaseBlob,
    ManagementPolicyDefinition,
    ManagementPolicyFilter,
    ManagementPolicyRule,
    ManagementPolicySchema,
    ManagementPolicySnapShot,
    ManagementPolicyVersion,
    MetricSpecification,
    Multichannel,
    NetworkRuleSet,
    NetworkSecurityPerimeter,
    NetworkSecurityPerimeterConfiguration,
    NetworkSecurityPerimeterConfigurationList,
    NetworkSecurityPerimeterConfigurationPropertiesProfile,
    NetworkSecurityPerimeterConfigurationPropertiesResourceAssociation,
    NspAccessRule,
    NspAccessRuleProperties,
    NspAccessRulePropertiesSubscriptionsItem,
    ObjectReplicationPolicies,
    ObjectReplicationPolicy,
    ObjectReplicationPolicyFilter,
    ObjectReplicationPolicyRule,
    Operation,
    OperationDisplay,
    OperationListResult,
    PermissionScope,
    PrivateEndpoint,
    PrivateEndpointConnection,
    PrivateEndpointConnectionListResult,
    PrivateLinkResource,
    PrivateLinkResourceListResult,
    PrivateLinkServiceConnectionState,
    ProtectedAppendWritesHistory,
    ProtocolSettings,
    ProvisioningIssue,
    ProvisioningIssueProperties,
    ProxyResource,
    ProxyResourceAutoGenerated,
    QueueServiceProperties,
    Resource,
    ResourceAccessRule,
    ResourceAutoGenerated,
    RestorePolicyProperties,
    Restriction,
    RoutingPreference,
    SKUCapability,
    SasPolicy,
    ServiceSasParameters,
    ServiceSpecification,
    SignedIdentifier,
    Sku,
    SkuInformation,
    SmbSetting,
    SshPublicKey,
    StorageAccount,
    StorageAccountCheckNameAvailabilityParameters,
    StorageAccountCreateParameters,
    StorageAccountInternetEndpoints,
    StorageAccountKey,
    StorageAccountListKeysResult,
    StorageAccountListResult,
    StorageAccountMicrosoftEndpoints,
    StorageAccountMigration,
    StorageAccountRegenerateKeyParameters,
    StorageAccountSkuConversionStatus,
    StorageAccountUpdateParameters,
    StorageQueue,
    StorageSkuListResult,
    StorageTaskAssignment,
    StorageTaskAssignmentExecutionContext,
    StorageTaskAssignmentProperties,
    StorageTaskAssignmentReport,
    StorageTaskAssignmentUpdateExecutionContext,
    StorageTaskAssignmentUpdateParameters,
    StorageTaskAssignmentUpdateProperties,
    StorageTaskAssignmentUpdateReport,
    StorageTaskAssignmentsList,
    StorageTaskReportInstance,
    StorageTaskReportProperties,
    StorageTaskReportSummary,
    SystemData,
    Table,
    TableAccessPolicy,
    TableServiceProperties,
    TableSignedIdentifier,
    TagFilter,
    TagProperty,
    TrackedResource,
    TriggerParameters,
    TriggerParametersUpdate,
    UpdateHistoryProperty,
    Usage,
    UsageListResult,
    UsageName,
    UserAssignedIdentity,
    VirtualNetworkRule,
)

from ._storage_management_client_enums import (  # type: ignore
    AccessTier,
    AccountImmutabilityPolicyState,
    AccountStatus,
    AccountType,
    AllowedCopyScope,
    AllowedMethods,
    BlobInventoryPolicyName,
    BlobRestoreProgressStatus,
    Bypass,
    CreatedByType,
    DefaultAction,
    DefaultSharePermission,
    DirectoryServiceOptions,
    DnsEndpointType,
    EnabledProtocols,
    EncryptionScopeSource,
    EncryptionScopeState,
    ExpirationAction,
    ExtendedLocationTypes,
    Format,
    GeoReplicationStatus,
    HttpProtocol,
    IdentityType,
    ImmutabilityPolicyState,
    ImmutabilityPolicyUpdateType,
    InventoryRuleType,
    IssueType,
    KeyPermission,
    KeySource,
    KeyType,
    Kind,
    LargeFileSharesState,
    LeaseContainerRequestEnum,
    LeaseDuration,
    LeaseShareAction,
    LeaseState,
    LeaseStatus,
    ListContainersInclude,
    ListEncryptionScopesInclude,
    ListLocalUserIncludeParam,
    ManagementPolicyName,
    MigrationName,
    MigrationState,
    MigrationStatus,
    MinimumTlsVersion,
    Name,
    NetworkSecurityPerimeterConfigurationProvisioningState,
    NspAccessRuleDirection,
    ObjectType,
    Permissions,
    PostFailoverRedundancy,
    PostPlannedFailoverRedundancy,
    PrivateEndpointConnectionProvisioningState,
    PrivateEndpointServiceConnectionStatus,
    ProvisioningState,
    PublicAccess,
    PublicNetworkAccess,
    Reason,
    ReasonCode,
    ResourceAssociationAccessMode,
    RootSquashType,
    RoutingChoice,
    RuleType,
    RunResult,
    RunStatusEnum,
    Schedule,
    Services,
    Severity,
    ShareAccessTier,
    SignedResource,
    SignedResourceTypes,
    SkuConversionStatus,
    SkuName,
    SkuTier,
    State,
    StorageAccountExpand,
    TriggerType,
    UsageUnit,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AccessPolicy",
    "AccountImmutabilityPolicyProperties",
    "AccountSasParameters",
    "ActiveDirectoryProperties",
    "AzureEntityResource",
    "AzureFilesIdentityBasedAuthentication",
    "BlobContainer",
    "BlobInventoryCreationTime",
    "BlobInventoryPolicy",
    "BlobInventoryPolicyDefinition",
    "BlobInventoryPolicyFilter",
    "BlobInventoryPolicyRule",
    "BlobInventoryPolicySchema",
    "BlobRestoreParameters",
    "BlobRestoreRange",
    "BlobRestoreStatus",
    "BlobServiceItems",
    "BlobServiceProperties",
    "ChangeFeed",
    "CheckNameAvailabilityResult",
    "CloudErrorBody",
    "CorsRule",
    "CorsRules",
    "CustomDomain",
    "DateAfterCreation",
    "DateAfterModification",
    "DeleteRetentionPolicy",
    "DeletedAccount",
    "DeletedAccountListResult",
    "DeletedShare",
    "Dimension",
    "Encryption",
    "EncryptionIdentity",
    "EncryptionScope",
    "EncryptionScopeKeyVaultProperties",
    "EncryptionScopeListResult",
    "EncryptionService",
    "EncryptionServices",
    "Endpoints",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "ErrorResponseAutoGenerated",
    "ErrorResponseBody",
    "ExecutionTarget",
    "ExecutionTrigger",
    "ExecutionTriggerUpdate",
    "ExtendedLocation",
    "FileServiceItems",
    "FileServiceProperties",
    "FileShare",
    "FileShareItem",
    "FileShareItems",
    "GeoReplicationStats",
    "IPRule",
    "Identity",
    "ImmutabilityPolicy",
    "ImmutabilityPolicyProperties",
    "ImmutableStorageAccount",
    "ImmutableStorageWithVersioning",
    "KeyCreationTime",
    "KeyPolicy",
    "KeyVaultProperties",
    "LastAccessTimeTrackingPolicy",
    "LeaseContainerRequest",
    "LeaseContainerResponse",
    "LeaseShareRequest",
    "LeaseShareResponse",
    "LegalHold",
    "LegalHoldProperties",
    "ListAccountSasResponse",
    "ListBlobInventoryPolicy",
    "ListContainerItem",
    "ListContainerItems",
    "ListQueue",
    "ListQueueResource",
    "ListQueueServices",
    "ListServiceSasResponse",
    "ListTableResource",
    "ListTableServices",
    "LocalUser",
    "LocalUserKeys",
    "LocalUserRegeneratePasswordResult",
    "LocalUsers",
    "ManagementPolicy",
    "ManagementPolicyAction",
    "ManagementPolicyBaseBlob",
    "ManagementPolicyDefinition",
    "ManagementPolicyFilter",
    "ManagementPolicyRule",
    "ManagementPolicySchema",
    "ManagementPolicySnapShot",
    "ManagementPolicyVersion",
    "MetricSpecification",
    "Multichannel",
    "NetworkRuleSet",
    "NetworkSecurityPerimeter",
    "NetworkSecurityPerimeterConfiguration",
    "NetworkSecurityPerimeterConfigurationList",
    "NetworkSecurityPerimeterConfigurationPropertiesProfile",
    "NetworkSecurityPerimeterConfigurationPropertiesResourceAssociation",
    "NspAccessRule",
    "NspAccessRuleProperties",
    "NspAccessRulePropertiesSubscriptionsItem",
    "ObjectReplicationPolicies",
    "ObjectReplicationPolicy",
    "ObjectReplicationPolicyFilter",
    "ObjectReplicationPolicyRule",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "PermissionScope",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkServiceConnectionState",
    "ProtectedAppendWritesHistory",
    "ProtocolSettings",
    "ProvisioningIssue",
    "ProvisioningIssueProperties",
    "ProxyResource",
    "ProxyResourceAutoGenerated",
    "QueueServiceProperties",
    "Resource",
    "ResourceAccessRule",
    "ResourceAutoGenerated",
    "RestorePolicyProperties",
    "Restriction",
    "RoutingPreference",
    "SKUCapability",
    "SasPolicy",
    "ServiceSasParameters",
    "ServiceSpecification",
    "SignedIdentifier",
    "Sku",
    "SkuInformation",
    "SmbSetting",
    "SshPublicKey",
    "StorageAccount",
    "StorageAccountCheckNameAvailabilityParameters",
    "StorageAccountCreateParameters",
    "StorageAccountInternetEndpoints",
    "StorageAccountKey",
    "StorageAccountListKeysResult",
    "StorageAccountListResult",
    "StorageAccountMicrosoftEndpoints",
    "StorageAccountMigration",
    "StorageAccountRegenerateKeyParameters",
    "StorageAccountSkuConversionStatus",
    "StorageAccountUpdateParameters",
    "StorageQueue",
    "StorageSkuListResult",
    "StorageTaskAssignment",
    "StorageTaskAssignmentExecutionContext",
    "StorageTaskAssignmentProperties",
    "StorageTaskAssignmentReport",
    "StorageTaskAssignmentUpdateExecutionContext",
    "StorageTaskAssignmentUpdateParameters",
    "StorageTaskAssignmentUpdateProperties",
    "StorageTaskAssignmentUpdateReport",
    "StorageTaskAssignmentsList",
    "StorageTaskReportInstance",
    "StorageTaskReportProperties",
    "StorageTaskReportSummary",
    "SystemData",
    "Table",
    "TableAccessPolicy",
    "TableServiceProperties",
    "TableSignedIdentifier",
    "TagFilter",
    "TagProperty",
    "TrackedResource",
    "TriggerParameters",
    "TriggerParametersUpdate",
    "UpdateHistoryProperty",
    "Usage",
    "UsageListResult",
    "UsageName",
    "UserAssignedIdentity",
    "VirtualNetworkRule",
    "AccessTier",
    "AccountImmutabilityPolicyState",
    "AccountStatus",
    "AccountType",
    "AllowedCopyScope",
    "AllowedMethods",
    "BlobInventoryPolicyName",
    "BlobRestoreProgressStatus",
    "Bypass",
    "CreatedByType",
    "DefaultAction",
    "DefaultSharePermission",
    "DirectoryServiceOptions",
    "DnsEndpointType",
    "EnabledProtocols",
    "EncryptionScopeSource",
    "EncryptionScopeState",
    "ExpirationAction",
    "ExtendedLocationTypes",
    "Format",
    "GeoReplicationStatus",
    "HttpProtocol",
    "IdentityType",
    "ImmutabilityPolicyState",
    "ImmutabilityPolicyUpdateType",
    "InventoryRuleType",
    "IssueType",
    "KeyPermission",
    "KeySource",
    "KeyType",
    "Kind",
    "LargeFileSharesState",
    "LeaseContainerRequestEnum",
    "LeaseDuration",
    "LeaseShareAction",
    "LeaseState",
    "LeaseStatus",
    "ListContainersInclude",
    "ListEncryptionScopesInclude",
    "ListLocalUserIncludeParam",
    "ManagementPolicyName",
    "MigrationName",
    "MigrationState",
    "MigrationStatus",
    "MinimumTlsVersion",
    "Name",
    "NetworkSecurityPerimeterConfigurationProvisioningState",
    "NspAccessRuleDirection",
    "ObjectType",
    "Permissions",
    "PostFailoverRedundancy",
    "PostPlannedFailoverRedundancy",
    "PrivateEndpointConnectionProvisioningState",
    "PrivateEndpointServiceConnectionStatus",
    "ProvisioningState",
    "PublicAccess",
    "PublicNetworkAccess",
    "Reason",
    "ReasonCode",
    "ResourceAssociationAccessMode",
    "RootSquashType",
    "RoutingChoice",
    "RuleType",
    "RunResult",
    "RunStatusEnum",
    "Schedule",
    "Services",
    "Severity",
    "ShareAccessTier",
    "SignedResource",
    "SignedResourceTypes",
    "SkuConversionStatus",
    "SkuName",
    "SkuTier",
    "State",
    "StorageAccountExpand",
    "TriggerType",
    "UsageUnit",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
