def show_city(city,country,population=''):
    if population:
     infor = city+","+country+"-"+"population"+" "+population
    else:
     infor=city+","+country
    return infor

