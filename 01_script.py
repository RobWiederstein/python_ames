#invite people for the Kaggle party
import inline as inline
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
#add warnings
import warnings
warnings.filterwarnings('ignore')
#%matplotlib inline

#import pandas as pd
#bring in the six packs
df_train = pd.read_csv('./input/train.csv')