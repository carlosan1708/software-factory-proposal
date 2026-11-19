targetScope = 'resourceGroup'

@description('Name of the sandbox group in the non-production resource group.')
@minLength(1)
@maxLength(32)
param sandboxGroupName string = 'sf-poc-sandboxes'

@description('Azure region that supports Container Apps Sandboxes.')
param location string = resourceGroup().location

var sandboxGroupDataOwnerRoleId = subscriptionResourceId(
  'Microsoft.Authorization/roleDefinitions',
  'c24cf47c-5077-412d-a19c-45202126392c'
)

resource sandboxGroup 'Microsoft.App/sandboxGroups@2026-07-01' = {
  name: sandboxGroupName
  location: location
}

resource controllerIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: '${sandboxGroupName}-controller'
  location: location
}

// Assign this identity to the trusted controller. The controller sets egress
// policy when it creates each short-lived generation or verification sandbox.
resource sandboxGroupDataOwner 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(sandboxGroup.id, controllerIdentity.id, sandboxGroupDataOwnerRoleId)
  scope: sandboxGroup
  properties: {
    principalId: controllerIdentity.properties.principalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: sandboxGroupDataOwnerRoleId
  }
}

output sandboxGroupId string = sandboxGroup.id
output controllerIdentityId string = controllerIdentity.id
output controllerClientId string = controllerIdentity.properties.clientId
