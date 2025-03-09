from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.appcontainers import ContainerAppsAPIClient as ContainerAppsClient
from rich.console import Console
from config import AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP, AZURE_CONTAINER_APPS

console = Console()

class AzureResourceManager:
    def __init__(self):
        self.credential = DefaultAzureCredential()
        self.container_apps_client = ContainerAppsClient(
            credential=self.credential,
            subscription_id=AZURE_SUBSCRIPTION_ID
        )

    def start_container_apps(self):
        """Start all configured Azure Container Apps."""
        if not AZURE_CONTAINER_APPS:
            console.print("[yellow]No Azure Container Apps configured[/yellow]")
            return

        for app_name in AZURE_CONTAINER_APPS:
            try:
                console.print(f"[green]Starting Azure Container App: {app_name}[/green]")
                # Start the container app
                poller = self.container_apps_client.container_apps.begin_start(
                    resource_group_name=AZURE_RESOURCE_GROUP,
                    container_app_name=app_name
                )
                poller.result()  # Wait for the operation to complete
            except Exception as e:
                console.print(f"[red]Error starting Azure Container App {app_name}: {str(e)}[/red]")

    def stop_container_apps(self):
        """Stop all configured Azure Container Apps."""
        if not AZURE_CONTAINER_APPS:
            console.print("[yellow]No Azure Container Apps configured[/yellow]")
            return

        for app_name in AZURE_CONTAINER_APPS:
            try:
                console.print(f"[green]Stopping Azure Container App: {app_name}[/green]")
                # Stop the container app
                poller = self.container_apps_client.container_apps.begin_stop(
                    resource_group_name=AZURE_RESOURCE_GROUP,
                    container_app_name=app_name
                )
                poller.result()  # Wait for the operation to complete
            except Exception as e:
                console.print(f"[red]Error stopping Azure Container App {app_name}: {str(e)}[/red]")