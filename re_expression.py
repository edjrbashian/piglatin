import os, sys, re
id_list = [" rober", "bobken", " samantha"]
  
no_space = []
for i in id_list:
	no_space.append(re.sub("^\s+", "", i)) # replace space before string with nothing in i
  	
print no_space
  	
  	
  	
  	
                       	