from Preprocess import Preprocess
from FieldStats import FieldStatistics
from Imputation import ImputeData
from Transform import Transformer
from Plots import Plotting

class EDA(object):

	def __init__(self, df = None,
				continuous_features=[],
				unordered_categorical_features = [],
				ordered_categorical_features = []):
		self.data = df
		self.continuous_features = continuous_features
		self.unordered_categorical_features = unordered_categorical_features
		self.ordered_categorical_features = ordered_categorical_features
		self.prprcs = Preprocess()
		self.fs = FieldStatistics()
		self.trnsfrmr = Transformer()
		self.imptr = ImputeData()
		self.pltr = Plotting()

	def set_continuous_features(self, continuous_features):
		self.continuous_features = continuous_features
	
	def set_unordered_categorical_features(self, unordered_categorical_features):
		self.unordered_categorical_features = unordered_categorical_features
	
	def set_ordered_categorical_features(self, ordered_categorical_features):
		self.ordered_categorical_features = ordered_categorical_features

	def convert_objects_to_floats(self, features_to_transform):
		self.numerics = self.trnsfrmr.transform_objects_to_floats(self.data,features_to_transform)

	def convert_floats_to_objects(self, features_to_transform):
		self.numerics = self.trnsfrmr.transform_floats_to_objects(self.data,features_to_transform) 

	def edaPipeline(self):
		self.prprcs.handle_empty_notations(self.data)
		self.numerics = self.fs.get_numeric_data_types(self.data)
		self.objects = self.fs.get_object_data_types(self.data)
		return self.fs.get_null_fields(self.data)

	## define possible getter functions