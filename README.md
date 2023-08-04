# Bachelorarbeit_RASA
Learning ChatBot for Bachelor Thesis 

This Chatbot can be used to learn a certain set of slides. 

## Installing RASA
First off, RASA Open Source has to be installed locally. A deployment has not been implemented yet. 

```shell
pip3 install rasa
```

Then, one has to open two terminals in the related directory. 

In the first shell, type the following command to train the model. This has to be initally.

```shell
rasa train
```
After the trainings has been completed, start the rasa chatbot via the following command:
```shell
rasa run 
```

In the second shell, type the following command to start up the action server for custom actions (required!)

```shell
rasa run actions
```

## Startin the Application
Then you are good to go - run the application *ChatbotInterface.py via double click - a shell will open to communicate with the chatbot. Have fun! 

