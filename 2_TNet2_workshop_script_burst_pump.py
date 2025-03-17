
import tsnet

import matplotlib.pyplot as plt
plt.close('all') 

#%% TNet2: Burst event

inp_file = 'Tnet2.inp'


# Open an example network and create a transient model
#-------------------------------------------------
tm = tsnet.network.TransientModel('networks/' + inp_file)

# Set wavespeed and time
#-------------------------------------------------
tm.set_wavespeed(1200.) # [m/s]
tf = 20 # simulation duration[s]
dt = 0.01 # time step [s]
tm.set_time(tf, dt)

# Add burst
#-------------------------------------------------
ts = 1 # burst start time
tc = 1 # time for burst to fully develop
final_burst_coeff = 0.01 # final burst coeff [ m^3/s/(m H20)^(1/2)]
tm.add_burst('JUNCTION-105', ts, tc, final_burst_coeff)

# Initialize steady state simulation
#-------------------------------------------------
t0 = 0. # initialize the simulation at 0s
engine = 'DD' # or PPD
tm = tsnet.simulation.Initializer(tm, t0, engine)

# Transient Simulation
#-------------------------------------------------
results_obj = 'Tnet2_burst' # name of the object for saving results 
tm = tsnet.simulation.MOCSimulator(tm,results_obj)

# Visulize results 
tm.plot_node_head(['JUNCTION-105'])

#%% report results
# head
#-------------------------------------------------
node = 'JUNCTION-105'
node = tm.get_node(node)
fig = plt.figure(figsize=(10,4), dpi=80, facecolor='w', edgecolor='w')
plt.plot(tm.simulation_timestamps,node.head, 'k', lw=3,label = 'JUNCTION-105')
node = '109'
node = tm.get_node(node)
plt.plot(tm.simulation_timestamps,node.head, 'b', lw=3,label = 'JUNCTION-109')
node = '187'
node = tm.get_node(node)
plt.plot(tm.simulation_timestamps,node.head, 'g', lw=3,label = 'JUNCTION-187')
plt.xlim([tm.simulation_timestamps[0],tm.simulation_timestamps[-1]])
plt.xlabel("Time [s]", fontsize=14)
plt.ylabel("Pressure Head [m]", fontsize=14)
plt.legend(loc='best')
plt.grid(True)
plt.show()
fig.savefig('./networks/Tnet2_burst_head.pdf', format='pdf',dpi=100)

# burst discharge
#-------------------------------------------------
node = 'JUNCTION-105'
node = tm.get_node(node)
fig = plt.figure(figsize=(10,4), dpi=80, facecolor='w', edgecolor='k')
plt.plot(tm.simulation_timestamps,node.emitter_discharge,'b', lw=3, label='JUNCTION-105 Burst Discharge')
plt.xlim([tm.simulation_timestamps[0],tm.simulation_timestamps[-1]])
plt.xlabel("Time [s]", fontsize=14)
plt.ylabel("Burst discharge [m^3/s]", fontsize=14)
plt.legend(loc='best')
plt.grid(True)
plt.show()

# velocity
#-------------------------------------------------
pipe = 'PIPE-109'
pipe = tm.get_link(pipe)
fig = plt.figure(figsize=(10,4), dpi=80, facecolor='w', edgecolor='w')
plt.plot(tm.simulation_timestamps,pipe.start_node_velocity,'k', lw=3, label='PIPE-109-Start Node')
plt.plot(tm.simulation_timestamps,pipe.end_node_velocity,'b', lw=3, label='PIPE-109-End Node')
plt.xlim([tm.simulation_timestamps[0],tm.simulation_timestamps[-1]])
plt.title('Velocity of Pipe %s '%pipe)
plt.xlabel("Time [s]")
plt.ylabel("Velocity [m/s]")
plt.legend(loc='best')
plt.grid(True)
plt.show()
fig.savefig('./networks/Tnet2_burst_velocity.pdf', format='pdf',dpi=100)

