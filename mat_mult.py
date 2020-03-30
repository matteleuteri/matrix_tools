import pandas as pd
import numpy as np

def process_matrices(m1, m2):
	mat1 = m1.to_numpy()
	mat2 = m2.to_numpy()
	#test that matrix shapes are correct
	print(mat1.shape)
	m = mat1.shape[0]
	n1 = mat1.shape[1]
	n2 = mat2.shape[0]
	p = mat2.shape[1]
	if n1 != n2:
		#matrix mult only defined when above dimensions match
		print("dimensions different")
	return mat1, mat2

def inner_product(v1, v2):
	#takes in a row v1 and column v2, two vectors
	total = 0
	for i in range(v2.shape[0]):
		#calculate sum of elements at i
		total = total + (v1[i]*v2[i])
		#only one index because we have vectors
	return total

def calc_product(m1, m2):
	ans = np.zeros((m1.shape[0],m2.shape[1]))
	for i in range(m1.shape[0]):
		for j in range(m2.shape[1]):
			ans[i,j]=inner_product(m1[i,:], m2[:,j])
	return ans

def main():
	input1=pd.read_csv("mat.txt", header=None)
	input2=pd.read_csv("mat_inv.txt", header=None)
	matrix1, matrix2 = process_matrices(input1, input2)
	mat_product = calc_product(matrix1, matrix2)
	print(mat_product)
	return

if __name__ == "__main__":
	main()

