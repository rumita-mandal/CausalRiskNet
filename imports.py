import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from causalml.inference.meta import BaseTRegressor

plt.style.use("seaborn-v0_8")
np.random.seed(42)
