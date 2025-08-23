def convert(number):
    if number%3 == 0:
        var = "Pling"
        
        if number%5 == 0:
            var = var + "Plang"
            
            if number%7 == 0:
                var = var + "Plong"
                
        elif number%7 == 0:
            var = var + "Plong"
                
    elif number%5 == 0:
        var = "Plang"
        
        if number%7 ==0:
            var = var + "Plong"
            
    elif number%7 == 0:
        var = "Plong"

    else:
        return str(number)
        
    return var