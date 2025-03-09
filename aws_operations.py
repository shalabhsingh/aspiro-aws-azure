import boto3
from rich.console import Console
from config import AWS_REGION, EC2_INSTANCES, APPRUNNER_SERVICES

console = Console()

class AWSResourceManager:
    def __init__(self):
        self.ec2_client = boto3.client('ec2', region_name=AWS_REGION)
        self.apprunner_client = boto3.client('apprunner', region_name=AWS_REGION)

    def start_ec2_instances(self):
        """Start all configured EC2 instances."""
        if not EC2_INSTANCES:
            console.print("[yellow]No EC2 instances configured[/yellow]")
            return

        try:
            response = self.ec2_client.start_instances(InstanceIds=EC2_INSTANCES)
            for instance in response['StartingInstances']:
                console.print(f"[green]Starting EC2 instance: {instance['InstanceId']}[/green]")
        except Exception as e:
            console.print(f"[red]Error starting EC2 instances: {str(e)}[/red]")

    def stop_ec2_instances(self):
        """Stop all configured EC2 instances."""
        if not EC2_INSTANCES:
            console.print("[yellow]No EC2 instances configured[/yellow]")
            return

        try:
            response = self.ec2_client.stop_instances(InstanceIds=EC2_INSTANCES)
            for instance in response['StoppingInstances']:
                console.print(f"[green]Stopping EC2 instance: {instance['InstanceId']}[/green]")
        except Exception as e:
            console.print(f"[red]Error stopping EC2 instances: {str(e)}[/red]")

    def resume_apprunner_services(self):
        """Resume all configured App Runner services."""
        if not APPRUNNER_SERVICES:
            console.print("[yellow]No App Runner services configured[/yellow]")
            return

        for service_arn in APPRUNNER_SERVICES:
            try:
                self.apprunner_client.resume_service(ServiceArn=service_arn)
                console.print(f"[green]Resuming App Runner service: {service_arn}[/green]")
            except Exception as e:
                console.print(f"[red]Error resuming App Runner service {service_arn}: {str(e)}[/red]")

    def pause_apprunner_services(self):
        """Pause all configured App Runner services."""
        if not APPRUNNER_SERVICES:
            console.print("[yellow]No App Runner services configured[/yellow]")
            return

        for service_arn in APPRUNNER_SERVICES:
            try:
                self.apprunner_client.pause_service(ServiceArn=service_arn)
                console.print(f"[green]Pausing App Runner service: {service_arn}[/green]")
            except Exception as e:
                console.print(f"[red]Error pausing App Runner service {service_arn}: {str(e)}[/red]") 