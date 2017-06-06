#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math

class Pendulo:
#inicialização
	def __init__(self, m, l, x, v):
		self.m= m
		self.l= l
		self.x= x
		self.v= v
		self.w2= g/l
		self.T= 2*math.pi*math.sqrt(l/g)
		self.e= 0.5*m*(self.l*self.v)**2 +self.m*g*self.l*(1-math.cos(self.x))
#aceleração	
	def a(self, x, v, t1):
		return -self.w2*math.sin(x) -gama*v +A*math.sin(wf*t1)
#movimentação
	def move(self, t1):
		at= self.a(self.x, self.v, t1)
		self.x= self.x +self.v*dt +0.5*at*(dt**2)
		atem= self.a(self.x, self.v, t1)
		vtem= self.v +0.5*(at+atem)*dt
		atem= self.a(self.x, vtem, t1)
		self.v= self.v +0.5*(at+atem)*dt
		self.at= self.a(self.x, self.v, t1)
		self.e= 0.5*self.m*(self.l*self.v)**2 +self.m*g*self.l*(1-math.cos(self.x))
#declaração das variáveis	
g=9.8
A=0
gama=0
wf=2./3.
t1=0
dt=0.01
#objeto
p1= Pendulo(1., 10., math.pi/2, 0)
#arrays
tmax=10*p1.T
t=np.arange(0,tmax,dt)
x=np.zeros(t.size)
v=np.zeros(t.size)
e=np.zeros(t.size)
x[0]=p1.x
v[0]=p1.v
e[0]=p1.e

for i in range(t.size):
	p1.move(t[i])
	x[i]=p1.x
	v[i]=p1.v
	e[i]=p1.e

plt.figure(figsize=(8,5),dpi=100)
plt.axis ([0,100,-1,1])
ax=plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["bottom"].set_position(("data",0))
ax.spines["left"].set_position(("data",0))
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.autoscale()

plt.rc('text',usetex=True)
plt.rc('font',**{'sans-serif':'Arial','family':'sans-serif'})
plt.xlabel(r'\textnormal{t}')
plt.ylabel(r'\textnormal{}')
plt.title(r'\textnormal{Pendulo (A=0,gama=0)}',fontsize=12)

plt.plot(t,x,'-b',linewidth=1,label="Theta")
plt.plot(t,v,'-g',linewidth=1,label="Velocidade")
plt.plot(t,e,'-r',linewidth=1,label="Energia")
plt.legend(loc="upper right")
plt.grid()
plt.savefig("pre.pdf",dpi=96)
plt.show()
