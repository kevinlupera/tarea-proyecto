#importando modulos necesarios
#%matpltlib inline

import matpltlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns

np.random.seed(2016) #replicar random
sns.set_palette("deep", desat=.6)
#parametros esteticos de seaborn
sns.set_context(rc={"figure.figsize":(8, 4)})

# Graficando Exponencial
exponencial = stats.expon()
x = np.linspace(exponencial.ppf(0.01),
                exponencial.ppf(0.99), 100)
fp = exponencial.pdf(x) # Función de Probabilidad
plt.plot(x, fp)
plt.title('Distribución Exponencial')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()
