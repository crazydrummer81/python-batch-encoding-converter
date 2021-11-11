import os
import codecs
import chardet
from shutil import copyfile 

source_folder = 'C:\\Users\\Mans\\Documents\\Dinect\\20211110-fixed\\'
target_folder = 'C:\\Users\\Mans\\Documents\\Dinect\\20211110-cp1251\\'

files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(source_folder) for f in filenames]

count = 0
nones = []
cp1251s = []
for source_filename in files:

	rel_path = source_filename.replace(source_folder, '')
	output_filename = target_folder + rel_path
	output_dir = os.path.dirname(output_filename)
	if not os.path.isdir(output_dir):
		print("New dir: %s", output_dir)
		os.makedirs(output_dir, exist_ok=True)

	rawdata = open(source_filename, "rb").read()
	encoding = chardet.detect(rawdata)['encoding']

	print("%d) %s: %s" % (count, encoding, source_filename))

	if (not encoding is None) and (encoding.lower() != 'windows-1251'):

		f = codecs.open(source_filename, 'r', encoding)
		u = f.read()   # now the contents have been transformed to a Unicode string
		out = codecs.open(output_filename, 'w', 'cp1251')
		out.write(u)   # and now the contents have been output as UTF-8
		count += 1

	elif encoding is None:

		nones.append(source_filename)
		copyfile(source_filename, output_filename)

	elif encoding.lower() == 'windows-1251':
		
		cp1251s.append(source_filename)
		copyfile(source_filename, output_filename)


print("Encoded: %s files" % count)
print("Nones: %s \n%s " % (len(nones), "\n".join(nones)))
print("cp1251s: %s \n%s" % (len(cp1251s), "\n".join(cp1251s)))
