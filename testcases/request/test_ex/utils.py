# Utility functions (e.g., JSON handling)

import json

def j_print(j_data):
    print(json.dumps(j_data, indent=4, ensure_ascii=False))