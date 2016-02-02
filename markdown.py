"""
This code generates Markdown table out of cloc summary tables.
"""
import re
import sys

# read cloc generated file

lineno = 0
with open(sys.argv[2], 'w') as m:
	with open(sys.argv[1], 'r') as f:
		for line in f:
			lineno += 1
			if lineno < 3 :
				continue
			if lineno == 3:
				titles = line.split()
				m.write(titles[0] + " | " + titles[1] + " | "  + titles[2] + " | " + titles[3] + " | " + titles[4] + " |\r\n")
				m.write("-- | -- | -- | -- | -- | ")
				continue
			if line.startswith('--'):
				continue
			mat = re.search('^([a-zA-Z/+\s4:]+)+\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)$', line);
			m.write(mat.group(1) + " | " + mat.group(2) + " | " + mat.group(3) + " | " + mat.group(4) + " | " + mat.group(5) + "\r\n")
	f.closed
m.closed

