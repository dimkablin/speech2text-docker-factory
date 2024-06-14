import docker

client = docker.from_env()

def get_running_models():
    containers = client.containers.list()
    models = [container.name for container in containers if 'speech2text' in container.name]
    return models
