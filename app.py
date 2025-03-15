import datetime

def greet():
  current_time = datetime.datetime.now()
  print(f"Hello from modified Jenkins at {current_time}!")

if __name__ == "__main__":
  greet()
