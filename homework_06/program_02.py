import json, os
import shutil


PARENT_DIR = "quotes_output"

with open("quotes.json", 'r') as quotes_file:
	data = json.load(quotes_file)

#if the parent directory already there, we will delete it
if os.path.exists(PARENT_DIR):
	shutil.rmtree(PARENT_DIR)#os.rmdir(PARENT_DIR)

os.mkdir(PARENT_DIR) #parent directory
os.chdir(PARENT_DIR) #change directory so that we are inside the parent directory
print("Created parent directory ", PARENT_DIR)

for node in data:
	corrected_author = node["author"].replace(" ", "_") if node["author"] is not None else "Unknown"
	dir_name = corrected_author.replace(" ", "_")
	os.mkdir(dir_name) if not os.path.exists(dir_name) else print("{} already exists".format(dir_name))
	os.chdir(dir_name) # go inside the newly created directory
	ticker = 1
	while os.path.exists(f'{corrected_author}_{ticker}.txt'):
	  ticker += 1
	with open(f'{corrected_author}_{ticker}.txt', 'w') as owf:
	  owf.write(node["text"])
	os.chdir("..") # go one level up in the directory tree