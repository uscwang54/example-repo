from datetime import datetime
import pandas as pd

times = []
user_inputs = []

while True:
    user_input = input("Enter event you want to recored: ")
    user_inputs.append(user_input)
    if user_input!='q':
        times.append(datetime.now().time().strftime('%H:%M:%S'))
        continue
    elif user_input=='q': #enter q to quit
        break

df = pd.DataFrame(columns=["Event","Time"])
for i in range(len(times)):
    df.loc[i] = [user_inputs[i], times[i]]
