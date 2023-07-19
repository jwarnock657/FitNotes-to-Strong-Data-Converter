import csv

def writeToFile(exercises):
  print("Writing exercises to file...")
  headers = ["Date", "Workout Name", "Exercise Name", "Set Order", "Weight", "Weight Unit", "Reps", "RPE", "Distance", "Distance Unit", "Seconds", "Notes", "Workout Notes", "Workout Duration"]
  f = open("output.csv", "w", newline='')
  writer = csv.writer(f, delimiter=";")

  writer.writerow(headers)
  for exercise in exercises:
    splitExercise = exercise.split(";")
    writer.writerow(splitExercise)

  f.close()

def run() :
  print("Running...")
  convertedExercises = []

  with open('fitnotes.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    i = 0
    exerciseName = ""
    setNum = 1
    for row in spamreader:
      if(i != 0):
        # values are: 
        #   Date,Exercise,Category,Weight,Weight Unit,Reps,Distance,Distance Unit,Time,Comment
        vals = row
        date = str(vals[0]) + " 17:00:00"
        workoutName = 'Workout on ' + str(vals[0])
        currExerciseName =  str(vals[1])
  
        # so we can keep track of the exercise set number
        if exerciseName != currExerciseName:
          exerciseName = currExerciseName
          setNum = 1
        else:
          setNum += 1

        setOrder = str(setNum)
        weight = str(int(float(vals[3]))) if len(vals[3]) > 0 else ''
        weightUnits = str(vals[4]).replace('s', '')
        reps = str(vals[5])
        rpe = ""
        distance = str(vals[6])
        distanceUnit = str(vals[7])
        seconds = "60s" if str(vals[8]) else ""
        notes = vals[9].replace('"', '')

        convertedString = date + ";" + workoutName + ";" + currExerciseName + ";" + setOrder + ";" + weight + ";" + weightUnits + ";" + reps + ";" + rpe + ";" + distance + ";" + distanceUnit + ";" + seconds + ";" + notes + ';;60s'
        
        # for some reason cardio seems to mess up on the import into hevy, have disabled
        if(distanceUnit == ""):
          convertedExercises.append(convertedString)
      
      i += 1 

    writeToFile(convertedExercises)
        
run()