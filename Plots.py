class Plotting(object):

	def __init__(self):
		pass

	def multiplot(self, data, features, plottype, nrows, ncols, figsize, y=None, colorize=False):
		""" This function draw a multi plot for 3 types of plots ["regplot","distplot","countplot"]"""
		n = 0
		plt.figure(1)
		fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
		
		if colorize:
			colors = sns.color_palette(n_colors=(nrows*ncols))
		else :
			colors = [None]*(nrows*ncols)
			
		for row in range(ncols):
			for col in range(nrows):
				
				if plottype == 'regplot':
					if y == None:
						raise ValueError('y value is needed with regplot type')
					
					sns.regplot(data = data, x = features[n], y = y ,ax=axes[row,col], color = colors[n])
					correlation = np.corrcoef(data[features[n]],data[y])[0,1]
					axes[row,col].set_title("Correlation {:.2f}".format(correlation))
				
				elif plottype == 'distplot':
					sns.distplot(a = data[features[n]],ax = axes[row,col],color=colors[n])
					skewness = data[features[n]].skew()
					axes[row,col].legend(["Skew : {:.2f}".format(skewness)])
				
				elif plottype in ['countplot']:
					g = sns.countplot(x = data[features[n]], y = y, ax = axes[row,col],color = colors[n])
					g = plt.setp(g.get_xticklabels(), rotation=45)
			
				n += 1
		plt.tight_layout()
		plt.show()
		plt.gcf().clear()

	def corrmat(self, data, features_list, corr_threshold=0.5, figsize=(20,15), cmap="RdYlGn", annot=True):
		corrmat = data[features_list].corr()
		top_corr_features = corrmat.index[abs(corrmat["EffectiveLossPaid"])>=corr_threshold]
		fig = plt.gcf()
		fig.set_size_inches(figsize)
		g = sns.heatmap(final_df[top_corr_features].corr(),annot=True,cmap=cmap)
		plt.tight_layout()
		plt.show()
		plt.gcf().clear()

	def joinplot(self, data):
		g = sns.jointplot(x = final_df['Value of Home'], y = final_df['JV'],kind="reg")
		
