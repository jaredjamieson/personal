# Jared Jamieson
# October 29, 2019
# CS/IT 200
# Lab 8
# cpu_simulation


# Imports
import random, priority_queue, csv

def main():
    """ User inputs and variables """
    user_format = input('Enter simulation format, (F)ile or (R)andom: ')
    user_cpu_num = int(input('Enter number of CPUs: '))
    
    jobs_completed = 0                                                        # Prime job counter
    tick = 1                                                                  # Prime tick counter
    
    # Heap Class Object
    my_queue = priority_queue.HeapPriorityQueue()
    
    sim_format(user_format, my_queue, jobs_completed, tick, user_cpu_num)     # Calls simulator

def response(answer):
        """ Returns the users response simplified"""
        if answer in ['YES', 'Yes', 'y', 'Y', 'yes']:
            return 'yes'
        elif answer in ['NO', 'no', 'N', 'n', 'No']:
            return 'no'
        elif answer in ['f', 'F', 'file', 'File']:
            return 'F'
        elif answer in ['r', 'R', 'random', 'Random']:
            return 'R'
        else:
            raise ValueError('Invalid response')
            

def build_schedule(total_cpu, tick):
    """ Builds the cpu format """
    temp_jobs = []
    c = ','
    for cpu in total_cpu:
        my_cpu = str(cpu[0][0])
        temp_jobs.append(my_cpu)
    c = c.join(temp_jobs)
        
    return('%d: %s' % (tick, c))


def make_cpu(user_cpu_num, job_name = '-', job_length = 0, jobs_completed = 0):
    """ Make CPUs per input """
    total_cpu = []
    for i in range(user_cpu_num):
        total_cpu.append([[job_name, job_length],jobs_completed])      # Make list of 'i' cpu's
    return total_cpu


def sim_format(user_format, my_queue, jobs_completed, tick, user_cpu_num):
    """ Random Simulation Format """
    if response(user_format) == 'R':
        user_yes = input('Do you want to use a random seed? ')
        if response(user_yes) == 'yes':
            randomizer = random.Random(int(input('Enter a seed: ')))
        else:
            randomizer = random.Random()
        probability = float(input('Enter the probaility that a new job is created each time-slice (0-1): '))
        sim_length = int(input('Enter length of simulation: '))
        
        total_cpu = make_cpu(user_cpu_num)
        queue_jobs = 1
        for i in range(sim_length):
            rand_num = randomizer.random()
            if rand_num < probability:              # Add probable additions to queue
                length = randomizer.randint(1 ,100)
                priority = randomizer.randint(-19, 20)
                my_queue.add(priority, [str(queue_jobs), length])
                queue_jobs += 1
            for cpu in total_cpu:
                if cpu[0][1] > 0:                   # If length, decrement
                    cpu[0][1] -= 1
                if cpu[0][1] == 0 and cpu[0][0] != '-':
                    cpu[0][0] = '-'                 # Change job name back to '-'
                    cpu[1] += 1                     # Increment jobs completed

                if cpu[0][0] == '-' and len(my_queue) != 0:
                    key, value = my_queue.remove_min()
                    cpu[0] = value                   # Save new job name and length

            print(build_schedule(total_cpu, tick))
            tick += 1
            
        total_completed = 0
        for cpu in total_cpu:
            total_completed += cpu[1]
        print('Total number of jobs completed: %d' % total_completed)

    """ File Simulation Format """
    if response(user_format) == 'F':
        user_file = 'file-input.csv' #input('Enter filename: ')
        total_cpu = make_cpu(user_cpu_num)
        with open(user_file, newline = '') as myfile:               # Open and reads csv file
            infile = csv.reader(myfile, delimiter = ',')
        
            for line in infile:
                if line[0] != 'No job':                             # Add [Name, Length] and priority to queue
                    my_queue.add(int(line[2]), [line[0], int(line[1])])       # If job exists, add
                for cpu in total_cpu:
                    if cpu[0][1] > 0:                   # If length, decrement
                        cpu[0][1] -= 1
                    if cpu[0][1] == 0 and cpu[0][0] != '-':
                        cpu[0][0] = '-'                 # Change job name back to '-'
                        cpu[1] += 1                     # Increment jobs completed

                    if cpu[0][0] == '-' and len(my_queue) != 0:
                        key, value = my_queue.remove_min()
                        cpu[0] = value                   # Save new job name and length

                print(build_schedule(total_cpu, tick))
                tick += 1
            
            total_completed = 0
            for cpu in total_cpu:
                total_completed += cpu[1]
            print('Total number of jobs completed: %d' % total_completed)
  

main()