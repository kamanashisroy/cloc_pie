"""
This code generates pie chart out of cloc summary file
"""
from pylab import *
import re

# read cloc generated file
lineno = 0
# The slices will be ordered and plotted counter-clockwise.
labels = []
fracs = []
#labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
#fracs = [15, 30, 45, 10]
#explode=(0, 0.05, 0, 0)

with open(sys.argv[1], 'r') as f:
	for line in f:
		lineno += 1
		if lineno < 5 :
			continue
		if line.startswith('--'):
			continue
		if line.startswith('SUM'):
			continue
		m = re.search('^([a-zA-Z/+\s4]+)+\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)$', line);
		labels.append(m.group(1))
		fracs.append(m.group(5))
f.closed

# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])
pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True)
#title('Language pie', bbox={'facecolor':'0.8', 'pad':5})

#show()
savefig("pie.svg")
