

import random
import statistics
import time
import gc
import math

import psutil
#import numpy

def acceptance_probability(temperature):
    return math.exp(temperature/(1+temperature))

def Fitness(guess):
    fitness = 0
  #  print (len(guess),len(proof))
 #   if (len(proof)==0):
     #   print ("Hello")
    for i in range(len(guess)):
        if proof[i] == guess[i]:
            fitness+=1
    return fitness

def Results(guess, timings):
    timeD = time.time() - sTime
    fit = Fitness(guess)
#    print(guess, fit, timeD)
    timings.append(timeD)

def get_neighbor(parent):
    index = random.randrange(0, len(parent))
    # turn the parent characters into a list
    childChars = list(parent)
    # pick 2 random characters from the possible set of genes
    newChar, alternate = random.sample(gSet, 2)
  #  print (gSet)
    # replace the index character with one of the randomly found genes
    childChars[index] = alternate if newChar == childChars[index] else newChar
    #chars = ''.join(childChars)
    # get the fitness of the newly generated character set
    #fitness = Fitness(childChars)
    #return Guess(chars, fitness)

    #print(childChars)
    return (childChars)

 #best = sa.anneal(fnGetFitness, len(target), optimalFitness,
  #                 self.charset, fnDisplay, 100000.0, 0.00001, 0.99 )

def anneal(parent, temperature, min_temp, alpha):
    geneTime = time.time()
    cc=0
    arcount=0
  #  print (alpha)

    #make the random initial guess
   # bestGuess = generate_guess(targetLen, charSet, get_fitness)
    #display(bestGuess)
    best_fitness = Fitness(parent)
    #If best_fitn guess is already perfect then no need to go on with the search!
    if best_fitness >= optimalFitness:
   #     print ("AR Count: ", arcount)
   #     print("AR Count: ", arcount)
        return cc, parent #best_fitness#Guess
    #Set the temperatures
    T = temperature
    T_min = min_temp
    #until the temperature reaches the minimum, search!
    while T > T_min:
        cc = cc+1
        new_solution = get_neighbor(parent)
        new_fitness = Fitness(new_solution)
 #       print ("NNS: ", new_solution)
   #     print ("FFNS: ", new_fitness)
       # x=input()
        #If the generated neighbor is already good, return it.
        if new_fitness == optimalFitness:
       #     print ("AR Count: ",arcount)
  #          print("AR Count: ", arcount)

            return cc, new_solution
        #If the generated neighbor is better, move on to it.
        if new_fitness > best_fitness:
            #bestGuess = new_solution #BCBCBCBC
            parent = new_solution #BCBCBCBC
            best_fitness = new_fitness
 #           print(time.time() - geneTime, end=',')
            geneTime = time.time()

        else:
            ar = acceptance_probability(T)
            #let the acceptance rate recommend whether to switch to the worse or not.
            if ar > random.uniform(2.71825400004040,6.71825464604849): #bad one
     #       if ar > random.uniform(2.71820060604849, 2.71825464604849):
                parent = new_solution
                best_fitness = new_fitness
                arcount = arcount + 1
        #the temperature decreases
        T = T*alpha
     #   print("BG11:", bestGuess)
#        #display(bestGuess)
 #   print("BG:", bestGuess)
 #   print("BG:", bestGuess)
#    print("AR Count: ", arcount)
    return cc, parent
#pid = psutil.Process(os.getpgid())
#print(pid.memory_info().rss)# str(os.getpgid())
#status = os.system('cat /proc' +pid + 'status')
#print(status)
random.seed()
#pst = time.time()
timee = time.process_time()
fits = []
lastt = []
count=0
totalCount=0
ite = []
totalstartTime = time.time()
with open("PDExp.txt", 'r') as f: #tokenize all the words in file guru99 into set 'a','b'
    p = f.read()
    gSet = p.split()
    #print(gSet)

with open("Population.txt", 'r') as f:
    for line in f: #all the lines in f (proofs.txt)
        timee += timee
        timings = []
        for i in range(1):
            startTime = time.time()
            proof = line.split() #tokenize each word within a line
            length = len(proof)
            #length of that word in line
            optimalFitness = len(proof)
           # print("OS:", proof)
            #print("OSL:", len(proof))
            g1 = [] #to save first generation randomely from Parent generation
            #g2 = [] #to save second generation randomely from Parent generation

            while len(g1) < len(proof):
                sSize = min(length - len(g1), len(gSet))
                g1.extend(random.sample(gSet, sSize))
                #g2.extend(random.sample(gSet, sSize))
                randSample = list(g1)
                #i2 = list(g2)
#                print("RS:", randSample)
                #print("OSL:", len(i1))
                # print(Fitness(g1))
                randSampleFit= Fitness(randSample)
 #           print("FRS:", randSampleFit)

           # print("SRS:", len(randSample))
            T_max = 100000.0
            T_min = 0.00001
            alpha = 0.99954001
#            alpha = 0.9992
            count=0
            count, randSample=anneal(randSample, T_max, T_min, alpha)
            totalCount = totalCount+count
            if totalCount % 5000 == 0:
                print (totalCount, randSampleFit)
#            print (count, end=',')

        #    print(time.time() - startTime)

#            print("NS:", randSample)
            #print("FNS:", neighborSampleFit)

                #print("SNS:", len(neighborSample))

                #  best = anneal(g1, 100000.0, 0.00001, 0.09 )

#                child = mutate(bParent)
#                cFitness = Fitness(child)

print("Total Time:", time.time() - totalstartTime)
print("Total Count", totalCount)
mem = psutil.virtual_memory()  # .total / (1024.0 ** 2)
print("Memory Used in Mb:", mem.used >> 20)
