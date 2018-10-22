from yaml import load, dump
import os
class Vars():
	def __init__(self, vars = None):
		if vars is None:
			self.vars = {}

	def _load_file(self, fn):
		if not os.path.exists(fn):
			raise ValueError("file '{}' not found".format(fn))
		with open(fn, encoding='utf8') as io:
			self.vars.update(load(io))

	def _set_recursive_path(self, path, value):
		path = path.split(".")
		n = 0
		V = self.vars
		for p in path:
			n += 1
			if n == len(path):
				V[p] = value
			else:
			 	V[p] = {}
			 	V = V[p]
			
	def get_as_dic(self):
		return self.vars

	def load_cli_args(self, args):
		if args is None:
			return
		for arg in args:
			s = arg.split("=",1)
			if len(s) < 2:
				raise ValueError("No = sign found for argument")
			self._set_recursive_path(s[0], s[1])

	def load_config_files(self, folder, files):
		if not os.path.exists(folder):
			raise ValueError("{} does not exist".format(folder))
		for f in files:
			fn = os.path.join(folder, f)
			self._load_file(fn)