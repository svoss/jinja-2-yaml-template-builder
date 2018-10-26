import os
import codecs
class Writer():
	def __init__(self, build_folder, to_console=False):
		self.build_folder = build_folder
		self.to_console = to_console
		self._prepare()

	def _prepare(self):
		if not self.to_console:
			self._make_sure_folder_exists(self.build_folder)

	def _make_sure_folder_exists(self, path):
		if not os.path.isdir(path):
			path = os.path.dirname(path)
		if not os.path.exists(path):
			os.makedirs(path)

	def write_to(self, f, content):
		if self.to_console:
			print(f)
			print("---")
			print(content)
			print("---")
		else:
			fn = os.path.join(self.build_folder, f)
			self._make_sure_folder_exists(fn)
			with codecs.open(fn, encoding='utf8', mode='w') as io:
				io.write(content)

