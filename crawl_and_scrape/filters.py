# I part of my code I'm looking for 'production manager' 

# I want to filter out 'post-production managers' 

# I do not want to exclude things like 'production manager (3 episodes)

naughty_list = ['post-production manager','wackawacka']

def PM_filter(String):
    string = String
    #print('PM_filter: the string is:', string)
    if 'production manager' in string and string not in naughty_list:
        #print('This is the string:', string)
        return 'production manager'
    else:
        pass
        #print('PM_filter: string does not contain production_manager')

'''
thing = PM_filter('production manager')
thing1 = PM_filter('post-production manager')
print(thing, thing)
'''
