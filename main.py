from rich.console import Console
from rich.prompt import Prompt
from aws_operations import AWSResourceManager
from azure_operations import AzureResourceManager

console = Console()

def main():
    aws_manager = AWSResourceManager()
    azure_manager = AzureResourceManager()

    while True:
        console.print("\n[bold cyan]Cloud Resource Manager[/bold cyan]")
        console.print("\n1. Start all resources")
        console.print("2. Stop all resources")
        console.print("3. Manage AWS resources only")
        console.print("4. Manage Azure resources only")
        console.print("5. Exit")

        choice = Prompt.ask("\nEnter your choice", choices=["1", "2", "3", "4", "5"])

        if choice == "1":
            console.print("\n[bold green]Starting all resources...[/bold green]")
            aws_manager.start_ec2_instances()
            aws_manager.resume_apprunner_services()
            azure_manager.start_vms()

        elif choice == "2":
            console.print("\n[bold yellow]Stopping all resources...[/bold yellow]")
            aws_manager.stop_ec2_instances()
            aws_manager.pause_apprunner_services()
            azure_manager.stop_vms()

        elif choice == "3":
            while True:
                console.print("\n[bold cyan]AWS Resource Management[/bold cyan]")
                console.print("\n1. Start EC2 instances")
                console.print("2. Stop EC2 instances")
                console.print("3. Resume App Runner services")
                console.print("4. Pause App Runner services")
                console.print("5. Back to main menu")

                aws_choice = Prompt.ask("\nEnter your choice", choices=["1", "2", "3", "4", "5"])

                if aws_choice == "1":
                    aws_manager.start_ec2_instances()
                elif aws_choice == "2":
                    aws_manager.stop_ec2_instances()
                elif aws_choice == "3":
                    aws_manager.resume_apprunner_services()
                elif aws_choice == "4":
                    aws_manager.pause_apprunner_services()
                elif aws_choice == "5":
                    break

        elif choice == "4":
            while True:
                console.print("\n[bold cyan]Azure Resource Management[/bold cyan]")
                console.print("\n1. Start VMs")
                console.print("2. Stop VMs")
                console.print("3. Back to main menu")

                azure_choice = Prompt.ask("\nEnter your choice", choices=["1", "2", "3"])

                if azure_choice == "1":
                    azure_manager.start_vms()
                elif azure_choice == "2":
                    azure_manager.stop_vms()
                elif azure_choice == "3":
                    break

        elif choice == "5":
            console.print("\n[bold green]Goodbye![/bold green]")
            break

if __name__ == "__main__":
    main() 