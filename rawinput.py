import numpy as npb
import matplotlib.pyplot as plt
from pylab import *
import os 
import string 

from analyzer1 import *


# print 'hello'

def comp_name():
	for i in range(2):
		a = raw_input("Please enter a company name:  ") # to ask password
		c = { 'JCPenney': 'RadioShack'}
	for i in c: # the password
		if a ==  i in c: # if the password entered and the password are the same to print.
			pass
			#print("You have successfully logged in")
			#exit()# to terminate the program.  Using 'break' instead of 'exit()' will allow your shell or idle to dump the block and continue to run.
		else: # if the password entered and the password are not the same to print.
			print("You have entered an invalid company name, please try again ")
			if i == 2:
				print("You have been denied access")
			exit() # to terminate the program

# comp_name()







print 'Welcome to the Stock Sentiment Analyzer!' 
original = raw_input ("What company are you interested in learning more about? \n")
if len(original) >3 : 
     pass
else: 
     print 'Please enter a valid company name before preceeding'





"""Visulization segment"""

"""Pie Chart"""

# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = 'Positive', 'Negative', '',''
#% of each sentiment category
fracs = [60, 40, 0, 0]

##  The highlights the FB wedge, pulling it out slightly from the pie.
explode=(0, 0.05, 0, 0)
pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
title('Sentiment Analysis', bbox={'facecolor':'0.8', 'pad':5})




"""Distribution graph"""
figure(2)
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Sentece Count Count')
plt.ylabel('Sentiment')
plt.title('Grammer Analysis')

#distribution
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)


"""Correlation Graph"""
figure(3)
ax = plt.subplot(111)
#correlation data
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

#plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            #arrowprops=dict(facecolor='black', shrink=0.05),
            #)

plt.ylim(-2,2)


show()

