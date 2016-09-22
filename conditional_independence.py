#Notes from Udacity review on conditional indepence
#exampe of conditional independence.
#temperature of ice-cream and ice-cubes are correlated,
#but conditionally independent given the freezer's temp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#%matplotlib inline
plt.figure(figsize=(16, 8))

# Lets set the freezer's temperature
freezer = np.random.normal(-15, 4, 100)

# Lets take the temperatures of the ice-cream and of the ice-cubes
ice_cream = freezer + np.random.normal(0,0.5,100)
ice_cubes = freezer + np.random.normal(0,0.23,100)

df = pd.DataFrame({
        'freezer temp.': freezer,
        'ice-cream temp.': ice_cream,
        'ice-cubes temp.': ice_cubes,
        'ice-cream temp. given freezer temp.': ice_cream - freezer,
        'ice-cubes temp. given freezer temp.': ice_cubes - freezer,
    })

plt.subplot('121')
sns.regplot('ice-cream temp.', 'ice-cubes temp.', df)
plt.subplot('122')
sns.regplot('ice-cream temp. given freezer temp.',
            'ice-cubes temp. given freezer temp.',
            df, color='green')
