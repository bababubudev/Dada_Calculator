import operator
import time
from os import system, name

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.pow,
}

calculation = ""

def check_response(player_input) -> object:
    response_p = ["yes", "sure", "okay", "alright", "aight", "go"]
    response_n = ["no", "nah", "sorry"]

    modified_input = player_input.split()[0].lower()
    amount_of_responses = max(len(response_p), len(response_n))
    amount_of_spaces = player_input.count(" ")
    amount_of_words = player_input.count(" ") + 1

    looper = 0 if amount_of_spaces == 0 else 1
    for _ in range(amount_of_words):
        for extern in range(amount_of_responses):
            if extern == 0: intern = 0
            if len(modified_input) <= 1:
                first_char = " "
                second_char = " "
            else:
                first_char = modified_input[0]
                second_char = modified_input[1]

            if response_p[extern].startswith(first_char):
                if response_p[extern].find(second_char) == modified_input.find(second_char):
                    return 1, response_p[extern]
            else:
                for item in response_n:
                    if item.startswith(first_char) and item.find(
                        second_char
                    ) == modified_input.find(second_char):
                        return -1, item

        if amount_of_spaces == 0:
            return 0, " "

        modified_input = player_input.split()[looper].lower() if (amount_of_spaces > 0) else modified_input.lower()
        looper += 1
        extern = 0


def respond_response(str):
    value, string = check_response(str)

    print("[", end='')
    if value == 1:
        if len(str) == len(string):
            print(
                'Ok see you I guess... You could have just pressed the X up there but whatever.',
                end='',
            )

        else:
            print(f"{str.capitalize()}? You mean { string.upper()}? Alright, whatever you say man.", end='')
    elif value == -1:
        if len(str) == len(string):
            print(f"Stop wasting my goddamn time with that {string} ass response. Now go back.", end='')
        else:
            print(f"{str.capitalize()}? You mean {string.upper()} ? God damnit. Whatever.", end='')
    else:
        print(f"Shit negro! Is \"{str.upper()}\" all you had to say?! Tell me again clearly mofo.", end='')
    print("]")


def sort_input(input_value) -> object:
    operators = ["+", "-", "*", "/", "^", "%"]
    num_value_dictionary = {}

    operator_dictionary = {
        k: operator_values
        for k, operator_values in enumerate(input_value)
        if input_value[k] in operators
    }

    list_of_operators = list(operator_dictionary)

    range_iterator = 0
    for l in range(len(operator_dictionary) + 1):
        if l >= len(list_of_operators):
            num_value_dictionary[l] = float(input_value[range_iterator: len(input_value)])
        else:
            num_value_dictionary[l] = float(input_value[range_iterator: list_of_operators[l]])
            range_iterator = list_of_operators[l] + 1

    return operator_dictionary, num_value_dictionary


def ask_response() -> int:
    new_player_input = str(input(f"\nAre you sure you want to {calculation}? : "))
    value, string = check_response(new_player_input)
    respond_response(new_player_input)
    return value

def clear():
    cleared = True
    _ = system('cls') if name == 'nt' else system('clear')

def store_history(str):
    for _ in range(1):
        history.append(str)

command_dic = {
    "Close program." : "end",
    "Clear screen." : "clear",
    "Check calculation history." : "history",
    "Clear calculation history." : "clh",
    "List all the commands." : "cmdl",
    "Force end the program." : "fend"
}

commands = list(command_dic)
history = []

print('\nType "cmdl" to see the list of commands.')

while True:
    try:
        calculation = input ("Input: ").lower()
        operator_dic, value_dic = sort_input(calculation)
        operator_list = list(operator_dic)
        value_list = list(value_dic)

        result = 0
        for i in range(len(operator_list)):
            if i == 0: 
                result = ops[operator_dic[operator_list[i]]](value_dic[value_list[i]], value_dic[value_list[i + 1]])
            else : result = ops[operator_dic[operator_list[i]]](result, value_dic[value_list[i + 1]])

        if result - int(result) == 0: result = int(result)
        output = f"\n [ {calculation} = {result} ] \n"
        store_history(output)
        print(output)
    except:
        value = 0
        want_to_break = False
        want_to_pass = False
        if calculation == command_dic[commands[0]].lower():
            while (value == 0):
                value = ask_response()
                if value == -1:
                    want_to_pass = True
                elif value == 1:
                    for timing in range(5):
                        b = "Shutting down in: " + (f" {5 - timing}")
                        print (b, end="\r")
                        time.sleep(1)
                    want_to_break = True
            if want_to_break : break
        elif calculation == command_dic[commands[1]].lower():
            clear()
        elif calculation == command_dic[commands[2]].lower():
            if not history:
                for element in history:
                    print(element)
            else:
                print ("Nothing to show in the history!\n")
        elif calculation == command_dic[commands[3]].lower():
            history.clear()
            print("History cleared.\n")
        elif calculation == command_dic[commands[4]].lower():
            for cmd in commands:
                print ("[", command_dic[cmd], "] = ", cmd)
            print("\n")
        elif calculation == command_dic[commands[5]].lower():
            print ("Force ending...\n")
            break
        else:
            print(f"\nInvalid input operation: [ {calculation} ]. \nType \"cmdl\" to check the command list \n")