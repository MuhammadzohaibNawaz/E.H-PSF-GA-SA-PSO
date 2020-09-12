import random
from random import randint
import math
import time
import psutil

def Fitness(guess,targetProof):
    fitness = 0
   # print("Guess",len(guess))
    for i in range(len(guess)):
        if guess[i] == targetProof[i]:
            if not (str(i)in fixedSlots):
                fixedSlots.append(str(i))
                # print(guess, fixedSlots)
            fitness+=1
 #  print(fitness)
    return fitness
def calculateVelocity (currentFitnessValue, currentVelocity):
    C1=1
    C2=1
    return math.floor(currentVelocity + C1 * random.random() * (pBest - currentFitnessValue) + C2 * random.random() * (gBest - currentFitnessValue))

def multiPositionMutate(randomSequece,positions):
    # print("Length: " , len(fixedSlots))
    #if positions < len(fixedSlots):
      #  positions=len(randomSequece)-len(fixedSlots)
    positions=1
    randNumList = []
    for i in range(0, positions):
        while True:
            rn = randint(0, len(randomSequece)-1)
            if not (str(rn) in randNumList or str(rn) in fixedSlots):
                randNumList.append(str(rn))
              #  print(fixedSlots)
                randomSequece[rn] = random.choice(gSet)
                # print(randomSequece)
                # randomSequece[rn] = str(randint (1,20))
                # ng, alter = random.sample(gSet, 2)  # print("DFGH", nGene, alter) #x = []#while nGene == cGenes[ind]:
                # if ng == randomSequece[rn]:
                #     randomSequece[rn] = alter
                break
velocity=1
nextVelocity=0
positionPSO=1
fixedSlots=[]
ite = []
totalIterations = 0
gBest=0
itertaion=0
totalstartTime=time.time()
startTime = time.time()
ccccc=0
with open("Population.txt", 'r') as f: #tokenize all the words in file guru99 into set 'a','b'
    p = f.read()
    gSet = p.split()

with open("PDE.txt", 'r') as f:
    for line in f: #all the lines in f (proofs.txt)
        startTime = time.time()
        proof = line.split()
        gBest = len(proof)
        # print (proof)
        pBest = 0
        fixedSlots=[]
        itertaion = 0
        randomSequence = []
        randomSequence = random.choices(gSet, k=len(proof))
#        ccccc=ccccc+1
     #   if ccccc % 10 == 0:
      #  print ("more : ", ccccc )
        while pBest < gBest:
            # print("RS: ", randomSequence)
            multiPositionMutate(randomSequence,positionPSO)
            itertaion=itertaion+1
            totalIterations=totalIterations+1
            if totalIterations % 500 == 0:
                print (totalIterations, pBest)
         #   print ("RS: ", randomSequence)
         #   print("TS: ", proof)
            fv=Fitness(randomSequence, proof)
            # print("RS: ", randomSequence)
            # print (fv)
            if pBest < fv:
                ccccc=ccccc+1
             #   if (ccccc<=81):
            #        print (ccccc, " ",time.time()-startTime )
                startTime=time.time()
                pBest = fv
                if pBest == gBest:
                    break
            # nextVelocity= velocity + C1 * random.random() *(pBest - fv)+ C2*random.random()*(gBest-fv)
            positionPSO=calculateVelocity(fv, velocity)
#         print(itertaion)
mem = psutil.virtual_memory()  # .total / (1024.0 ** 2)
# print(itertaion)
print(totalIterations)
print("Total Time:", time.time() - totalstartTime)
print("Memory Used in Mb:", mem.used >> 20)

# velocty ka function
# make other code for removed optimization
# hill climbing
# increase dataset
