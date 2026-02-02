import pandas as pd
import numpy as np
import sys

def topsis():
    if len(sys.argv) != 5:
        print("Usage: topsis <input_file> <weights> <impacts> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = list(map(float, sys.argv[2].split(',')))
    impacts = sys.argv[3].split(',')
    output_file = sys.argv[4]

    data = pd.read_csv(input_file)

    matrix = data.iloc[:, 1:].values.astype(float)

    # Step 1: Normalize
    norm = np.sqrt((matrix ** 2).sum(axis=0))
    normalized = matrix / norm

    # Step 2: Apply weights
    weighted = normalized * weights

    # Step 3: Ideal best and worst
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted[:, i].max())
            ideal_worst.append(weighted[:, i].min())
        else:
            ideal_best.append(weighted[:, i].min())
            ideal_worst.append(weighted[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Distance calculation
    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # Step 5: TOPSIS score
    score = dist_worst / (dist_best + dist_worst)

    data['Topsis Score'] = score
    data['Rank'] = data['Topsis Score'].rank(ascending=False).astype(int)

    data.to_csv(output_file, index=False)
    print("Result saved successfully")
