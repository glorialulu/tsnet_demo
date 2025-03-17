# -*- coding: utf-8 -*-
"""
Created on Fri May 20 16:58:38 2022

@author: ps28866
"""
import tsnet

import matplotlib.pyplot as plt
plt.close('all') 

#%% part 1: Getting started

# inp source file
#-------------------------------------------------
inp_file = 'Tnet1.inp'

# Open an example network and create a transient model
#-------------------------------------------------
tm = tsnet.network.TransientModel('networks/' + inp_file)

# Set wavespeed
#-------------------------------------------------
tm.set_wavespeed(1200.) # m/s

# Set time options
#-------------------------------------------------
tf = 20   # simulation period [s]
tm.set_time(tf)

# Set valve closure
#-------------------------------------------------
ts = 5 # valve closure start time [s]
tc = 1 # valve closure period [s]
se = 0 # end open percentage [s]
m = 2 # closure constant [dimensionless]
tm.valve_closure('VALVE',[tc,ts,se,m])

# Initialize steady state simulation
t0=0
tm = tsnet.simulation.Initializer(tm,t0)

# Transient simulation
#-------------------------------------------------
tm = tsnet.simulation.MOCSimulator(tm)


# Plot head at nodes
#-------------------------------------------------
node = 'N7'
node = tm.get_node(node)
fig = plt.figure(figsize=(10,4), dpi=80, facecolor='w', edgecolor='w')
plt.plot(tm.simulation_timestamps,node.head, 'k', lw=3, label = 'N7')
node = 'N5'
node = tm.get_node(node)
plt.plot(tm.simulation_timestamps,node.head, 'b', lw=3, label = 'N5')
node = 'N2'
node = tm.get_node(node)
plt.plot(tm.simulation_timestamps,node.head, 'm', lw=3, label = 'N2')
node = 'N3'
node = tm.get_node(node)
plt.plot(tm.simulation_timestamps,node.head, 'g', lw=3, label = 'N3')
plt.xlim([tm.simulation_timestamps[0],tm.simulation_timestamps[-1]])
#plt.title('Pressure Head at Node %s '%node)
plt.xlabel("Time [s]", fontsize=14)
plt.ylabel("Pressure Head [m]", fontsize=14)
plt.legend(loc='best')

# build in function to plot heads
#-------------------------------------------------
tm.plot_node_head(['N2', 'N3', 'N5', 'N7'])

# Plot velocity
#-------------------------------------------------
pipe = 'P7'
pipe = tm.get_link(pipe)
fig = plt.figure(figsize=(10,4), dpi=80, facecolor='w', edgecolor='w')
plt.plot(tm.simulation_timestamps,pipe.start_node_velocity,'k', lw=3, label='Start Node')
plt.plot(tm.simulation_timestamps,pipe.end_node_velocity, 'b', lw=3, label='End Node')
plt.xlim([tm.simulation_timestamps[0],tm.simulation_timestamps[-1]])
plt.title('Velocity in Pipe %s '%pipe)
plt.xlabel("Time [s]", fontsize=14)
plt.ylabel("Velocity [m/s]", fontsize=14)
plt.legend(loc='best')

#%% Slower valve closure
#-------------------------------------------------
# Open an example network and create a transient model
#-------------------------------------------------
tm1 = tsnet.network.TransientModel('networks/' + inp_file)

# Set wavespeed
#-------------------------------------------------
tm1.set_wavespeed(1200.) # m/s

# Set time options
#-------------------------------------------------
tf = 20   # simulation period [s]
tm1.set_time(tf)
ts = 5 # valve closure start time [s]
tc = 3 # valve closure period [s]
se = 0 # end open percentage [s]
m = 2 # closure constant [dimensionless]
tm1.valve_closure('VALVE',[tc,ts,se,m])

# Initialize steady state simulation
t0=0
tm1 = tsnet.simulation.Initializer(tm1,t0)

# Transient simulation
#-------------------------------------------------
tm1 = tsnet.simulation.MOCSimulator(tm1)

# Plot head at nodes
#-------------------------------------------------
node = 'N7'
node = tm1.get_node(node)
fig = plt.figure(figsize=(10,4), dpi=80, facecolor='w', edgecolor='w')
plt.plot(tm1.simulation_timestamps,node.head, 'k', lw=3, label = 'N7')
node = 'N5'
node = tm1.get_node(node)
plt.plot(tm1.simulation_timestamps,node.head, 'b', lw=3, label = 'N5')
node = 'N2'
node = tm1.get_node(node)
plt.plot(tm1.simulation_timestamps,node.head, 'm', lw=3, label = 'N2')
node = 'N3'
node = tm1.get_node(node)
plt.plot(tm1.simulation_timestamps,node.head, 'g', lw=3, label = 'N3')
plt.xlim([tm1.simulation_timestamps[0],tm1.simulation_timestamps[-1]])
#plt.title('Pressure Head at Node %s '%node)
plt.xlabel("Time [s]", fontsize=14)
plt.ylabel("Pressure Head [m]", fontsize=14)
plt.legend(loc='best')

# Plot velocity
#-------------------------------------------------
pipe = 'P7'
pipe = tm1.get_link(pipe)
fig = plt.figure(figsize=(10,4), dpi=80, facecolor='w', edgecolor='w')
plt.plot(tm1.simulation_timestamps,pipe.start_node_velocity,'k', lw=3, label='Start Node')
plt.plot(tm1.simulation_timestamps,pipe.end_node_velocity, 'b', lw=3, label='End Node')
plt.xlim([tm1.simulation_timestamps[0],tm1.simulation_timestamps[-1]])
plt.title('Velocity of Pipe %s '%pipe)
plt.xlabel("Time [s]", fontsize=14)
plt.ylabel("Velocity [m/s]", fontsize=14)
plt.legend(loc='best')