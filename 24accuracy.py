# 24accuracy.py by Adele Ferrer

def accuracy(tp, fp, tn, fn):
	precision = tp / (tp + fp)
	recall = tp / (tp + fn)
	f1 = 2 * ((precision * recall) / (precision + recall))
	accuracy = (tp + tn) / (tp + fn + tn + fp)
	return f1, accuracy 

print(accuracy(8, 2, 9, 3))
print(accuracy(80, 10, 90, 20))
print(accuracy(77, 5, 89, 7))