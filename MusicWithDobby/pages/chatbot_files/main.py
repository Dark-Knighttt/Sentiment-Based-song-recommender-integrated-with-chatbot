import json
from difflib import get_close_matches

# load knowledge_base from json file into the program

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path,'r') as file:
        data: dict = json.load(file)
    return data

# save the dictionary to the knowledge base so that next time we start the program we will have the old responses in memory too

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path,'w',encoding='utf-8') as file:
        json.dump(data,file,ensure_ascii = False,indent= 2)
        # file.write(data)

# function to find best match from the dictionary with user questions of type string

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff = 0.8)
    return matches[0] if matches else None

# a function to get answer of each question
def get_answer_for_question(question:str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

# creating mainscript

def chat_bot(prompt:str):
    # print("i am called")
    knowledge_base: dict = load_knowledge_base('pages\chatbot_files\knowledge_base.json')

    if True:
        user_input = prompt
        if user_input.lower() == 'quit' :
            exit

        best_match: str | None = find_best_match(user_input.lower(), [q["question"] for q in knowledge_base["questions"]])
        # print("level 2 cleared")

        if best_match:
            answer: str =  get_answer_for_question(best_match, knowledge_base)
            response = answer
            # print("level3")
        else:
            response = f'I don\'t know , how to answer this !'
            # print("Bot: I don't know the answer. Can you teach me?")
            # new_answer: str = input('Type the answer or "skip" to skip: ')

            # if new_answer.lower() != 'skip':
            #     knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
            #     save_knowledge_base('knowledge_base.json', knowledge_base)
            #     print('Bot: Thank you! I learned a new reponse!')
            #     print("level4")
    # print("level5")    
    return response
# if __name__ == "__main__":
    # chat_bot(prompt)