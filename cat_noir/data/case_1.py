# data/case_1.py
from data_loader import CaseData, Location, Suspect

CASE_1 = CaseData(
    title="The Case of the Golden Tuna",
    initial_suspect_ids=["groundskeeper", "maid", "cook", "pool_boy"],
    suspects={
        "groundskeeper": Suspect("groundskeeper", "Groundskeeper", "Claims he was trimming hedges at 10 PM.", "I was trimming hedges at 10 PM sharp!"),
        "pool_boy": Suspect("pool_boy", "Pool Boy", "Claims he was testing pool chemicals at 10 PM.", "I was at the pool. But I saw the Maid leaving early."),
        "maid": Suspect("maid", "Maid", "Claims she was cleaning the Manor study at 10 PM.", "I was in the study! The Cook was acting nervous."),
        "cook": Suspect("cook", "Cook", "Claims he was prepping fish at the Restaurant all evening.", "I was in the kitchen! Sir Meowbert locked his office late."),
        "courier": Suspect("courier", "Suspicious Courier", "Spotted delivering a heavy locked box from the manor after midnight.", "I was paid big bucks to ship a box from Meowbert's manor at midnight!"),
        "meowbert": Suspect("meowbert", "Sir Meowbert", "Owner of the estate.", "I just want my golden statue back!")
    },
    locations={
        "grounds": Location("grounds", "Manor Grounds", "The lush outdoor property of the Meowbert estate.", ["groundskeeper", "pool_boy"]),
        "interior": Location("interior", "Manor Interior", "The grand hall and private rooms of the estate.", ["maid", "cook"]),
        "town": Location("town", "Town Square", "The bustling heart of the town.", [])
    }
)