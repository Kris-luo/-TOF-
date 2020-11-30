import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

from 晶面计算配合numpy import *


#---------------------晶面原子数与粒径关系图————————————————————————————————————————————————————————————————
the_input_data = eval('[%s]'% input('please input pariticle size (for example: 1,2,3) : '))
particle_size = np.array(the_input_data)
the_last_coefficiency = -(particle_size/1.105/0.276)**3 - 6
new_list_m = []
for i in the_last_coefficiency:
    coefficiency = [16,-33,24,i]
    new_list_m.append(np.roots(coefficiency)[0])
    #计算三元方程m值

loading = float(input('what is the loading ')) 
   
result = particles_sum(new_list_m,loading)
Ns_111 = result[0].tolist()
Ns_100 = result[1].tolist()
Ns_edge = result[3].tolist()
Ns_corner = result[2].tolist()
Ns_surface = result[4].tolist()

print(Ns_corner)


#————————————————————————————归一化TOF与粒径关系图——————————————————————————————————
reaction_rate = float(input('please input your reaction rate'))
TOF_result = TOF_caculation(reaction_rate,Ns_111,Ns_100,Ns_edge,Ns_corner)
TOF111 = TOF_result[0].tolist()
TOF100 = TOF_result[1].tolist()
TOFedge = TOF_result[2].tolist()
TOFcorner = TOF_result[3].tolist()
print(TOFcorner)

'''Normalized_TOF_result = Normalized_TOF(TOF111,TOF100,TOFedge,TOFcorner)
Normalized_TOF111 = Normalized_TOF_result[0].tolist()
Normalized_TOF100 = Normalized_TOF_result[1].tolist()
Normalized_TOFedge = Normalized_TOF_result[2].tolist()
Normalized_TOFcorner = Normalized_TOF_result[3].tolist()'''




""" #-------------------作图---------------------------
fig1,(ax,ax2,ax3) = plt.subplots(3,1, sharex = True)
#多图绘制法,1行两列的图
ax.plot(the_input_data,Ns_surface,linewidth= 4.0 , color = 'red' , linestyle= '-',marker='o', label='surface')
ax2.plot(the_input_data,Ns_111,linewidth= 4.0 , color = 'blue' ,linestyle= '-',marker='o'  ,  label='facet (111)')
ax2.plot(the_input_data, Ns_100 , linewidth= 4.0 ,color = 'green' , linestyle= '-',marker='o', label='facet (100)')
ax2.plot(the_input_data, Ns_edge , linewidth= 4.0 ,color = 'orange' , linestyle= '-',marker='o', label='facet (edge)')
ax2.plot(the_input_data, Ns_corner , linewidth= 4.0 ,color = 'pink' , linestyle= '-',marker='o', label='facet (corner)')

ax.set_ylim(3*10**18,4.4*10**18)#分段
ax2.set_ylim(0,1.7*10**18)#分段数据

ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
#将两个并排的图的上下坐标轴隐藏

#ax.xaxis.tick_top()
#use ticks only on top
#ax.tick_params(labeltop = 'off')
ax2.xaxis.tick_bottom()

plt.subplots_adjust(wspace= 0.15)
d = .015 # how big to make the diagonal lines in axes coordinates
# arguments to pass plot, just so we don't keep repeating them

kwargs=dict(transform=ax.transAxes, color='k', clip_on=False) # switch to the bottom axes
ax.plot((-d,d),(-d,+d), **kwargs) # top-left diagonal
ax.plot((1-d,1+d),(-d,d), **kwargs) # top-right diagonal

kwargs.update(transform=ax2.transAxes)
ax2.plot((-d,+d),(1-d,1+d), **kwargs) # bottom-left diagonal
ax2.plot((1-d,1+d),(1-d,1+d), **kwargs) # bottom-left diagonal
ax.set_ylabel('Number of atoms')


# What's cool about this is that now if we vary the distance between
# ax and ax2 via f.subplots_adjust(hspace=...) or plt.subplot_tool(),
# the diagonal lines will move accordingly, and stay right at the tips
# of the spines they are 'breaking'plt.plot(the_input_data,Normalized_TOF111, 'bo')
ax3.plot(the_input_data,Normalized_TOF100, 'bo')
ax3.plot(the_input_data,Normalized_TOFedge, 'bo')
ax3.plot(the_input_data,Normalized_TOFcorner, 'bo')
ax3.set_xlabel('Particle size')
ax3.set_ylabel('Normalized TOF') 
plt.show()
 """





""" plt.plot(the_input_data, Ns_111 , linewidth= 4.0 , linestyle= '-',marker='o'  ,  label='facet (111)')
plt.plot(the_input_data, Ns_100 , linewidth= 4.0 , linestyle= '-',marker='o', label='facet (100)')
plt.plot(the_input_data, Ns_surface,linewidth= 4.0 , linestyle= '-',marker='o', label='surface')
plt.xlabel('Particle size')
plt.ylabel('Number of atoms')
#plt.title('Interesting Graph\nCheck it out')
plt.legend(loc='best',frameon = False)
plt.show() """
#晶面原子数与粒径关系图





    
    

    
    



    

    




