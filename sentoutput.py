"""def correlation(stock_change, sentiment)
	if stock_change > 0 and sentiment > 0:
		return 'Correlated'
	if stock_change < 0 and sentiment < 0:
		return 'Correlated negatively'
	if stock_change > 0 and sentiment < 0:
		return 'No correlation'
	if stock_change < 0 and sentiment > 0:
		return 'No correlation'
	if stock_change = 0:
		return 'No change, Irrelevant'
"""

def correlation(stock_change, sentiment):
	correlation = []
	for element in stock_change:
		correl = (sentiment / stock_change)
		correlation.append(correl)
	return correlation
