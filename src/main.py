#!/usr/local/bin/python

import argparse
import os
from builder import Builder
from variables import Vars
from writer import Writer

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("folder")
	parser.add_argument("--build_dir", default="build/", required=False)
	parser.add_argument('-a','--arg', action='append', help='List of arguments, arguments will always overwrite config folder files', required=False)
	parser.add_argument('-c','--config', action='append', help='Config file with parameters', required=False)
	parser.add_argument('-f','--file', action='append', help='Limit build to these files or folders, multiple paths supported', required=False)
	parser.add_argument('-v','--verbose', help="Print text to console", action='store_true', required=False)
	return parser.parse_args()

def main():
	args = parse_args()
	V = Vars()
	writer = Writer(args.build_dir, args.verbose)
	b = Builder(args.folder, writer)

	if args.config is not None:
		V.load_config_files(args.folder, args.config)
	V.load_cli_args(args.arg)
	if args.file is not None:
		b.build_files(args.file, V)
	else:
		b.build(V)

if __name__ == "__main__":
	main()