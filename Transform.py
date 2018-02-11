class Transformer(object):

	def __init__(self):
		pass

	def transform_objects_to_floats(self, adf, features_list):
		for feat in features_list:
			adf[feat] = adf[feat].astype(float)

	def transform_floats_to_objects(self, adf, features_list):
		for feat in features_list:
			adf[feat] = adf[feat].astype(str)

	def log_transform_positive_skew(self, adf, features_to_transform=None, skewness_threshold=1):
		if not features_to_transform:
			for feat in adf.columns:
				if adf[feat].skew() > skewness_threshold:
					adf[feat] = np.log1p(adf[feat])
		elif features_to_transform:
			for feat in adf.columns:
				if adf[feat].skew() > skewness_threshold:
						adf[feat] = np.log1p(adf[feat])

	def categorical_label_encoder(self):
		pass

	def categorical_dummy_encoder(self):
		pass

	def high_cardinality_features_encoder(self):
		pass
 
	# def exp_transform_negative_skew(self, adf, features_to_transform=None, skewness_threshold=1):
	# 	if not features_to_transform:
	# 		for feat in adf.columns:
	# 			if adf[feat].skew() < skewness_threshold:
	# 				adf[feat] = np.exp(adf[feat])
	# 	elif features_to_transform:
	# 		for feat in adf.columns:
	# 			if adf[feat].skew() < skewness_threshold:
	# 					adf[feat] = np.exp(adf[feat])