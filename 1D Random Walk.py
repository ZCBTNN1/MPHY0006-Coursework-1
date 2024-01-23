# import of random module (for random number generation) and matplotlib (for graph plotting)

import random
import matplotlib.pyplot as plt
import numpy as np

# Define number of walk simulations,and number of steps per walk
num_walks = int(input("how many walks should be simulated? ")) # total number of walks simulated
num_steps = int(input("how many steps should be completed per walk? ")) #number of steps of each walk simulation
step_direction=[]

#Creating a list of 1 and -1 values
prob_up=str(input("input the fractional probability of an positive direction step in the form x/y = "))
prob_numdenom=prob_up.split("/")
numer=int(prob_numdenom[0])
denom=int(prob_numdenom[1])
prob_up=numer/denom

for i in range(numer):
  step_direction.append(1)
for i in range(denom-numer):
  step_direction.append(-1) 
#add more "1" values to step_direction list to increase chances of step in the
#positive direction, and "-1" values for the negative direction

y_pos_data = [[] for i in range(num_walks)] #Create 2D array, with 'num_walks' number of nested arrays

# generation of random walk steps
for i in range(num_walks):
  current_y_pos=0
  y_pos_data[i].append(0)
  for j in range(num_steps):
    current_y_pos+=step_direction[random.randint(0,len(step_direction)-1)]
    y_pos_data[i].append(current_y_pos)

# first plot, line graph of random walks
##creating list of x values, x = step number
x=[]
for i in range(num_steps+1):
    x.append(i)

##plotting all random walks onto a single line graph
plt.figure(figsize=(8,6))
plt.title("random walk simulations")
for i in range(num_walks):
  for t in range(num_steps-1): #t represents an arbitrary time step 
    current_walk_data=y_pos_data[i]
    plt.plot(x,current_walk_data)                  #where 1t corresponds to 1 step

# second plot, histogram of final positions for each walk
## attain final positions of each walk
experimental_final_positions=[]
for i in range(num_walks): #attain data from all walks
    experimental_final_positions.append(y_pos_data[i][num_steps])
print("all experimental final positions ", experimental_final_positions)

## mean and standard deviation of final positions
mean_positions=np.mean(experimental_final_positions)
print("mean: ", mean_positions)
stdev_positions=np.std(experimental_final_positions)
print("stdev: ", stdev_positions)

## Create list of all possible final positions for histogram
all_theoretical_final_positions=[]
for i in range((2*num_steps)+1):
    all_theoretical_final_positions.append(i-num_steps)
    all_theoretical_final_positions.append(i-num_steps+0.5)
print("all theoretical final positions ", all_theoretical_final_positions)

## attain probabilities of final positions from experimental_final_positions
experimental_final_positions_count=[] #a list to count the frequency of each end position
for i in range((2*num_steps)+1):
    count_of_i=experimental_final_positions.count(i-num_steps)
    experimental_final_positions_count.append(count_of_i/num_walks) #counts are converted into probabilities
print("experimental final positions count ", experimental_final_positions_count) #by dividing by num_walks 
print("total probability: ", np.sum(experimental_final_positions_count))

## plotting histogram

#plt.figure(figsize=(8,8))
#fig, ax = plt.subplots()
#plt.style.use("default")
#plt.title("Histogram of final positions of Simulated Walks")
#plt.ylabel("Frequency of Position Occurring")
#plt.xlabel("Displacement from Starting Position")
#plt.grid(True)
#plt.bar(all_theoretical_final_positions,experimental_final_positions_count)
#hist=plt.hist(experimental_final_positions,bins=all_theoretical_final_positions, label = 'Histogram', color="blue")

##Plot normal dist
#x=np.linspace(-num_steps,num_steps,250)
#y=(2*num_walks/(stdev_positions*np.sqrt(2*np.pi)))*(np.e)**((-(x-mean_positions)**2)/(2*(stdev_positions**2)))
#NormalDist=plt.plot(x,y, color="red", alpha=0.5, label = "Scaled & Fitted Normal Distribution")

#ax.legend(handles=[hist[2], NormalDist[0]], labels=[f'Histogram Data\n(n={num_walks}, steps={num_steps})', f'Normal Distribution \n(Scaled)\n $\mu$={round(mean_positions,3)} ,$\sigma$={round(stdev_positions, 3)}'], loc='upper right')

## plotting bar chart

## Create list of all possible final positions for bar chart
all_theoretical_final_positions_bar=[]
for i in range((2*num_steps)+1):
    all_theoretical_final_positions_bar.append(i-num_steps)
print("all theoretical final positions (bar): ", all_theoretical_final_positions_bar)

## plot bar chart
plt.figure(figsize=(10,10))
fig, ax = plt.subplots()
plt.style.use("default")
plt.title("Bar Chart of final positions of Simulated Walks")
plt.ylabel("Probability of Position Occurring")
plt.xlabel("Displacement from Starting Position")
plt.grid(True)
barchart=plt.bar(all_theoretical_final_positions_bar,experimental_final_positions_count, color="mediumblue")

## plot normal dist (experimental)
x=np.linspace(-num_steps,num_steps,250)
y=(2/(stdev_positions*np.sqrt(2*np.pi)))*(np.e)**((-(x-mean_positions)**2)/(2*(stdev_positions**2)))
NormalDist=plt.plot(x,y, color="red", alpha=0.55, label = "Scaled & Fitted Normal Distribution")

## plot normal dist (theoretical)
theonorm_mean=(num_steps*prob_up)-(num_steps*(1-prob_up))
theonorm_stdev= np.sqrt(num_steps*(prob_up)*(1-prob_up))
theo_x=np.linspace(-num_steps,num_steps,250)
theo_y= (2/(theonorm_stdev*np.sqrt(2*np.pi)))*(np.e)**((-(x-theonorm_mean)**2)/(2*(theonorm_stdev**2)))
theo_NormalDist=plt.plot(theo_x,theo_y, linestyle="dashed", color="green", alpha=0.55, label="Theoretical Normal Distribution")

## plot legend
if step_direction.count(-1)>step_direction.count(1):
    location="upper right"
if step_direction.count(1) >= step_direction.count(-1):
    location="upper left"

ax.legend(handles=[barchart[2], NormalDist[0], theo_NormalDist[0]], labels=[f'Bar Chart Data\n(n={num_walks}, steps={num_steps})', f'Normal Distribution \n(Scaled)\n($\mu$={round(mean_positions,3)}, $\sigma$={round(stdev_positions, 3)})', f'Theoretical\nNormal Distribution\n($\mu$={round(theonorm_mean,3)}, $\sigma$={round(theonorm_stdev,3)})'], loc=location)
