import json
import re


def parse_postman_collection(file_path, target_section_name):
    """Load the JSON file and find the target section."""
    with open(file_path, "r") as f:
        collection = json.load(f)

    # Postman collections use an "item" key for sections.
    # We search for an item with a matching name.
    for section in collection.get("item", []):
        if section.get("name", "").lower() == target_section_name.lower():
            return section
    raise ValueError(f"Section '{target_section_name}' not found in the collection.")


def extract_endpoint_details(item):
    """
    Given a Postman endpoint (item), extract basic details:
     - name: the endpoint name
     - method: the HTTP method
     - endpoint: the URL path (cleaned of base URL variables)
     - description: a description for documentation
     - body: sample payload in raw format (if any)
    """
    request = item.get("request", {})
    method = request.get("method", "GET")
    # The URL is often stored in a sub-dict under "url" with a "raw" key.
    url_raw = request.get("url", {}).get("raw", "")
    # Remove the environment variable base (e.g. "{{url}}")
    endpoint = url_raw.replace("{{url}}/api/v2", "").strip().split("?")[0]
    try:
        params = (
            url_raw.replace("{{url}}/api/v2", "")
            .strip()
            .split("?")[1]
            .replace("=", ":")
        )
    except IndexError:
        params = "NO PARAMS USED IN THIS METHOD"
    description = request.get("description", "").strip()
    body = request.get("body", {}).get("raw", "").strip()

    return {
        "name": item.get("name", "unnamed"),
        "method": method.upper(),
        "endpoint": endpoint,
        "params": params,
        "description": description,
        "body": body,
    }


def safe_snake_case(text: str) -> str:
    """Convert a text string to snake_case ignoring punctuation."""
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    return "_".join(text.lower().split())


def generate_method_code(details):
    """
    Generate a method based on endpoint details.
    This template uses a single payload parameter.
    You may extend it to auto-generate individual parameters
    by parsing the details['body'] JSON.
    """
    # Create a method name combining the HTTP method and endpoint name.
    http_method = details["method"].lower()  # e.g., post, get, etc.
    name_suffix = safe_snake_case(details["name"])
    method_name = f"{http_method}_{name_suffix}"

    # Build a docstring. Use the description if available,
    # otherwise default to a standard message.
    doc_lines = []
    if details["description"]:
        doc_lines.append(details["description"])
    else:
        doc_lines.append("{{Description of what the endpoint does}}")

    doc_lines.append("")
    doc_lines.append("Args:")
    if http_method == "get" or http_method == "delete":
        doc_lines.append("      {{Adjust for params you add}}")
    elif http_method == "put":
        doc_lines.append("      payload (dict): Updates to apply.")
    elif http_method == "post":
        doc_lines.append("      payload (dict): New configuration.")

    doc_lines.append("")
    doc_lines.append("Returns:")
    doc_lines.append("    {{data type}}: {{small detail of what is returned}}")
    docstring = "\n        ".join(doc_lines)

    if "NO PARAMS" not in details["params"]:
        params_stringified = "{"
        if "&" in details["params"]:
            params_list = details["params"].split("&")
            for p in params_list:
                string_split = p.split(":")
                key = string_split[0]
                value = string_split[1]
                params_stringified += f"'{key}':'{value}',"
        else:
            string_split = details["params"].split(":")
            key = string_split[0]
            value = string_split[1]
            params_stringified += f"'{key}':'{value}',"
        params_stringified += "}"

        details["params"] = params_stringified
    # Build the method code. Here we assume that you will supply any needed parameters
    # via a generic `payload` dictionary. In your example, you had several explicit parameters.
    # Extending this function to parse the expected JSON schema could allow more detailed signatures.
    if http_method == "get" or http_method == "delete":
        method_code = (
            f"    def {method_name}(self, 'ADD YOUR PARAMS HERE'):\n"
            f'        """{docstring}\n\n'
            f'        """\n'
            f'        endpoint = "{details["endpoint"]}"\n\n'
            f"        params = {details['params']}\n\n"
            f"        return self._requester.{http_method}(endpoint, params=params)\n\n"
        )
    else:
        method_code = (
            f"    def {method_name}(self, payload: dict = {{}}):\n"
            f'        """{docstring}\n\n'
            f'        """\n'
            f'        endpoint = "{details["endpoint"]}"\n\n'
            f'        params = "{details["params"]}"\n\n'
            f"        return self._requester.{http_method}(endpoint, params=params, data=payload)\n\n"
        )
    return method_code


def generate_class_code(section, class_name):
    """
    Build the whole class as a string.
    Iterates through each endpoint in the target section,
    and writes the corresponding method in the class.
    """
    class_lines = [
        "from .base_endpoint import BaseEndpoint",
        "",
        f"class {class_name}(BaseEndpoint):",
        "    def __init__(self, *args, **kwargs):",
        "        super().__init__(*args, **kwargs)",
        "",
    ]

    method_type_lines = {
        "get": ["    #GET", ""],
        "post": ["    #POST", ""],
        "put": ["    #PUT", ""],
        "delete": ["    #DELETE", ""],
    }

    # Each endpoint in the section's "item" is processed.
    for item in section.get("item", []):
        details = extract_endpoint_details(item)
        method_code = generate_method_code(details)
        if "def get" in method_code:
            method_type_lines["get"].append(method_code)
        elif "def post" in method_code:
            method_type_lines["post"].append(method_code)
        elif "def put" in method_code:
            method_type_lines["put"].append(method_code)
        elif "def delete" in method_code:
            method_type_lines["delete"].append(method_code)

    for v in method_type_lines.values():
        for line in v:
            class_lines.append(line)

    return "\n".join(class_lines)


class testingArgs:
    section = "Administatrators"
    class_name = "Administrators"


def main():
    # parser = argparse.ArgumentParser(
    #     description="Generate API endpoint class from a Postman JSON collection"
    # )
    # parser.add_argument(
    #     "--section", help="Name of the section to generate endpoints for"
    # )
    # parser.add_argument(
    #     "--class-name",
    #     help="Name for the generated class",
    #     default="GeneratedEndpoints",
    # )
    # args = parser.parse_args()

    args = testingArgs()
    try:
        section = parse_postman_collection(
            "./assets/Odin API.postman_collection.json", args.section
        )
    except ValueError as e:
        print(e)
        return

    class_code = generate_class_code(section, args.class_name)
    # Output to stdout or write to a file
    print(class_code)
    file_name = safe_snake_case(args.class_name)
    with open(f"./{file_name}.py", "w") as file:
        for line in class_code:
            file.write(line)


if __name__ == "__main__":
    main()
