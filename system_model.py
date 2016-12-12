from state_vars import get_properties
def plot_network():
	A = get_properties(293.0,0.05)
	B = get_properties(393.0,0.03)
	print A, B

plot_network()