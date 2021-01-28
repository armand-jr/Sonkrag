# Sonkrag  
## Background information  
Three dummy-districts want to catch the excess of energy that are produced by solar panels on the houses within that district. The batteries that catch this excessive energy have a limited amount they can contain. Therefore, the houses in each district have to be divided among the batteries so as much energy as possible can be saved for the smallest cost possible. The houses are connected to the batteries through cables. The length of the cables should therefore be minimized to minimize cost.  

## Algorithm information
### Random
1. Give every house a random battery
2. Switch houses until the max capaciteit is not exceeded

### Greedy
1. Give every house the closest battery
2. Switch houses until the max capaciteit is not exceeded
3. Switch houses, if total cost improves keep switch

### Hillclimber
1. Make startsolution with random algorithm
2. Loop n times x iterations
   1. Switch 2 random houses
   2. If total cost improves keep changes else reverse changes
   3. After i times no improvements stop and start new iterations loop

### Hillclimbergreedy
1. Make startsolution with greedy algorithm
2. Loop n times x iterations
   1. Switch 2 random houses
   2. If total cost improves keep changes else reverse changes
   3. After i times no improvements stop and start new iterations loop

### Genetic
1. Make n random different start solutions
2. Loop until no improvements where found n times in a row
   1. Sort population in half best and half worst values
   2. Make 60% of population parents, 2/3 of parents form best, 1/3 from worst
   3. Make pares of parents and make two children
      1. if houses have the same battery keep the battery
	  2. if battery is different change 20% to random or closest battery, 80% keeps the battery of parent1

### Genetic_Pop_HC
1. Make n random different start solutions
2. Loop until no improvements where found n times in a row
   1. Improve the population with hillclimber algorithm
   2. Sort population in half best and half worst values
   3. Make 60% of population parents, 2/3 of parents form best, 1/3 from worst
   4. Make pares of parents and make two children
      1. if houses have the same battery keep the battery
	  2. if battery is different change 20% to random or closest battery, 80% keeps the battery of parent1

### Genetichillclimber
1. Make startsolution with genetic algorithm
2. Loop n times x iterations
   1. Switch 2 random houses
   2. If total cost improves keep changes else reverse changes
   3. After i times no improvements stop and start new iterations loop


## What do we need?
### Used Packages  
All coding has been written in Python 3.7. We made use of the following packages:  
-	Pip  
-	Matplotlib  
-	Random  
- 	Copy  

### Use  
To run the written program type in:  
‘python main.py [algorithm] [district number] [basis/advanced5]’  
#### Algorithms:
* random
* greedy
* hillclimber
* hillclimbergreedy
* genetic
* genetic_pop_hc
* genetichillclimber  
#### District number:
* 1
* 2
* 3  

### Additional data info
In district-1_batteries.csv, district-2_batteries.csv and district-3_batteries.csv change coordinates from example "30,14" to 30,14

### Outline  
To sum up the outline of the most important folders and files, see the following list:  
*   /code: here you will find all code
	* /code/algorithms: here you will find all code to 
	* /code/classes: here you will find all the classes that will construct the data 
	* /code/visualization: here you will find the code that will visualize the outcome in a grid
*   /data: here you will find all datafiles that serve as input sources to solve the above mentioned problem with the use of the created algorithms  

# Authors  
*   Armand Stiens  
*   Dionne Ruigrok  
*   Willem Folkers  

This README file was inspired by the [RadioRussia case written by the assistants of the minor programming at UvA](https://github.com/Qvdpost/RadioRussia/tree/3c6633eab040a30cfd80f27dcb9f237a0bb08227).  


![UML](docs/images/DESIGN.png)  

