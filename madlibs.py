from random import choice

def list_append(my_list:list,quantity:int,component:str):
    '''form a list with elements collected from speech components'''
    my_list.append(input(f'input {component}-->'))
    for i in range(quantity-1):
        my_list.append(input(f'input {component} again-->'))
    return None

def my_choice(mylist:list):
    '''randomly ((if its not a list with one element)) selects an element from the list,
      returns this element and removes it from the list'''
    if len(mylist)!=1:
        n=choice(mylist)
        mylist.remove(n)
        return n
    else:
        return mylist[0]

print('Now we will play Mad Libs')
print('We have three stories\n1:Story about hospital\n2:Story about camping\n3:Story about correspondence')
number_choice = input('Please input one of the story numbers-->')

if number_choice=='1':
    number=[]
    adjective=[]
    noun=[]
    measure_of_time=[]
    mode_of_Transportation=[]
    color=[]
    part_of_the_body=[]
    verb=[]
    silly_Word=[]
    list_append(number,2,'number')
    list_append(adjective,3,'adjective')
    list_append(noun,5,'noun') 
    list_append(measure_of_time,1,'measure_of_time')
    list_append(mode_of_Transportation,1,'mode_of_Transportation')
    list_append(color,1,'color')
    list_append(part_of_the_body,1,'part_of_the_Body')
    list_append(verb,2,'verb')
    list_append(silly_Word,1,'silly_Word')

    story1=f'''It was about {my_choice(number)} {my_choice(measure_of_time)} ago when I arrived at the
    hospital in a {my_choice(mode_of_Transportation)}. The hospital is
    a/an {my_choice(adjective)} place, there are a lot of {my_choice(adjective)} {my_choice(noun)} here.
    There are nurses here who have {my_choice(color)} {my_choice(part_of_the_body)}. If someone
    wants to come into my room I told them that they have to {my_choice(verb)} first.
    I`ve decorated my room with {my_choice(number)} {my_choice(noun)}. Today I talked to a
    doctor and they were wearing a {my_choice(noun)} on their {my_choice(part_of_the_body)}.
    I heard that all doctors {my_choice(verb)} {my_choice(noun)} every day for breakfast. The
    most {my_choice(adjective)} thing about being in the hospital is the {my_choice(silly_Word)} {my_choice(noun)}!'''
    print(story1)

elif number_choice == '2':
    number=[]
    adjective_feeling=[]
    noun=[]
    measure_of_time=[]
    proper_noun=[]
    color=[]
    animal=[]
    verb=[]
    silly_Word=[]
    persons_name=[]
    adverb_ending_in_ly=[]
    verb_ending_in_ing=[]
    list_append(number,2,'number')
    list_append(adjective_feeling,2,'adjective_feeling')
    list_append(noun,2,'noun') 
    list_append(measure_of_time,1,'measure_of_time')
    list_append(proper_noun,1,'proper_noun')
    list_append(color,1,'color')
    list_append(animal,2,'animal')
    list_append(verb,2,'verb')
    list_append(silly_Word,1,'silly_Word')
    list_append(persons_name,1,'persons_name')
    list_append(verb_ending_in_ing,1,'verb_ending_in_ing')
    list_append(adverb_ending_in_ly,1,'adverb_ending_in_ly')

    story2=f'''This weekend I am going camping with{my_choice(proper_noun)} {my_choice(persons_name)}.
    I packed my lantern, sleeping bag, and{my_choice(noun)}.I am
    so {my_choice(adjective_feeling)} to {my_choice(verb)} in a tent. I am {my_choice(adjective_feeling)}
    we might see a(n) {my_choice(animal)}, I hear they`re kind of dangerous. While
    we`re camping, we are going to hike, fish, and {my_choice(verb)}. I have heard
    that the{my_choice(color)} lake is great for {my_choice(verb_ending_in_ing)}. Then we
    will {my_choice(adverb_ending_in_ly)} hike through the forest for {my_choice(number)}
    {my_choice(measure_of_time)}. If I see a {my_choice(color)} {my_choice(animal)} while hiking, I am going
    to bring it home as a pet! At night we will tell {my_choice(number)} {my_choice(silly_Word)}
    stories and roast {my_choice(noun)} around the campfire!!'''
    print(story2)

elif number_choice=='3': 
    number=[]
    adjective=[]
    noun=[]
    noun_plural=[]
    magical_creature_plural=[]
    color=[]
    proper_noun_persons_name=[]
    verb_ending_in_ing=[]
    room_in_a_house=[]
    animal=[]
    place=[]
    measure_of_time=[]
    list_append(place,1,'place')
    list_append(animal,1,'animal')
    list_append(number,1,'number')
    list_append(adjective,5,'adjective')
    list_append(noun,2,'noun') 
    list_append(noun_plural,2,'noun_plural')
    list_append(magical_creature_plural,2,'magical_creature_plural')
    list_append(color,1,'color')
    list_append(proper_noun_persons_name,1,'proper_noun_persons_name')
    list_append(verb_ending_in_ing,2,'verb_ending_in_ing')
    list_append(room_in_a_house,1,'room_in_a_house')
    list_append(measure_of_time,1,'measure_of_time')
    

    story3=f'''Dear {my_choice(proper_noun_persons_name)}, I am writing to you from
    a {my_choice(adjective)} castle in an enchanted forest. I found myself here one
    day after going for a ride on a {my_choice(color)} {my_choice(animal)} in {my_choice(place)}. There
    are {my_choice(adjective)} {my_choice(magical_creature_plural)} and {my_choice(adjective)} {my_choice(magical_creature_plural)}
    here! In the {my_choice(room_in_a_house)} there is a pool full
    of {my_choice(noun)}. I fall asleep each night on a{my_choice(noun)} of {my_choice(noun_plural)} and
    dream of {my_choice(adjective)} {my_choice(noun_plural)}. It feels as though I have lived
    here for {my_choice(number)} {my_choice(measure_of_time)}. I hope one day you can visit,
    although the only way to get here now is {my_choice(verb_ending_in_ing)} on a {my_choice(adjective)} {my_choice(noun)}!!'''
    print(story3)
