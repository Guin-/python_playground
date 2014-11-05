# get all file names
# for each file
#  rename(remove numbers)

def rename_files():
	# Get file names from a folder
	file_list = os.listdir(r"path") 
	# print file_list
	saved_path = os.getcwd()
	print ("current Working Directory is " + saved_path)
	os.chdir(r"path")
	# For each file, rename filename
	for file_name in file_list:
		print ("Old Name -" + file_name)
		print ("New Name -" + file_name.translate(None, "0123456789"))

		os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()

# if you try to rename a file that does not exist an error will occur
# if we try to rename a file that already exists 
