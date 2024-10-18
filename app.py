from daily_classic import daily_answer
from weekly_challenge import weekly_answer
from sequence import sequence_answer
from daily_chill import chill_answer
from daily_extreme import extreme_answer
from google_sheets import sheet_append
from datetime import datetime
import sys


def main(game):

    if game == 'Weekly':
        print(f"{datetime.now().strftime('%D %H:%M:%S')}: Running for Daily and Weekly")
        answers = weekly_answer()
    # weekly_answers = ["ARBOR", "STARK", "LEAVE", "GOOFY"] # for testing only

    elif game == 'Sequence':
        print(f"{datetime.now().strftime('%D %H:%M:%S')}: Running for Sequence")
        answers = sequence_answer()
    # sequence_answers = ["VOCAL", "CLEAT", "MANOR", "PLAIT"] # for testing only

    elif game == 'Chill':
        print(f"{datetime.now().strftime('%D %H:%M:%S')}: Running for Chill")
        answers = chill_answer()
    # chill_answers = ["VOCAL", "CLEAT", "MANOR", "PLAIT"] # for testing only

    elif game == 'Extreme':
        print(f"{datetime.now().strftime('%D %H:%M:%S')}: Running for Extreme")
        answers = extreme_answer()
        # answers = ["VOCAL", "CLEAT", "MANOR", "PLAIT"] # for testing only

    if answers:
        sheet_append(answers, game)
        print(f"{datetime.now().strftime('%D %H:%M:%S')}: All answers have been stored.")


if __name__ == "__main__":
    game = sys.argv[1]
    main(game)
