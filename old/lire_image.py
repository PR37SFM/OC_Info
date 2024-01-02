message = 'Entrez votre message:'
filename_out = input(message)
while len(filename_out) == 0:
    print('! text is empty')
    filename_out = input(message)
filename_out = filename_out + '.png'
print(filename_out)