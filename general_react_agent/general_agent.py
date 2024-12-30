import json

class GeneralAgent: 
    def __init__(self, system_prompt, client, interviewee, search_engine):
        self.system_prompt = system_prompt 
        self.messages = [{
            "role": "system",
            "content": self.system_prompt, 
        }]

        self.client = client
        self.interviewee = interviewee
        self.search_engine = search_engine

        self._tools = [
            {
                "type": "function",
                "function": {
                    "name": "ask_user_question",
                    "description": "Ask the user a question. Call this whenever you need more information from the user to achieve your task. The user remembers what questions was asked before and will answer accordingly",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "question": {
                                "type": "string",
                                "description": "The question you want to ask the user",
                            },
                        },
                        "required": ["question"],
                        "additionalProperties": False,
                    },
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "search_internet",
                    "description": "search the internet using Tavily to clarify anything you need to know.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "search_query": {
                                "type": "string",
                                "description": "The query you want to run to gain additional information",
                            },
                        },
                        "required": ["search_query"],
                        "additionalProperties": False,
                    },
                }
            }
 
        ]

        self._tools_map = {
            "search_internet": self.search_engine.search_internet,
            "ask_user_question": self.interviewee.ask_user_question,
        }

    def run(self):
        run_loop = True
        while run_loop:

            agent_response = self.client.send_message(self.messages, tools=self._tools)
            finish_reason = agent_response.choices[0].finish_reason

            if finish_reason =='stop':
                run_loop = False

                print("Finished Analysis. Final analysis:")
                print(agent_response.choices[0].message.content)

            elif finish_reason == 'tool_calls':
                tool_calls = agent_response.choices[0].message.tool_calls
                for tool_call in tool_calls:
                    function_name = tool_call.function.name
                    function_arguments = json.loads(tool_call.function.arguments)

                    self.messages.append({"role":"assistant", "content":"tool call function: {}, tool call arguments: {}".format(function_name, tool_call.function.arguments)})

                    function_response = self._tools_map[function_name](**function_arguments) 

                    self.messages.append({"role":"user", "content":"tool call response: {}".format(function_response)})