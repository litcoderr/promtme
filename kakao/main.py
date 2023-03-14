"""
Generates prompt for response recommendations of Kakaotalk message
"""

from typing import List
import argparse
import pandas as pd
from pathlib import Path

parser = argparse.ArgumentParser(description='kakaotalk prompt generator settings')
parser.add_argument('-i', '--input_folder', type=str, help='Path to input folder')
args = parser.parse_args()


def format_msg(_pd_csv: pd.DataFrame) -> List[str]:
    """
    """
    msg = []
    for index, row in _pd_csv.iterrows():
        msg.append(f"[{row['User']}] : {row['Message']}\n")
    return msg

prompt = []

if __name__ == "__main__":
    input_folder_path = Path(args.input_folder)
    csv_path = input_folder_path / "chat.csv"
    result_path = input_folder_path / "result.txt"
    pd_csv = pd.read_csv(csv_path)

    # User specifications
    print("Who are you: ", end="")
    NAME = input()
    prompt.append(f"My name is {NAME}.\n")

    # Number of recent conversations to feed
    print("N number of conversation: ", end="")
    N = int(input())
    pd_csv = pd_csv[-N:]

    prompt.append("This is a conversation from a messenger app. Format is as follows.\n")
    prompt.append("[User1] : Message1\n")
    prompt.append("[User2] : Message2\n")
    prompt.append(f"How should I {NAME} reply to this following message in korean?\n\n")
    prompt.extend(format_msg(pd_csv))

    # make prompt string
    prompt_str = ""
    for s in prompt:
        prompt_str = prompt_str + s

    with open(result_path, 'w', encoding="utf-8") as f:
        f.write(prompt_str)
