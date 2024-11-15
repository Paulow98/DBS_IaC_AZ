# Initialize clients (Pedro was here lmao)
subscription_id = "your-subscription-id"
credentials = DefaultAzureCredential()

resource_client = ResourceManagementClient(credentials, subscription_id)
network_client = NetworkManagementClient(credentials, subscription_id)
compute_client = ComputeManagementClient(credentials, subscription_id)
