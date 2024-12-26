class UserPersona:
    def __init__(self, description):
        self._description = description 
        self.messages = [{
            "role": "system",
            "content": self._description
        }]
    
    def save_answer(self, answer):
        message = {"role": "assistant", "content": answer}
        self.messages.append(message)

    def ask_question(self, question, client, context=None):
        message = {"role": "user", "content": question}
        self.messages.append(message)

        return client.send_message(message=self.messages)

        


#highschool_completion = highschool_student_client.chat.completions.create(
    #messages=[
        #{
            #"role": "system",
            #"content": "You are a 16-year-old high school student who is excited about music and social media.",
        #},
        #{
            #"role": "user",
            #"content": "how do you like to spend your free time?",
        #}
    #],
    #model="gpt-4o",
#)

#astrophysicist_completion = highschool_student_client.chat.completions.create(
    #messages=[
        #{
            #"role": "system",
            #"content": "You are a physics professor who speaks in a formal, academic tone. You have been researching on quantum mechanics for the last 14 years",
        #},
        #{
            #"role": "user",
            #"content": "how do you like to spend your free time?",
        #}
    #],
    #model="gpt-4o",
#)
