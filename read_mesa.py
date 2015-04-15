import re

def readMESALog (filename):
	history = {}
	with open(filename, 'rb') as history_file:
		rows = history_file.readlines()[5:] # Chop off the first 5 rows--we're only interested in the column labels and data
		labels = re.split(' +', rows[0])[1:][:-1] # Removing the '' and '\n' at the front and end of each row
		history['labels'] = labels

		for label in labels:
			history[label] = []

		for row_data in rows[1:]:
			row = re.split(' +', row_data)[1:][:-1]
			for i in range(len(row)):
				if re.match('^[\d\.\-E]+$', row[i]): # If it looks like a number, convert it to a float
					history[labels[i]].append(float(row[i]))
				else:
					history[labels[i]].append(row[i])
	return history

