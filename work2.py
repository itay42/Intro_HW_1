
######################### A #########################

def reverseWord(word):
    index = 1
    new_word = 'i'
    for char in word:
        new_word = new_word + word[len(word) - index]
        index = index + 1
    return new_word[1:]

def reverse(sentence, reverse_word):
    
    if type(reverse_word) != str or type(sentence) != str:
        return 'invalid input'
    
    index_start = sentence.find(reverse_word)
    
    if index_start == -1:
        return 'The word was not found'
    
    if index_start != -1:
        new_word = reverseWord(reverse_word)
        new_sentence = sentence[0:index_start] + new_word + sentence[index_start+len(new_word):]
        return new_sentence
    
######################### B #########################
 
# e Symbolizes equation
# i Symbolizes index
# n Symbolizes number
# act Symbolizes action
# action a symbolizes action  *- 
# action b symbolizes action /-

#Calculate in string and bring back in string 2 number and the action between them. n1 need to be first
def cla(n1, action, n2):
    if action == '-':
        return str(float(n1) - float(n2))
    if action == '+':
        return str(float(n1) + float(n2))
    if action == '*':
        return str(float(n1) * float(n2))
    if action == '/':
        return str(float(n1) / float(n2))
    if action == '^':
        return str(float(n1) ** float(n2))
    if action == 'a':
        return str(float(n1) * float(n2)*(-1))
    if action == 'b':
        return str(float(n1) / float(n2)*(-1))

#make list from all the number in equation (steing)
def m_list(e):
    x = e.replace('-','+').replace('*','+').replace('/','+').replace('^','+').replace('a','+').replace('b','+')
    return x.split("+")

#make list from all the action in equation (steing)
def act_list(e):
    a_list = []

    for char in e:
        if char == '+' or char == '-' or char == '/' or char == '*' or char == '^' or char == 'a' or char == 'b':
            a_list.append(char)
    return a_list
  
#compute the equation represented by a string   
def compute_equation(e):
    
    #if input not a number or digit retuen error
    for i in e:
        if (not i.isdigit())and(i not in ['.','+','-','*',"/"]):
            return("invalid input detected")
        
    #replace action to be fix with all function
    if "+-" in e:
        e = e.replace("+-", "-")
    if "*-" in e:
        e = e.replace("*-", "a")
    if "/-" in e:
        e = e.replace("/-", "b")
    if "**" in e:
        e = e.replace("**", "^")
    
    #Split the string equation into 2 lists
    a_l = act_list(e)
    m_l = m_list(e)
    new_clac = 'a'
    
    #fix lists if there is - in start of the equation
    if  m_l[0] == '':
        m_l.pop(0)
        m_l[0] = str(float(m_l[0])*(-1))
        a_l.pop(0)
        
    #Calculating the equation.
    #Computer 2 numbers at each stage according to the multiplication rules
    while a_l != []:
        
        #Calculation of powers
        if '^' in a_l:
            i = 0 
            for act in a_l:
                if act == '^':
                    new_clac = cla(m_l[i], act, m_l[i+1]) #the calculation
                    m_l.pop(i+1) #change the list after the calculation
                    m_l.pop(i)
                    m_l.insert(i,new_clac)
                    a_l.pop(i)
                i = i + 1
        #calculation Multiplication and division
        if '^' not in a_l:
            i = 0   
            for act in a_l:
                if act == 'a' or act == 'b' or act == '*' or act == '/':
                    new_clac = cla(m_l[i], act, m_l[i+1])
                    m_l.pop(i+1)
                    m_l.pop(i)
                    m_l.insert(i,new_clac)
                    a_l.pop(i)
                i = i + 1
            #Calculation addition and subtraction
            
        if '^' not in a_l and 'a' not in a_l and 'b' not in a_l and '*' not in a_l and '/' not in a_l:           
            i = 0   
            for act in a_l:
                if act == "+" or act == "-":                
                    new_clac = cla(m_l[i], act, m_l[i+1])
                    m_l.pop(i+1)
                    m_l.pop(i)
                    m_l.insert(i,new_clac)
                    a_l.pop(i)
                i = i + 1
                
    #Decision type of out put            
    if float(m_l[0])%1 == 0:
        x = m_l[0].replace('.0', '')
        return int(x)
    else:
        return float(m_l[0])



x = ['*', '^']

if '+' not in x and '-' not in x :
    print('in')

