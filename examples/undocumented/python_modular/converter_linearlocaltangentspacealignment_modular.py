#!/usr/bin/env python
from tools.load import LoadMatrix

lm=LoadMatrix()
data = lm.load_numbers('../data/fm_train_real.dat')

parameter_list = [[data,20],[data,30]]

def converter_linearlocaltangentspacealignment_modular (data,k):
	try:
		from shogun.Features import RealFeatures
		from shogun.Converter import LinearLocalTangentSpaceAlignment
		
		features = RealFeatures(data)
			
		converter = LinearLocalTangentSpaceAlignment()
		converter.set_target_dim(1)
		converter.set_k(k)
		converter.apply(features)

		return features
	except ImportError:
		print('No Eigen3 available')

if __name__=='__main__':
	print('LinearLocalTangentSpaceAlignment')
	converter_linearlocaltangentspacealignment_modular(*parameter_list[0])

