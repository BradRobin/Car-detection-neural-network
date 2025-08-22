import os

def filter_labels(folder):
    for file in os.listdir(folder):
        if file.endswith('.txt'):
            file_path = os.path.join(folder, file)
            with open(file_path, 'r') as f:
                lines = f.readlines()
            with open(file_path, 'w') as f:
                for line in lines:
                    if line.startswith('0'):
                        f.write(line)

# Filter train and valid labels
filter_labels(r'C:\Users\bradr\OneDrive\Documents\GitHub\Car-detection-neural-network\data\train\labels')
filter_labels(r'C:\Users\bradr\OneDrive\Documents\GitHub\Car-detection-neural-network\data\valid\labels')