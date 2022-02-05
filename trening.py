
b = 20
c = b/2.54
print('Равен в дюймах %s.' %c)


#Как код ниже разместить в одну строку?
in_file = open('C:/Users/Aleksey/Desktop/from_file.txt')
indata = in_file.read()

print( "Исходный файл имеет размер %s" % len(indata))

out_input = open('C:/Users/Aleksey/Desktop/to_file.txt', 'w')
out_input.write(indata)

out_input.close()
in_file.close()