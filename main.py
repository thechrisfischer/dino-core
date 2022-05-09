# /usr/bin/env python

# First we need to load a file of worksouts
# Second we need to get input from the user about how long they want to Workout
# Third convert time user wants to workout into seconds
# 4. we want to pick some random workouts to fill the time
import random
import pyttsx3
import time
from num2words import num2words


def load_workouts():
    # set the path of the file_handle
    path = 'workouts.txt'
    # create a file handle readonly to access data
    file_handle = open(path, 'r')
    # read all contents into the workouts variable
    workouts = file_handle.readlines()
    # print out the workouts we have to choose from

    # define a blank array
    workouts_array = []
    # read each line into the workouts_array
    for line in workouts:
        workouts_array.append(line.strip())

    return workouts_array


def get_rand_workouts(workout_list, time):
    # TODO need to pop elements off the list to make sure we dont
    # have the same choice twice when making random choices
    workout_time_array = []
    num_workouts = time * 2
    workouts = []
    count = num_workouts
    while count > 0:
        w = random.choice(workout_list)
        workouts.append(w)
        workout_list.remove(w)
        count = count - 1
    for w in workouts:
        w_arr = [w, 30]
        workout_time_array.append(w_arr)
    return workout_time_array


def speak_workouts(workout_list):
    engine = pyttsx3.init()
    while workout_list:
        workout = workout_list.pop()
        print(workout)
        engine.say(workout[0] + " for " + num2words(workout[1]) + " seconds")
        engine.runAndWait()
        time.sleep(workout[1] / 10)


def main():
    workout_list = load_workouts()
    speak_workouts(get_rand_workouts(workout_list, 5))


if __name__ == '__main__':
    main()
