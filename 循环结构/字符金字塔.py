letter = str(input())
letter_so = letter.upper()
pos = ord(letter_so) - ord("A") + 1
letter_total = 'A''B''C''D''E''F''G''H''I''J''K''L''M''N''O''P''Q''R''S''T''U''V''W''X''Y''Z'
for i in range (1, pos + 1):
	letter = letter_total[i-1]
	left = letter_total[:1]
	right = letter_total[i-2::-1]
	line = left + right
	spaces = pos - i
	print(""*spaces + line)
    
	       
            
                 
            
            
            
            
    