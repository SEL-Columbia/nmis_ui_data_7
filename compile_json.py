import os
import yaml
import simplejson as json

def convert_json_to_yaml():
    with open("schema_original.json", "r") as json_file:
        json_str = json_file.read()
    yaml_s = yaml.safe_dump(json.loads(json_str))
    with open("schema.yaml", "w") as yaml_file:
        yaml_file.write(yaml_s)

def convert_yaml_to_json(yf_path, jf_path):
    with open(yf_path, "r") as yaml_file:
        yaml_str = yaml_file.read()
    json_s = json.dumps(yaml.load(yaml_str), indent=4)
    with open(jf_path, "w") as json_file:
        json_file.write(json_s)

def convert_all_yaml_to_json(root_file):
    yaml_files = []
    for root, dirs, files in os.walk(root_file):
        if ".git" not in root:
            for file in files:
                if file.endswith(".yaml"):
                    yaml_files.append(os.path.join(root, file))
    for yaml_file_path in yaml_files:
        json_file_path = yaml_file_path.replace(".yaml", ".json")
        convert_yaml_to_json(yaml_file_path, json_file_path)
    print "Compiled %d file(s) from YAML to JSON" % len(yaml_files)

convert_all_yaml_to_json(".")