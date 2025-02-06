import yaml


config = {
    "version": 1,
    "services": {
        "web": {"image": "nginx:latest", "ports": [80, 443]},
        "db": {"image": "postgres:14", "environment": {"POSTGRES_DB": "mydb"}}
    }
}

yaml_str = yaml.dump(config)
print(yaml_str)
print(type(yaml_str))

load_yaml = yaml.safe_load(yaml_str)
print(load_yaml)
print(type(load_yaml))