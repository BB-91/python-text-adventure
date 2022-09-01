from enum import Enum, unique, auto

@unique
class Choice(Enum):
    START = auto()
    EAST = auto()
    WEST = auto()
    FOLLOW_THE_SOUND = auto()
    FOLLOW_THE_SMOKE = auto()


story = {
    Choice.START: [
        "You wake up in a strange forest.",
        "Ahead lies a path branching east and west.",
        "Which direction will you go?",
        [Choice.EAST, Choice.WEST]
    ],

    Choice.EAST: [
        "Walking east, you hear the faint sound of a brook.",
        "In the distance, you see a billow of smoke.",
        "What will you do?",
        [Choice.FOLLOW_THE_SOUND, Choice.FOLLOW_THE_SMOKE]
    ],
}

def get_prompt_sentences(story_point: Choice) -> list[str]:
    return story[story_point][:-1]

def get_choices(story_point: Choice) -> list[Choice]:
    return story[story_point][-1]

def get_choice_names(story_point: Choice) -> list[str]:
    return list(map(lambda choice: choice.name, get_choices(story_point)))  

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
    
    for choice_name in get_choice_names(story_point):
        bordered_choices.append(get_bordered_choice_name(choice_name))
    
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


def begin_adventure() -> None:
    print(get_bordered_prompt(Choice.START))


def print_pretty(arr: list) -> None:
    for value in arr:
        print(value)


def main():
    begin_adventure()


main()