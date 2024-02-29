def convert():
    seconds = ""
    while not seconds.isdigit():
        seconds = input('Amount of seconds: ')
    
    time: list = [float(seconds)]
    output = [ ('Seconds', 60), ('Minutes', 60), ('Hours', 24) , ('Days', 365), ('Years', 100), ('Century', 1000)]
    
    s, a = "", 
    
    for i in range(len(output)):
        if time[i] <= int(output[i][1]) - 1:
            if not time[i].is_integer():
                for index in range(len(time)):
                    if index < (len(time) - 1):
                        if index != 0:
                            a = ", " + s
                        s = f"{int((time[index+1] % 1) * int(output[index][1]))} {output[index][0]}" + a      
                    else:
                        s = f"{int(time[index])} {output[index][0]}, " + s
                        
                print(s)
            else:
                print(f'{int(time[i])} {output[i][0]}')
            break
        else:
            time.append(time[i]/int(output[i][1]))
    
convert()