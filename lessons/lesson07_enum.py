## enum exercise

from enum import Enum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

color = Color.RED
print(color)
print(color.name)
print(color.value)

#Comparing Enums
if color == Color.RED:
    print("The color is red.")
elif color == Color.GREEN:
    print("The color is green.")
elif color == Color.BLUE:
    print("The color is blue.")

# Iterating Over Enums

for item in Color:
    print(item)

for item in Color:
    print(item.name, item.value)

#auto()  - auto() assigns sequential integer values automatically.

class AutoEnum(Enum):
    PENDING =auto()
    RUNNING = auto()
    COMPLETED = auto()

print(AutoEnum.PENDING.value)
print(AutoEnum.RUNNING.value)
print(AutoEnum.COMPLETED.value)

# StrEnum - Unlike a regular Enum, StrEnum behaves like a string, 
# which is often convenient when interacting with APIs.   

from enum import StrEnum

class Modelprovider(StrEnum):
    GROQ = "groq"
    OPENAI = "openai"
    OLLAMA = "ollama"

print(Modelprovider.GROQ.value) 
print(Modelprovider.OPENAI)   

def connect_to_model(provider: Modelprovider):
    if provider == Modelprovider.GROQ:
        print("Connecting to GROQ model...")
    elif provider == Modelprovider.OPENAI:
        print("Connecting to OpenAI model...")
    elif provider == Modelprovider.OLLAMA:
        print("Connecting to Ollama model...")
    else:
        print("Unknown model provider.")

connect_to_model(Modelprovider.GROQ)        


###############  Enum + Dataclass Here's a pattern you'll use in production code ######

from dataclasses import dataclass
from enum import StrEnum

class ModelProvider(StrEnum):
    GROQ = "groq"
    OPENAI = "openai"
    OLLAMA = "ollama"

@dataclass
class ModelConfig:
    provider:ModelProvider
    ModelName:str
    temperature:float=0.7

config1 =ModelConfig(provider=ModelProvider.OLLAMA, ModelName="GPT-4.1", temperature=1.0)
print(config1) # This combines structured data (dataclass) with controlled values (Enum).        
