__author__ = 'grack'
test="test string that is what im searching for"
import random
pop_size=100
fitness_arr=[]
population=[]
father_index=0
mother_index=0
found_index=0
def randstring(length=10):
    valid_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()?><~'
    return ''.join((random.choice(valid_letters) for i in xrange(length)))
def init():
    global population
    for i in range (0,pop_size):
        population.append(randstring(len(test)))
def fitness(str):
    f=0
    for i in range (0,len(test)):
        if test[i]==str[i]:
            f=f+1
    return f
def calc_fitness():
    global fitness_arr
    fitness_arr=[]
    for i in range (0,pop_size):
        fitness_arr.append(fitness(population[i]))
def find_max_index():
    max_index=0
    for i in range(0,pop_size):
        if fitness_arr[i]>fitness_arr[max_index]:
            max_index=i
    return max_index
def find_second_max_index():
    global fitness_arr
    max_index=find_max_index()
    second_max_index=0
    for i in range (0,pop_size):
        if(fitness_arr[i]>fitness_arr[second_max_index] and i!=max_index):
            second_max_index=i
    return second_max_index
def selection():
    global mother_index
    mother_index=find_max_index()
    global father_index
    father_index=find_second_max_index()
    if mother_index==father_index:
        father_index=father_index+1
def crossover():
    new_child=[]
    rnd_num=random.randrange(1,len(test))
    # print "rnd_num : ",rnd_num
    print "mother index : ",mother_index," father index : ",father_index,"\n"
    #rnd_num=int(len(test)/2)
    for i in range(0,rnd_num+1):
        new_child.append(population[mother_index][i])
    for j in range(rnd_num+1,len(test)):
        new_child.append(population[father_index][j])
    child=''.join(new_child)
    return child
def mutation(child):
    global population
    population=[]
    print "child : ",child,"\n"
    population.append(child)
    for i in range(1,pop_size):
        str_item=child
        rnd_mutate_place=random.randrange(0,len(test))
        str_list=list(str_item)
        str_list[rnd_mutate_place]=randstring(1)
        str_item=''.join(str_list)
        # for j in range(0,len(test)):
        #     c=randstring(1)
        #
        #     item.append(c)
        #str_item=''.join(item)
        population.append(str_item)
def found():
    global found_index
    if(len(test) in fitness_arr):
        found_index=fitness_arr.index(len(test))
        return True
    return False
def genetic_alg():
    t=0
    while(not(found())):
        selection()
        child=crossover()
        mutation(child)
        calc_fitness()
        t=t+1
        print "generation ",t
        print population
        print fitness_arr
init()
calc_fitness()
print population
print fitness_arr
genetic_alg()
print "found solution at index : ",found_index
print len(test)
print 77**41
st=((77**41)/((10**15)*93))
st=st/60
st=st/60
st=st/24
st=st/365
print st