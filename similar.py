file_path = 'ai.txt'  # Replace with the actual path or filename
file2_path = 'ai2.txt'


if (file_path.endswith(".txt") and file2_path.endswith(".txt")):
	print("Text file detected")


	with open(file_path, 'r') as file:
	    # Read the lines and store them into a list
	    file_content = file.readlines()
	# Display the content of the list
	print("Contents in file 1 are")
	print(file_content)
	print()

	with open(file2_path, 'r') as file:
	    # Read the lines and store them into a list
	    file2_content = file.readlines()
	# Display the content of the list
	print("Contents in file 1 are")
	print(file2_content)
	print()

	if file_content == file2_content:
		print("They are same")
	else:
		print("They are different")
		
elif (file_path.endswith(".pdf") and file2_path.endswith(".pdf")):
	pass
