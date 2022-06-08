import os
import re
from ia import train 

current_model = "models/test_model.keras"

print('\n'+8*'='+ ' EP3 - TREINO '+8*'=')

train(current_model)

print(f"Training complete!\n\nNew file {current_model}")
