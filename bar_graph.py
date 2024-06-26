import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [34,65,76,89,12,29]
y = [12,34,53,21,9,70]

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.bar(x,y,color=['Red','Blue','Green','Pink','Black','Orange'])
plt.show()