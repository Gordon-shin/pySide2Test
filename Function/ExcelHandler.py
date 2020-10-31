import hashlib
import os

import pandas
from PySide2.QtWidgets import QMessageBox


class ExcelHandler(object):
	# 构造方法
	def __init__(self, path,output_path, columns, flag):
		self.path = path
		self.filename = os.path.basename(path)
		self.output_path = output_path
		#columns表示要加密的列
		self.columns = columns.split(",")
		self.flag = flag
	def create_md5_xls(self):
		head = self.columns
		dfs = pandas.read_excel(self.path, sheet_name=0)
		print(dfs.keys())
		for item in head:
			dfs[item] = [self.md5(str(val), "utf-8") for val in dfs[item]]
		output = os.path.join(self.output_path,self.filename)
		dfs.to_excel(output)



	@staticmethod
	def md5(str, encoding):
		m1 = hashlib.md5()
		m1.update(str.encode(encoding))
		hash = m1.hexdigest()
		return hash


if __name__ == '__main__':
	excel = ExcelHandler;
	# 读取xlsx文件方法
	head = ['Applicant', 'Accepted']
	dfs = pandas.read_excel("D:\\5.xlsx", sheet_name=1)  # can also index sheet by name or fetch all sheets
	print(dfs.keys())
	for item in head:
		dfs[item] = [excel.md5(str(val), "utf-8") for val in dfs[item]]
	dfs.to_excel("dfs.xlsx")
	print(dfs)
