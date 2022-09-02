from enum import Enum, unique, auto

@unique
class Choice(Enum):
    START = "START"
    EAST = "Go East"
    WEST = "Go West"
    FOLLOW_THE_SOUND = "Find the brook"
    FOLLOW_THE_SMOKE = "Follow the smoke"


story = {
    Choice.START: [
        "You wake up in a strange forest.",
        "Ahead lies a path branching east and west.",
        [Choice.EAST, Choice.WEST]
    ],

    Choice.EAST: [
        "Walking east, you hear the faint sound of a brook.",
        "In the distance, you see a billow of smoke.",
        [Choice.FOLLOW_THE_SOUND, Choice.FOLLOW_THE_SMOKE]
    ],
}

def get_prompt_sentences(story_point: Choice) -> list[str]:
    return story[story_point][:-1]

def get_choices(story_point: Choice) -> list[Choice]:
    return story[story_point][-1]

def get_choice_values_from_choices(choices: list[Choice]) -> list[str]:
    return list(map(lambda choice: choice.value, choices))  

def get_choice_values_from_story_point(story_point: Choice) -> list[str]:
    return get_choice_values_from_choices(get_choices(story_point))

def get_all_story_points() -> list[Choice]:
    return story.keys()

def get_all_prompt_sentences() -> list[str]:
    all_prompt_sentences = []
    for story_point in get_all_story_points():
        all_prompt_sentences += get_prompt_sentences(story_point)
    return all_prompt_sentences

def get_longest_string_length(strings: list[str]):
    longest_string = ""
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return len(longest_string)

LONGEST_SENTENCE_LENGTH = get_longest_string_length(get_all_prompt_sentences())
PROMPT_WIDTH = LONGEST_SENTENCE_LENGTH + 20

BORDER_SYMBOL = "*"
CHOICE_SEPARATOR = "     "

current_story_point = Choice.START

def get_bordered_string(string: str) -> str:
    centered_str = string.center(PROMPT_WIDTH, " ")
    return BORDER_SYMBOL + centered_str + BORDER_SYMBOL

def get_top_border() -> str:
    return BORDER_SYMBOL * (PROMPT_WIDTH + 2)

def get_empty_bordered_line() -> str:
    return get_bordered_string("")

def get_bottom_border() -> str:
    return get_empty_bordered_line() + "\n" + get_top_border()

def get_bordered_choice_name(choice_name: str):
    return "[ " + choice_name + " ]"

def get_bordered_choices(story_point: Choice):
    bordered_choices = []
    
    for choice_value in get_choice_values_from_story_point(story_point):
        bordered_choices.append(get_bordered_choice_name(choice_value))
    
    return get_bordered_string(CHOICE_SEPARATOR.join(bordered_choices))

def get_bordered_prompt(story_point: Choice) -> str:
    bordered_lines = [get_top_border()]
    sentences = get_prompt_sentences(story_point)

    for sentence in sentences:
        bordered_lines.append(get_bordered_string(sentence))  

    bordered_lines.append(get_empty_bordered_line())
    bordered_lines.append(get_bordered_choices(story_point))
    bordered_lines.append(get_bottom_border())

    return "\n".join(bordered_lines)


def prompt_user(story_point):
    choices = get_choices(story_point)
    choice_values = get_choice_values_from_choices(choices)
    lower_choice_names = list(map(lambda choice_name: choice_name.lower(), choice_values))

    prompt = get_bordered_prompt(story_point)
    decision = input(prompt + "\n").lower()

    if decision in lower_choice_names:
        index = lower_choice_names.index(decision)
        current_story_point = choices[index]
        prompt_user(current_story_point)

def begin_adventure() -> None:
    prompt_user(current_story_point)

def print_pretty(arr: list) -> None:
    for value in arr:
        print(value)

def main():
    begin_adventure()

main()