import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from termcolor import colored as cl
from joblib import dump

from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree

rcParams['figure.figsize'] = (25, 20)

df = pd.read_csv('../tools/train_data.csv')
df.drop('Unnamed: 0', axis = 1, inplace = True)

X_var = df[['Canny', 'contrast', 'FFT', 'frequency', 'Laplacian', 'SSIM']].values
y_var = df['is_blurry'].values

X_train, X_test, y_train, y_test = train_test_split(X_var, y_var, test_size = 0.2, random_state = 0)

model = dtc(criterion = 'entropy', max_depth = 4, min_samples_split=20, min_samples_leaf=10)
model.fit(X_train, y_train)

pred_model = model.predict(X_test)

print(pred_model)

print(cl('Accuracy of the model is {:.0%}'.format(accuracy_score(y_test, pred_model)), attrs = ['bold']))

feature_names = df.columns[:6]
target_names = [str(name) for name in df['is_blurry'].unique().tolist()]

plot_tree(model,
          feature_names = feature_names,
          class_names = target_names,
          filled = True,
          rounded = True)

plt.savefig('../tools/decision_tree_visualization_clear_all_blurry.png')

dump(model, '../tools/decision_tree_model_clear_all_blurry.joblib')