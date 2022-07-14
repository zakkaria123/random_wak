from random import choice
#creating the random walk class and storing each values of the walk in lists
class RandomWalk():   
  def __init__(self,number_of_points):
    self.number_of_points=number_of_points
    self.x_values=[0]
    self.y_values=[0]
  def fill_walk(self):
    while len(self.x_values)<self.number_of_points:
      x_distance,y_distance=choice([0,1,2,3,4]),choice([0,1,2,3,4])
      x_direction,y_direction=choice([-1,1]),choice([-1,1])
      x_step=x_distance*x_direction
      y_step=y_distance*y_direction
      if x_step==0 and y_step==0:                 #ignore stationary movements
        continue
      x=self.x_values[-1]+x_step
      y=self.y_values[-1]+y_step
      self.x_values.append(x)
      self.y_values.append(y)

def plot_rand_walk():
  import matplotlib.pyplot as plt       #library for visualizing 
  while True:
    walk=RandomWalk(80000)              #number of times for random walks
    walk.fill_walk()
    points=range(walk.number_of_points)
    fig,my_plot=plt.subplots()
    #fading the random walk we use the cmap
    my_plot.scatter(walk.x_values,walk.y_values,c=points,cmap=plt.cm.Greens,s=2,edgecolors='none')
    my_plot.scatter(walk.x_values[-1],walk.y_values[-1],c='red',s=100)
    my_plot.scatter(0,0,c='cyan',s=100)
    plt.title('Random Walk by Zakaria123')
    plt.show()
    user_input=input('Plot again? yes/no: ').lower()
    #to run code over and over again until we no longer want to create plots
    if user_input=='no':
      break
      
plot_rand_walk()      
    
