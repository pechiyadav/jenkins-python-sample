import datetime

def greet():
  current_time = datetime.datetime.now()
  print(f"Hello from Jenkins using polling at {current_time}!")

if __name__ == "__main__":
  greet()
