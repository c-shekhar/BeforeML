from config import empty_notations

class Preprocess(object):

	def __init__(self):
		pass

	def handle_empty_notations(self, adf):
		for col in adf.columns:
			try:
				adf[col].replace(empty_notations.keys(),empty_notations.values(),inplace=True)
			except Exception as e:
				pass
