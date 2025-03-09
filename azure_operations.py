from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from rich.console import Console
from config import AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP, AZURE_VMS

console = Console()

class AzureResourceManager:
    def __init__(self):
        self.credential = DefaultAzureCredential()
        self.compute_client = ComputeManagementClient(
            credential=self.credential,
            subscription_id=AZURE_SUBSCRIPTION_ID
        )

    def start_vms(self):
        """Start all configured Azure VMs."""
        if not AZURE_VMS:
            console.print("[yellow]No Azure VMs configured[/yellow]")
            return

        for vm_name in AZURE_VMS:
            try:
                console.print(f"[green]Starting Azure VM: {vm_name}[/green]")
                self.compute_client.virtual_machines.begin_start(
                    AZURE_RESOURCE_GROUP,
                    vm_name
                ).result()
            except Exception as e:
                console.print(f"[red]Error starting Azure VM {vm_name}: {str(e)}[/red]")

    def stop_vms(self):
        """Stop all configured Azure VMs."""
        if not AZURE_VMS:
            console.print("[yellow]No Azure VMs configured[/yellow]")
            return

        for vm_name in AZURE_VMS:
            try:
                console.print(f"[green]Stopping Azure VM: {vm_name}[/green]")
                self.compute_client.virtual_machines.begin_deallocate(
                    AZURE_RESOURCE_GROUP,
                    vm_name
                ).result()
            except Exception as e:
                console.print(f"[red]Error stopping Azure VM {vm_name}: {str(e)}[/red]") 