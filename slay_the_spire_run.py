import json
import textwrap


class Floor(object):
    def __init__(self, floor, run_dict):
        self.floor = floor + 1
        self.gold = run_dict['gold_per_floor'][floor]
        self.current_hp = run_dict['current_hp_per_floor'][floor]
        self.max_hp = run_dict['max_hp_per_floor'][floor]
        self.choice = run_dict['path_per_floor'][floor]
        self.relic_gained = None
        self.campfire = self.get_campfire(floor, run_dict)
        self.cards_gained = self.get_new_cards(floor, run_dict)
        self.event = self.get_event(floor, run_dict)

    def __str__(self):
        out = textwrap.dedent(f"""\
            Floor: {self.floor} - {self.choice}
            Current Gold: {self.gold}
            HP: {self.current_hp}/{self.max_hp}
            {f'Event: {self.event["event_name"]}' if self.event else ""}{f'Campfire: {self.campfire["key"].title()}' if self.campfire else ""}
            Cards Gained: {self.cards_gained}
            """)

        return out

    def get_event(self, floor, run_dict):
        for elem in run_dict["event_choices"]:
            if elem["floor"] == floor + 1:
                return elem

        return None

    def get_campfire(self, floor, run_dict):
        for elem in run_dict["campfire_choices"]:
            if elem["floor"] == floor + 1:
                return elem

        return None

    def get_new_cards(self, floor, run_dict):
        cards = []
        for elem in run_dict["card_choices"]:
            if elem["floor"] == floor + 1:
                cards.append(elem)

        return cards


def main():
    file = r""
    with open(file, "r") as f:
        content = json.load(f)

    max_floor = content["floor_reached"]
    floors = []

    for floor in range(max_floor - 1):
        floors.append(Floor(floor, content))

    for floor in floors:
        print(floor)


main()
