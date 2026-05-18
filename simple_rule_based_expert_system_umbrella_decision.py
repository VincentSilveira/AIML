rules = [
    {"conditions": {"raining": "yes"}, "decision": "Carry an umbrella"},
    {"conditions": {"raining": "no", "cloudy": "yes", "jacket": "no"}, "decision": "Carry an umbrella"}
]


def make_decision(facts, rules):
    for rule in rules:
        if all(facts.get(key) == value for key, value in rule["conditions"].items()):
            return rule["decision"]
    return "No need to carry an umbrella"


def main():
    print("Umbrella Decision Support System")

    facts = {
        "raining": input("Is it raining? (yes/no): ").strip().lower(),
        "cloudy": input("Is it cloudy? (yes/no): ").strip().lower(),
        "jacket": input("Do you have a jacket? (yes/no): ").strip().lower()
    }

    decision = make_decision(facts, rules)
    print(f"\nDecision: {decision}")

if __name__ == "__main__":
    main()
