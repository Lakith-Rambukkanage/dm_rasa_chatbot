# Sinhala Ecommerce Rasa-chatbot
 Simple Clothing Ecommerce Chatbot with Rasa Framework 

## steps to setup
1. `C:\> python3 -m venv ./venv`
2. `C:\> .\venv\Scripts\activate`
3. `pip3 install -U --user pip && pip3 install rasa`
4. `rasa train`
5. `rasa run actions` (in a seperate terminal)
6. `rasa run --credentials ./credentials.yml  --enable-api --auth-token XYZ123 --model ./models --endpoints ./endpoints.yml --cors "*"`

## Rasa Docs
* documentation [documentations](https://rasa.com/docs/)
## UI
* refer : [scalableminds](https://github.com/scalableminds/chatroom)
