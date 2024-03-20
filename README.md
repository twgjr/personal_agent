# Local LLM Personal Agent

This is a personal project inspired by my sons love of a certain Disney trash collecting robot (furthermore named "trash robot").

## Goals
1. Run without internet access.  Local models only.
2. Run on a Raspberry Pi 5 or similar low power device.
3. Act like the trash robot.  Limited vocabulary, but can take actions based on spoken input.
4. Minimize the need for training models by using pre-trained models and prompt engineering.

## How to Implement
All models should be able to fit onto one Raspberry Pi 5 with 8GB of RAM.

1. Agent (Actions):  Use the LangChain and Ollama libraries to pull and run local language models.  The language model will be set up as an agent that can take a set of predefined actions based on the input.  Examples of actions are "find the plant".
3. Speech:  Use the local speech recognition library to convert spoken input to text.  The text will be sent to the agent for processing.
2. Vision:  Use Yolo to quickly identify objects in a video feed.  The video feed will be from a camera on the Raspberry Pi.  The video feed will be processed by the Yolo model and the results will be sent to the agent for processing.
3. Planning and Navigation:  Use the same agent but with different prompts in a chain to plan and navigate to a location.  The agent will be able to take a set of predefined actions to navigate to a location.  Examples of actions are "go to the kitchen".  May need to learn a map of its surroundings (much later)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Raspberry Pi 5 or similar low power device (could also be run on a laptop or desktop computer in a linux environment)
- Python 3.10 or higher
- pip package manager

### Installation

1. Setup a virtual environment such as venv.  

2. Install packages as needed for the various language model examples.

3. Install Ollama using their installation script and curl command.


## Usage

Currently the language models are set up to chat with younger children in mind.

To use the LLM Personal Agent, run the model script and follow the prompts to ask questions.

```bash
python agent.py <model_name>
```

If the model has never been downloaded before, it will pull it from Ollama.  This takes several minutes.  Then it will run the model. Suggested first model is ```gemma:2b```.

It will prompt for the user to provide an text prompt.  The agent will respond like a chatbot in the terminal.

Type "exit" to exit the chatbot.