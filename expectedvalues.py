import os
def expectedvalues():
	path = r"C:\Users\Nathan Chan\Downloads"
	with open(os.path.join(path, "rosalind_iev.txt")) as f:
		data = f.read()
	values = data.split(' ')
	a = int(values[0])
	b = int(values[1])
	c = int(values[2])
	d = int(values[3])
	e = int(values[4])
	f = int(values[5])
	n = a + b + c + d + e + f
	expectedpopulation = n * 2
	expected_values = (a/n + b/n + c/n + (d/n * 0.75) + (e/n * 0.5)) * expectedpopulation
	return expected_values
	print(data)
print(expectedvalues())