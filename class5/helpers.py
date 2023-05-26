import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

def plot_density_qq(dataset, col):

    plt.figure(figsize=(7, 3))
    plt.subplot(1, 2, 1)
    sns.distplot(dataset[col], bins=30)
    plt.title("Histograma y Densisdad")

    plt.subplot(1, 2, 2)
    stats.probplot(dataset[col], dist="norm", plot=plt)
    plt.title("Q-Q Plot")
    plt.show()

def detectOutliersLimits(dataset, col):
     '''
     Descripción: Calcula los limites superiores e inferiores para detección de outliers.
     Input: dataset-> pandas dataframe, col -> string nombre de columna
     Output: tupla de floats con los limites superior e inferior
     '''
     IQR = dataset[col].quantile(0.75) - dataset[col].quantile(0.25)
     LI =  dataset[col].quantile(0.25) - (IQR*1.75)
     LS = dataset[col].quantile(0.75) + (IQR*1.75)

     return LI, LS


def is_normal_dist(dataset, col):
     sesgo = round(dataset[col].skew(), 3)
     kurtosis = round(dataset[col].kurt(), 3)
     normal_sesgo = False
     normal_kurtosis = False
     etiqueta = 'No es Normal'
     normal = False

     if((sesgo >= -0.1) and (sesgo <= 0.1)):
          normal_sesgo = True
     else:
          normal_sesgo = False

     if((kurtosis >= 2.8) and (kurtosis <= 3.2)):
          normal_kurtosis = True
     else:
          normal_kurtosis = False

     if(normal_sesgo and normal_kurtosis):
          etiqueta = 'Es Normal'
          normal = True

     print(f"{col} - Asimetría: {sesgo} - Curtosis: {kurtosis} - {etiqueta}")
     return normal