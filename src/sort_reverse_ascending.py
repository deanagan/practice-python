def reverse_ascending(items):
	res, d = [], []
	for i,n in enumerate(items):

		if d and d[-1] >= n:
			res.extend(list(sorted(d, reverse=True)))
			d.clear()
		d.append(n)
	res.extend(sorted(d, reverse=True))
	return res
