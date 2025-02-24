import os
import yaml

# write
def write_yaml(data):
    with open(os.getcwd()+"/extract.yaml",encoding="utf-8",mode="a+") as f:
        yaml.dump(data,stream=f,allow_unicode=True)
        
# read
def read_yaml(key):
    with open(os.getcwd()+"/extract.yaml",encoding="utf-8",mode="a+") as f:
        value = yaml.load(f,yaml.FullLoader)
        return value[key]