# Aspiro AWS Azure Resource Manager

A Python-based tool for managing AWS and Azure cloud resources. This tool helps automate the process of starting/stopping EC2 instances and managing App Runner services.

## Features

- Start/Stop AWS EC2 instances
- Resume/Pause AWS App Runner services
- Rich console output for better visibility
- Configurable resource management

## Prerequisites

- Python 3.7+
- AWS credentials configured
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/aspiro-aws-azure.git
cd aspiro-aws-azure
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your AWS credentials and update the config.py file with your resource IDs.

## Usage

Run the appropriate commands to manage your cloud resources:

```python
from aws_operations import AWSResourceManager

# Initialize the manager
manager = AWSResourceManager()

# Start EC2 instances
manager.start_ec2_instances()

# Resume App Runner services
manager.resume_apprunner_services()
```

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 