def parse_metrics(file_content):
    data = {}
    current_group = None

    for line in file_content.split('\n'):
        line = line.strip()
        if not line:
            continue

        if line.startswith('#'):  # New group
            current_group = line[1:].strip()  # Remove '#' and extra spaces
            data[current_group] = {}
        elif line.startswith('-'):  # Metric line
            if current_group is not None:
                metric, value = line[2:].split(':', 1)  # Split at the first colon
                metric = metric.strip('**').strip()  # Remove '**' and extra spaces
                value = value.strip()
                data[current_group][metric] = value
            else:
                print("Error: Metric found outside of a group")
        else:
            print("Unrecognized line format:", line)

    return data

def read_from_markdown(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    return file_content

# Example usage:
file_path = 'test.md'  # Replace with your Markdown file path
file_content = read_from_markdown(file_path)
parsed_data = parse_metrics(file_content)
print(parsed_data)