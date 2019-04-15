sWORDS = ["बच्चा","लड़का","घोड़ा","गधा","बच्ची","लड़की","नदी","गली","माला","लता","शाखा","गाथा","माली","जोहरी","कूली","आदमी"]

ADD = ["आ","आओं","आयें","इयाँ","इयों","ई","ए","ओं"]

DEL = ["आ","आओं","आयें","इयाँ","इयों","ई","ए","ओं"]

#CORRECT_ANS_1 = ["आ","आ","आ","आ","आ","ए","ए","ओं"]
CORRECT_ANS_1 = [["Delete","Add","Number","Case"],["आ","आ","sing","dr"],["आ","आ","plu","dr"],["आ","आ","sing","ob"],["आ","आ","plu","ob"]]
#CORRECT_ANS_2 = ["ई","ई","ई","ई","ई","इयाँ","ई","इयों"]
CORRECT_ANS_2 = [["Delete","Add","Number","Case"],["ई","ई","sing","dr"],["ई","इयाँ","plu","dr"],["ई","ई","sing","ob"],["ई","इयों","plu","ob"]]
#CORRECT_ANS_3 = ["लता","आ","आ","आ","आ","आ","आयें","आ","आओं"]
CORRECT_ANS_3 = [["Delete","Add","Number","Case"],["आ","आ","sing","dr"],["आ","आयें","plu","dr"],["आ","आ","sing","ob"],["आ","आओं","plu","ob"]]
#CORRECT_ANS_4 = ["ई","ई","ई","ई","ई","ई","ई","इयों"]
CORRECT_ANS_4 = [["Delete","Add","Number","Case"],["ई","ई","sing","dr"],["ई","ई","plu","dr"],["ई","ई","sing","ob"],["ई","इयों","plu","ob"]]

ans=[]

CORRECT_ANS_1_index = ["0","0","0","0","0","6","6","7"]
CORRECT_ANS_2_index = ["5","5","5","5","5","3","5","4"]
CORRECT_ANS_3_index = ["0","0","0","0","0","2","0","1"]
CORRECT_ANS_4_index = ["5","5","5","5","5","5","5","3"]

#Taking user input for word(index)
print("Enter the word index ")
inputdata = int(input())

#Taking word for deletion(index)
del1 = (input())
del2 = (input())
del3 = (input())
del4 = (input())

#Taking word for addition(index)
add1 = (input())
add2 = (input())
add3 = (input())
add4 = (input())
count=0;
if inputdata>=1 and inputdata<=4:
	if del1==CORRECT_ANS_1_index[0] and add1==CORRECT_ANS_1_index[4]:
		ans.append("correct")
	else:
		ans.append("incorrect")
		++count

	if del2==CORRECT_ANS_1_index[1] and add2==CORRECT_ANS_1_index[5]:
		ans.append("correct")
	else:
		ans.append("incorrect")
		++count

	if del3==CORRECT_ANS_1_index[2] and add3==CORRECT_ANS_1_index[6]:
		ans.append("correct")
	else:
		ans.append("incorrect")
		++count

	if del4==CORRECT_ANS_1_index[3] and add4==CORRECT_ANS_1_index[7]:
		ans.append("correct")
	else:
		ans.append("incorrect")
		++count
	print(ans)
	print('\n')
	print('\n'.join(['\t'.join([str(cell) for cell in row])for row in CORRECT_ANS_1]))


elif inputdata>=5 and inputdata<=8:
	if del1==CORRECT_ANS_2_index[0] and add1==CORRECT_ANS_2_index[4]:
		ans.append("correct")
	else:
		ans.append("incorrect")
		++count

	if del2==CORRECT_ANS_2_index[1] and add2==CORRECT_ANS_2_index[5]:
		ans.append("correct")
	else:
		ans.append("incorrect")
		++count

	if del3==CORRECT_ANS_2_index[2] and add3==CORRECT_ANS_2_index[6]:
		ans.append("correct")
	else:
		ans.append("incorrect")
		++count

	if del4==CORRECT_ANS_2_index[3] and add4==CORRECT_ANS_2_index[7]:
		ans.append("correct")
	else:
		ans.append("incorrect")
		++count
	print(ans)
	print('\n')
	print('\n'.join(['\t'.join([str(cell) for cell in row])for row in CORRECT_ANS_2]))


elif inputdata>=9 and inputdata<=12:
	if del1==CORRECT_ANS_3_index[0] and add1==CORRECT_ANS_3_index[4]:
		ans.append("correct")
	else:
		ans.append("incorrect")		
		++count

	if del2==CORRECT_ANS_3_index[1] and add2==CORRECT_ANS_3_index[5]:
		ans.append("correct")	
	else:
		ans.append("incorrect")		
		++count

	if del3==CORRECT_ANS_3_index[2] and add3==CORRECT_ANS_3_index[6]:
		ans.append("correct")
	else:
		ans.append("incorrect")
		++count

	if del4==CORRECT_ANS_3_index[3] and add4==CORRECT_ANS_3_index[7]:
		ans.append("correct")
	else:
		ans.append("incorrect")
		++count
	print(ans)
	print('\n')
	print('\n'.join(['\t'.join([str(cell) for cell in row])for row in CORRECT_ANS_3]))


elif inputdata>=13 and inputdata<=16:
	if del1==CORRECT_ANS_4_index[0] and add1==CORRECT_ANS_4_index[4]:
		ans.append("correct")
	else:
		ans.append("incorrect")
		++count

	if del2==CORRECT_ANS_4_index[1] and add2==CORRECT_ANS_4_index[5]:
		ans.append("correct")
	else:
		ans.append("incorrect")
		++count

	if del3==CORRECT_ANS_4_index[2] and add3==CORRECT_ANS_4_index[6]:
		ans.append("correct")
	else:
		ans.append("incorrect")
		++count

	if del4==CORRECT_ANS_4_index[3] and add4==CORRECT_ANS_4_index[7]:
		ans.append("correct")
	else:
		ans.append("incorrect")
		++count
	print(ans)
	print('\n')
	print('\n'.join(['\t'.join([str(cell) for cell in row])for row in CORRECT_ANS_4]))
