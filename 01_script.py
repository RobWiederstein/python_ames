# Author: Pedro Marcelino
# Title: Comprehensive data exploration with Python
# Url: https://www.kaggle.com/code/pmarcelino/comprehensive-data-exploration-with-python/notebook
# invite people for the Kaggle party
import inline as inline
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats

import warnings
warnings.filterwarnings('ignore')
#%matplotlib inline

#import pandas as pd
#bring in the six packs
df_train = pd.read_csv('./input/train.csv')