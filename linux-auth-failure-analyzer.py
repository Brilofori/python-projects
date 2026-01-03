logFile = 'Logs/Linux_2k.log'
count = 0
with open(logFile, 'r') as logs:
    for log in logs:
        if 'authentication failure' in log.lower():
            parts = log.split()
            
            

            for rhostValue in parts:
                if rhostValue.startswith("rhost="):
                    ipaddr = rhostValue.split('=')[1]
                    for x in ipaddr:
                        count += 1
                        print({ipaddr:count})
                    
 
                    
                        
                



