# Rasa-Chatbot
Simple Chatbot using Rasa framework. Inprogress.

### Installations
- Create a virtual environment 
- rasa==1.9.4 `pip install rasa`

### Training

```python
rasa train
```

### To run the bot

```python
rasa shell
```

### Overview of the files 

`data/nlu.md` - contains NLU training data

`data/core.md` - contains stories 

`domain.yml` - the domain file, including bot response templates

`config.yml` - training configurations for the NLU pipeline and policy ensemble

`actions` - directory containing custom action code. This is run as a python module i.e. `actions.actions`

### References
- https://rasa.com/

