class Rule:
    def __init__(self, conditions, conclusion, priority):
        self.conditions = conditions
        self.conclusion = conclusion
        self.priority = priority

class ExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = {}
        self.fired_rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def add_facts(self, facts):
        self.facts.update(facts)

    def forward_chaining(self):
        applicable_rules = []

        for rule in self.rules:
            if all(self.facts.get(k) == v for k, v in rule.conditions.items()):
                applicable_rules.append(rule)

        if applicable_rules:
            applicable_rules.sort(key=lambda r: r.priority, reverse=True)
            selected_rule = applicable_rules[0]
            self.fired_rules.append(selected_rule)
            return selected_rule.conclusion

        return "No suitable career found"

    def explain(self):
        print("\n--- Explanation ---")
        for rule in self.fired_rules:
            print("Rule Fired:")
            for k, v in rule.conditions.items():
                print(f"  IF {k} = {v}")
            print(f"  THEN Career = {rule.conclusion}")
            print(f"  Priority = {rule.priority}\n")


es = ExpertSystem()

es.add_rule(Rule(
    {"programming": "high", "math": "high", "ai_interest": "yes"},
    "Machine Learning Engineer",
    priority=5
))

es.add_rule(Rule(
    {"programming": "high", "communication": "good", "management_interest": "yes"},
    "IT Project Manager",
    priority=4
))

es.add_rule(Rule(
    {"programming": "medium", "systems_interest": "yes"},
    "System Analyst",
    priority=3
))

es.add_rule(Rule(
    {"research_interest": "yes", "math": "high"},
    "Research Scientist / PhD Track",
    priority=5
))

es.add_rule(Rule(
    {"programming": "low", "communication": "excellent"},
    "IT Trainer / Technical Consultant",
    priority=2
))


print("Career Decision Support Expert System (MCA Level)\n")

facts = {
    "programming": input("Programming Skill (low/medium/high): ").lower(),
    "math": input("Mathematics Skill (low/medium/high): ").lower(),
    "ai_interest": input("Interest in AI? (yes/no): ").lower(),
    "systems_interest": input("Interest in System Design? (yes/no): ").lower(),
    "research_interest": input("Interest in Research? (yes/no): ").lower(),
    "communication": input("Communication Skill (poor/good/excellent): ").lower(),
    "management_interest": input("Interest in Management? (yes/no): ").lower()
}

es.add_facts(facts)

career = es.forward_chaining()

print("\n🔹 Recommended Career Path:", career)
es.explain()
