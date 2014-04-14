#
# Currently handles three kinds of files succesfully:-
# -- pdf files. 
# -- .docx files.
# -- plain text files.
#


from .models import ResumeWithFileField
 
import os
import magic 
#requires installation of magic.
# refer to the site : https://pypi.python.org/pypi/filemagic/

from docx import opendocx, getdocumenttext
# Requires installation of docx python library
# sudo pip install -e git://github.com/mikemaccana/python-docx.git#egg=docx

def handle_docx(input_path, output_path):
	try:
		document = opendocx(input_path)
		newfile = open(output_path, 'w')
	except:
		return 'Unable to open the file'

	paratextlist = getdocumenttext(document)
	newparatextlist = []
	for paratext in paratextlist:
		newparatextlist.append(paratext.encode("utf-8"))
	return '\n'.join(newparatextlist)

def file_handler(data_key):
	data=ResumeWithFileField.objects.get(id=data_key)
	data_dictionary = {}
	data_dictionary['name'] = data.name
	data_dictionary['upload_date'] = data.upload_date
	resume_path = str(data.resume_file)
	output = 'temp_out.txt'
	with magic.Magic(flags = magic.MAGIC_MIME_TYPE) as m:
		file_type = m.id_filename(resume_path)
	if(file_type == 'application/pdf'):
		os.system(("pdftotext %s %s") %(resume_path, output))
		fp = open(output, 'r')
		text = fp.read()
		data_dictionary['text'] = text
	elif(file_type == 'application/msword'):
		data_dictionary['text'] = handle_docx(resume_path, output)
	elif(file_type == 'text/plain'):
		fp = open(resume_path)
		text = fp.read()
		data_dictionary['text'] = text
	else:	
		data_dictionary['text'] = 'un-recognized file type'
	return data_dictionary
