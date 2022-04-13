from parl.utils import summary
import numpy as np

if __name__ == "__main__":
    for i in range(10):
        x = np.random.random(1000)
        summary.add_histogram('distribution centers', x + i, i)