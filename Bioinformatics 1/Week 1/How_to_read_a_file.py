def read_genome(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

file_path = "MinSkew.txt"
genome = read_genome(file_path)