

def calculate_distance(speed, time):
  return speed * time

def main():
  speed = 55  
  total_time = 4  
  interval = 0.5  

  print("Time (hours) | Distance (miles)")
  print("-----------------------------")
  
  current_time = 0
  while current_time <= total_time:
    distance = calculate_distance(speed, current_time)
    print(f"{current_time:.1f}          | {distance:.1f}")
    current_time += interval

if __name__ == "__main__":
  main()