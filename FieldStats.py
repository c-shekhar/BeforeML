from config import numeric_data_types,object_data_types

class FieldStatistics(object):
	
	def __init__(self):
		pass

	def get_numeric_data_types(self, adf):
		return list(adf.select_dtypes(include=numeric_data_types).columns)

	def get_object_data_types(self, adf):
		return list(adf.select_dtypes(include=object_data_types).columns)

	def get_null_fields(self, adf):
		return adf.isnull().sum()

	def get_skewness(self, adf):
		feat_skewness = {}
		for feat in adf.columns:
			if feat not in feat_skewness:
				feat_skewness[feat] = adf[feat].skew()
		return feat_skewness