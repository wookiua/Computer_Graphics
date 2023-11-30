import matplotlib.pyplot as plt

def read_dataset(file_DS5):
    with open(file_DS5, 'r') as file:
        pairs = file.readlines()
        dataset = [list(map(int, line.strip().split())) for line in pairs]
    return dataset

def all_points(dataset):
    x_values = [point[1] for point in dataset]
    y_values = [point[0] for point in dataset]

    plt.figure(figsize=(960/80, 540/80))

    plt.scatter(x_values, y_values, color='blue', marker='o')

    plt.savefig('output_plot.png')
    
    plt.show()

file_DS5 = 'DS5.txt'
dataset = read_dataset(file_DS5)
all_points(dataset)
