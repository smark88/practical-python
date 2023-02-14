def pax(time,paxlist,pax):
    pax = pax.upper()
    if time is not None and pax in paxlist:
        try:
            output = {}
            output['Pax'] = pax
            output['Multiplier'] =  paxlist[pax]
            output['Time'] =  round(time * paxlist[pax],3)
            return output
        except:
            ValueError
            return 1


current = {
    'SS': 0.833,	 	
    'AS': 0.823,	 	
    'BS': 0.818,	 	
    }
print(pax(69.420,current,'as'))
