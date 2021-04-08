#plotear_temperaturas.py

import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.load("../Data/Temperaturas.npy")
plt.hist(temperaturas,bins=50)
plt.xlabel("Temperaturas")
plt.ylabel("Mediciones")
plt.title("Histograma de las temperaturas simuladas")