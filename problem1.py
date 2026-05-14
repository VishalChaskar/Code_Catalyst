input_data = "72-101-108-108-111"
 
ascii_values = input_data.split('-')
 
result = ''.join(chr(int(num)) for num in ascii_values)
 
print(result)