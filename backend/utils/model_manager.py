import yaml


def get_speech2text_urls(file_path="docker-compose.yml"):
    """
    Parses a Docker Compose YAML content to extract URLs of services 
    containing 'speech2text' in their names.

    Args:
    yaml_content (str): Path to the content of the Docker Compose YAML file 
        as a string.

    Returns:
    dict: A dictionary where keys are service names and values are 
        their corresponding ports.
    """
    with open(file_path, 'r') as file:
        yaml_content = file.read()

    data = yaml.safe_load(yaml_content)
    services = data['services']
    urls = {}

    for service_name, service_data in services.items():
        if 'speech2text' in service_name:
            port = None
            if 'ports' in service_data:
                port = service_data['ports'][0].split(':')[0]
            elif 'environment' in service_data:
                for env_var in service_data['environment']:
                    if env_var.startswith('PORT='):
                        port = env_var.split('=')[1]
                        break
            
            if port:
                urls[service_name] = port
    
    return urls