# -*- coding: utf-8 -*-
"""
Created on Mon May 23 13:46:10 2022

@author: ps28866
"""
import tsnet
import matplotlib.pyplot as plt
import numpy as np

plt.close('all') 

#%% TNet3: Retrieving simulation results
#-------------------------------------------------

# Burst event
#-------------------------------------------------
inp_file = 'networks/Tnet3.inp'
tm = tsnet.network.TransientModel(inp_file)

# Set wavespeed
#-------------------------------------------------
wavespeed = 1200
tm.set_wavespeed(wavespeed)

# Set time step
#-------------------------------------------------
tf = 20 # simulation period [s]
tm.set_time(tf)

# Add burst
#-------------------------------------------------
ts = 1 # burst start time
tc = 1 # time for burst to fully develop
final_burst_coeff = 0.01 # final burst coeff [ m^3/s/(m H20)^(1/2)]
tm.add_burst('JUNCTION-73', ts, tc, final_burst_coeff)

# Initialize steady state simulation
#-------------------------------------------------
t0 = 0. # initialize the simulation at 0s
engine = 'PDD' # or Epanet
tm = tsnet.simulation.Initializer(tm, t0, engine)

# Transient simulation
#-------------------------------------------------
result_obj = 'Tnet3_burst_event' # name of the object for saving simulation results
tm_burst = tsnet.simulation.MOCSimulator(tm,result_obj)

#%% Valve closure
#-------------------------------------------------

tm = tsnet.network.TransientModel(inp_file)

# Set wavespeed
#-------------------------------------------------
tm.set_wavespeed(wavespeed)

# Set time step
#-------------------------------------------------
tf = 20 # simulation period [s]
tm.set_time(tf)

# Set valve closure
#-------------------------------------------------
ts = 1 # valve closure start time [s]
tc = 1 # valve closure period [s]
se = 0 # end open percentage [s]
m = 1 # closure constant [dimensionless]
valve_op = [tc,ts,se,m]
tm.valve_closure('VALVE-175',valve_op)

# Initialize steady state simulation
#-------------------------------------------------
t0 = 0. # initialize the simulation at 0s
engine = 'DD' # or Epanet
tm = tsnet.simulation.Initializer(tm, t0, engine)

# Transient simulation
#-------------------------------------------------
result_obj = 'Tnet3_valve_closure_event' # name of the object for saving simulation results
tm_valve = tsnet.simulation.MOCSimulator(tm,result_obj)

#%%  Pump shutoff
#-------------------------------------------------
tm = tsnet.network.TransientModel(inp_file)

# Set wavespeed
#-------------------------------------------------
tm.set_wavespeed(wavespeed)

# Set time step
#-------------------------------------------------
tf = 20 # simulation period [s]
tm.set_time(tf)

# Set pump shut off
#-------------------------------------------------
tc = 2 # pump closure period
ts = 1 # pump closure start time
se = 0 # end open percentage
m = 1 # closure constant
pump_op = [tc,ts,se,m]
tm.pump_shut_off('PUMP-172', pump_op)

# Initialize steady state simulation
#-------------------------------------------------
t0 = 0. # initialize the simulation at 0s
engine = 'DD' # or Epanet
tm = tsnet.simulation.Initializer(tm, t0, engine)

# Transient simulation
result_obj = 'Tnet3_pump_shutoff_event' # name of the object for saving simulation results
tm_pump = tsnet.simulation.MOCSimulator(tm,result_obj)

#%% report results
import pickle

file = open('Tnet3_burst_event.obj', 'rb')
tm_burst = pickle.load(file)

file = open('Tnet3_valve_closure_event.obj', 'rb')
tm_valve = pickle.load(file)

file = open('Tnet3_pump_shutoff_event.obj', 'rb')
tm_pump = pickle.load(file)

#-------------------------------------------------
node = 'JUNCTION-20'
node = tm_burst.get_node(node)
fig = plt.figure(figsize=(10,4), dpi=80, facecolor='w', edgecolor='w')
plt.plot(tm_burst.simulation_timestamps,node.head, 'k', lw=3,label = 'Burst')

#-------------------------------------------------
node = 'JUNCTION-20'
node = tm_valve.get_node(node)
plt.plot(tm_burst.simulation_timestamps,node.head, 'b', lw=3,label = 'Valve')

#-------------------------------------------------
node = 'JUNCTION-20'
node = tm_pump.get_node(node)
plt.plot(tm_pump.simulation_timestamps,node.head, 'r', lw=3,label = 'Pump')
plt.xlim([tm_burst.simulation_timestamps[0],tm_burst.simulation_timestamps[-1]])

plt.xlabel("Time [s]", fontsize=14)
plt.ylabel("Head [m]", fontsize=14)
plt.legend(loc='best')
plt.title('Transient response at %s '%node)
plt.grid(True)
plt.show()
fig.savefig('./networks/Tnet3_get_all_results.pdf', format='pdf',dpi=100)

