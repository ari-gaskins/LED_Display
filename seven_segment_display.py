# user input
user = str(input('Enter a number: '))

def seven_segment_converter(num_string):
    # digit rows 
    #FIXME turn this into dictionary for faster parsing
    one = ['#', '# ', '#', '#', '#']
    two = ['###', ' #', '###', '#  ', '###']
    three = ['###', '  #', '###', '  #', '###']
    four = ['# #', '# #', '###', '  #', '  #']
    five = ['###', '#  ', '###', '  #', '###']
    six = ['###', '#  ', '###', '# #', '###']
    seven = ['###', '  #', '  #', '  #', '  #']
    eight = ['###', '# #', '###', '# #', '###']
    nine = ['###', '# #', '###', '  #', '###']
    zero = ['###', '# #', '# #', '# #', '###']
    
    #FIXME change to check dictionary
    for row in range(5):
        print()
        for num in num_string:
            if num == '1':
                print(one[row], end=' ')
                continue
            
            elif num == '2':
                print(two[row], end=' ')
                continue
            
            elif num == '3':
                print(three[row], end=' ')
                continue
            
            elif num == '4':
                print(four[row], end=' ')
                continue
                
            elif num == '5':
                print(five[row], end=' ')
                continue
                
            elif num == '6':
                print(six[row], end=' ')
                continue
                
            elif num == '7':
                print(seven[row], end=' ')
                continue
            
            elif num == '8':
                print(eight[row], end=' ')
                continue
            
            elif num == '9':
                print(nine[row], end=' ')
                continue
                
            elif num == '0':
                print(zero[row], end=' ')
                continue
            
            else:
                print('Not a number.')
                break
                
seven_segment_converter(user)
    
