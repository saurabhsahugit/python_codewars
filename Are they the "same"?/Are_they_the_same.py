import math

def comp(array1, array2):
    result = []
    
    if array1 is None or array2 is None:
        return False
     
    else:
        for num in array2:
            num = math.sqrt(num)
            
            if num in array1:
                result.append("True")
                array1.remove(num)
            elif (num * -1) in array1:
                result.append("True")
                array1.remove(num * -1)
            
            else:
                result.append("False")
    
    
    if "False" in result:
        return False
    else:
        return True
	