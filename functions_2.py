import string
import random



def remove_punctuation(input_string):
    """
     remove the punctuation of input
    
     Parameters
     ----------
     input_string : string
        
        
     Returns
     -------
     output_string : string
     string without punctuation
   
     ###from assignment encoder
    """ 
    out_string= ''
    
    for item in input_string:
        if item not in string.punctuation:
            out_string= out_string+item
            
            
    return out_string


def prepare_text(input_string):
    """
    lower the input 
    Parameters
    ----------
    input_string : string
    turn capital letter into lower letter
        
    Returns
    -------
    output_string : string with lower letter
    ###from assignment chatbot  
    """ 
    temp_string=input_string.lower()
    temp_string=remove_punctuation(temp_string)
    out_list=list(temp_string)
    
    
    return(out_list)


def decoder(input_string):
    """ decode the input into numbers
    Parameters
    ----------
    input_string : string
        String to convert to code points
        
    Returns
    -------
    output_string : numbers into list
    
    """
    output =[]
    temp = input_string
    
    for i in range(len(temp)):
        output.append( ord(temp[i]))
        
    return output


