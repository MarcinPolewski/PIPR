import yaml
import json

if __name__ == "__main__":
    with open("posts.json") as f:
        data = json.load(f)

    with open("posts.yaml", "w") as f:
        yaml.safe_dump(data, f)
