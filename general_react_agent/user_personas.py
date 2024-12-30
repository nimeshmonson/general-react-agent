class UserPersona:
    def __init__(self, description, client):
        self._description = description 
        self.messages = [{
            "role": "system",
            "content": self._description
        }]
        self.client = client
    
    def save_answer(self, answer):
        message = {"role": "assistant", "content": answer}
        self.messages.append(message)

    def ask_user_question(self, question, context=None):
        message = {"role": "user", "content": question}
        self.messages.append(message)
        
        print("Asked User a Question: {}".format(question))

        answer = self.client.send_message(message=self.messages).choices[0].message.content
        self.messages.append({"role": "assistant", "content": answer})

        print("User Responded: {}".format(answer))

        return answer