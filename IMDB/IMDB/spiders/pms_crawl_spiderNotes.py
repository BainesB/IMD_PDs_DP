
# url = 'https://www.imdb.com/title/tt1777610/fullcredits?ref_=tt_ql_1'

# flying monsters page: https://www.imdb.com/title/tt1777610/?ref_=nv_sr_1?ref_=nv_sr_1

# atlantic page: https://www.imdb.com/search/title/?companies=co0146284

# atlatnic full cast and crew: https://www.imdb.com/title/tt1777610/fullcredits?ref_=tt_ql_1


# get the prog title text 

#response.css('.parent a::text').get()



# i think this might be it: 
#####

#credits = response.css('.credit::text').getall()

#crewnames = response.css('.cast_list~ .simpleCreditsTable a::text').getall() 

'''
>>> crewdict= {}
>>> crewdict
{}
>>> count = 2
>>> for i in credits:
...     crewdict[i]=crewnames[count]
...     count+=1
...

'''


