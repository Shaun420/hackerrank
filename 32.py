def taumBday(b, w, bc, wc, z):
	if bc > wc:
		if ((bc - wc) > z):
			return (w * wc) + (b * (wc + z))
		else:
			return (w * wc) + (b * bc)
	else:
		if ((wc - bc) > z):
			return (b * bc) + (w * (bc + z))
		else:
			return (b * bc) + (w * wc)

print("Result:",taumBday(3, 6, 9, 1, 1))
