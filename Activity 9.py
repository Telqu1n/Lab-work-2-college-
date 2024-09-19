
list = []
def studant_grades():
  
  
  studant_num = 0 
  while studant_num < 10:
    grades = int(input("Enter your grades: "))
    list.append(grades)
    studant_num += 1
    
  print ("The grades are: ", list)

studant_grades()

