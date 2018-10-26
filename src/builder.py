import os
import jinja2

class Builder:
	def __init__(self, folder, writer):
		self.folder = folder
		self.writer = writer
		self._create_environment()

	def _create_environment(self):
		if not os.path.exists(self.folder):
			raise ValueError("{} does not exist".format(self.folder))
		self.template_folder = os.path.join(self.folder, 'templates')
		if not os.path.exists(self.template_folder):
			raise ValueError("No templates subfolder found in '{}'".format(self.folder))
		fps = [self.template_folder]
		fp_helpers = os.path.join(self.folder, 'includes')
		if os.path.exists(fp_helpers):
			fps.append(fp_helpers)
		loader = jinja2.FileSystemLoader(fps)
		self.environment = jinja2.Environment(loader=loader, undefined=jinja2.StrictUndefined)

	def _build_template(self, fn, V):
		tmp = self.environment.get_template(fn)
		self.writer.write_to(fn, tmp.render(V.get_as_dic()))

	def build_files(self, files, V):
		for fn in files:
			if os.path.isdir(fn):
				self._build_template(fn, V)
			else:
				self.build(V, fn)

	def build(self, V, subfolder=''):
		base = os.path.join(self.template_folder, subfolder)
		with os.scandir(base) as scan:
			for f in scan:
				path = os.path.join(subfolder, f.name)
				if f.is_file() and f.name.endswith('.yaml') or f.name.endswith('.yml'):  
					self._build_template(path, V)
				elif not f.name.startswith('.') and f.is_dir():
					self.build(V, path)
