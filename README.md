# Sinhala Ecommerce Rasa-chatbot
 Simple Clothing Ecommerce Chatbot with Rasa Framework 

## steps to setup
1. >`C:\> python3 -m venv ./venv`
2. >`C:\> .\venv\Scripts\activate`
3. >`pip3 install -U --user pip && pip3 install rasa`
4. >`rasa train`
5. >`rasa run actions` (in a seperate terminal)
6. >`rasa run --credentials ./credentials.yml  --enable-api --auth-token XYZ123 --model ./models --endpoints ./endpoints.yml --cors "*"`
7. > open `index.html` locally on browser
## Functionality
1. query products with 
    * product category - පිරිමි, කාන්තා, ළමා, උපාංග
    * product name - කලිසම, කමිසය, බ්ලවුස්, ගවුම, සපත්තු, මේස්, බඳ පටිය
    * size - කුඩා, මධ්‍යම, විශාල
    * material - සේද, කපු, සම්, කැන්වස් 
    * brand - ලුයිස්, අඩිඩාස්, නයික්, කිටී, ප්රාඩා
    * colour - කළු, සුදු, නිල්, දුඹුරු
2. add items to cart
3. clear cart
4. ask for payment info
5. ask for delivery info
6. check if you are talking to a bot
7. request redirect to actual customer service agent

> **For examples refer [example_queries.txt](example_queries.txt)**

---

## Rasa Docs
* [documentation](https://rasa.com/docs/)

---
## UI
This repo uses the *scalableminds UI*. Alternatively *Rasa-X* can be used 
* refer : [scalableminds](https://github.com/scalableminds/chatroom)
