def endex(): 
        lan="This is javaScript"
        get=input("insert your letter")
	for index,value in enumerate(lan):
		              if(value== get):
			          val=lan.append(index)
				  print(val)

endex('i')
