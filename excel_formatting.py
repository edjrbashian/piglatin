import xlwt

font = xlwt.Font() # Create the Font 
font.name = 'Times New Roman' 
font.bold = True
font.height = 400 #multiply font size by 20  
font.underline = True 
font.italic = True    
style = xlwt.XFStyle() # Create the Style 
style.font = font # Apply the Font to the Style 
worksheet.write(0, 0, 'Unformatted value',style) 