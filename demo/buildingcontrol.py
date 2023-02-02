import pandas as pd
import matplotlib.pyplot as plt
import pulp
import numpy as np

# Loading RC models
from python_rcmodels import *

# Preprocessing
path_RCmodels = '../data/'
file = 'calibrated_models.csv'
df_RC = pd.read_csv(path_RCmodels+file, index_col='identification_number')

H = 100  # problem horizon
dt = 10/60  # sampling frequency [1/h]
random_data = np.random.rand(H, 2)
tidx = pd.date_range('2022-01-01', periods=H, freq='10T')
dfw = pd.DataFrame(random_data, columns=['T_a', 'Q_sol'], index=tidx)

# System parameters 
c_opr = 0.22  #euro/kWh of heat input
c_comf = 1    # euro/C comfort penalty
T_set = 20
hp_capacity = 30  # kWh


# Defining LP problem & variables  
my_lp_problem = pulp.LpProblem("My_LP_Problem", pulp.LpMinimize)

# Continuous Variables
u_heat = pulp.LpVariable.dicts('u_heat', range(H), lowBound=0, upBound=hp_capacity, cat='Continous')  # heat input
T_blg = pulp.LpVariable.dicts('T_blg', range(H+1), lowBound=0, cat='Continuous')  # Building inside temperature
cost_comf = pulp.LpVariable.dicts('comf_cos', range(H+1), lowBound=0, cat='Continuous')  # Building inside temperature

# Objective function
cost_opr = c_opr * sum(u_heat[t] for t in range(H))
for t in range(H+1):
    my_lp_problem += cost_comf[t] >= c_comf * (T_set - T_blg[t])
my_lp_problem += cost_opr + sum(cost_comf[t] for t in range(H+1))

# Building model
b = df_RC.index.tolist()[0]
my_lp_problem = RCmodel(my_lp_problem, df_RC.loc[b, 'model_name'], dfw, T_blg, u_heat, H, dt, b, s=1, T_set=T_set)

# Initial conditions
my_lp_problem += T_blg[0] == T_set


# Optimization
print('Problem constructed!')
status = my_lp_problem.solve()
print(pulp.LpStatus[status])
print('Optimal solution found is: ' + str(pulp.value(my_lp_problem.objective)))


# Results extraction
df_res = pd.DataFrame(columns=["heat", "T"])
for t in range(H):
    df_res.loc[t, "heat"] = pulp.value(u_heat[t])
    df_res.loc[t, "T"] = pulp.value(T_blg[t])
    df_res.loc[t, "comfort_cost"] = pulp.value(cost_comf[t])
df_res.loc[0, "objective"] = pulp.value(my_lp_problem.objective)


# Results visualization
fig, axs = plt.subplots(2, 1)
axs[0].plot(df_res.index, df_res["T"].values, c='b')
axs[0].axhline(y=T_set, color='red', linestyle='--')
axs[0].set(ylabel='Building inside Temp [C]',
           title='Optimized control variables')
axs[0].grid()
axs[1].plot(df_res.index, df_res["heat"].values, c='red')
axs[1].set(xlabel='time steps (5min)', ylabel='Heat input [kw]')
axs[1].grid()
plt.show()


# Saving results
df_res.to_csv('buildingcontrol_res.csv')