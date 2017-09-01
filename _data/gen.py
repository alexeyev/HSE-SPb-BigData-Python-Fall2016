import random 

with open("sparse_matrix_huge.csv", "w") as wr_file: 
    for i in range(5000):
        row = ["0"] * 5000
        row[i] = str(random.random())
        row[random.randint(0, 5000)] = str(random.random())
        wr_file.write(",".join(row) + "\n")
