tech_name = 'power Bi'


print ('1 current_tech tech name = ' ,tech_name)
def current_tech():
    global tech_name
    print('2 current_tech_name = ', tech_name)

    tech_name = 'python'
    print('3 current_tech_name = ', tech_name)

current_tech()
print('4 current_tech_name = ', tech_name)
