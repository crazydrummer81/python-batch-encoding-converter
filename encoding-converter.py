import os
import codecs
import chardet
from shutil import copyfile 

source_folder = 'D:\\Temp\\0000-dinect\\20211111\\unconverted'
target_folder = 'D:\\Temp\\0000-dinect\\20211111\\utf-8'
target_encoding = 'utf-8'
target_encoding_str = 'utf-8' # Need for check with OS
# target_encoding = 'cp1251'
# target_encoding_str = 'windows-1251' # Need for check with OS

files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(source_folder) for f in filenames]

count = 0
nones = []
allready_in_target_encoding = []
for source_filename in files:

	rel_path = source_filename.replace(source_folder, '')
	output_filename = target_folder + rel_path
	output_dir = os.path.dirname(output_filename)
	if not os.path.isdir(output_dir):
		print("New dir: %s" % output_dir)
		os.makedirs(output_dir, exist_ok=True)

	rawdata = open(source_filename, "rb").read()
	encoding = chardet.detect(rawdata)['encoding']

	print("%d) %s: %s" % (count, encoding, source_filename))

	if (not encoding is None) and (encoding.lower() != target_encoding_str):

		f = codecs.open(source_filename, 'r', encoding)
		u = f.read()   # now the contents have been transformed to a Unicode string
		out = codecs.open(output_filename, 'w', target_encoding)
		out.write(u)   # and now the contents have been output as UTF-8
		count += 1

	elif encoding is None:

		nones.append(source_filename)
		copyfile(source_filename, output_filename)

	elif encoding.lower() == target_encoding:
		
		allready_in_target_encoding.append(source_filename)
		copyfile(source_filename, output_filename)


print("Encoded: %s files" % count)
print("Nones: %s \n%s " % (len(nones), "\n".join(nones)))
print("allready_in_target_encoding: %s \n%s" % (len(allready_in_target_encoding), "\n".join(allready_in_target_encoding)))