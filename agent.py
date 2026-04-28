import json

class ReflectionAgent:
    def __init__(self, tree_file):
        # Load the tree from JSON
        with open(tree_file, "r") as f:
            self.tree = json.load(f)["nodes"]
        # Index nodes by ID for quick lookup
        self.nodes = {node.get("id", f"node_{i}"): node for i, node in enumerate(self.tree)}
        self.state = {"axis1": {}, "axis2": {}, "axis3": {}, "answers": {}}

    def run(self):
        current_id = "START"
        while True:
            node = self.nodes[current_id]

            if node["type"] == "start":
                print(node["text"])
                current_id = node["target"]

            elif node["type"] == "question":
                print(node["text"])
                for i, option in enumerate(node["options"], 1):
                    print(f"{i}. {option}")
                choice = int(input("Choose an option: "))
                answer = node["options"][choice - 1]
                self.state["answers"][current_id] = answer
                current_id = node["target"]

            elif node["type"] == "decision":
                answer = list(self.state["answers"].values())[-1]
                for rule, target in node["rules"].items():
                    if answer in rule.split("|"):
                        current_id = target
                        break

            elif node["type"] == "reflection":
                print("Reflection:", node["text"])
                if "signal" in node:
                    axis, value = node["signal"].split(":")
                    self.state[axis][value] = self.state[axis].get(value, 0) + 1
                current_id = node["target"]

            elif node["type"] == "bridge":
                print(node["text"])
                current_id = node["target"]

            elif node["type"] == "summary":
                axis1 = max(self.state["axis1"], key=self.state["axis1"].get, default="neutral")
                axis2 = max(self.state["axis2"], key=self.state["axis2"].get, default="neutral")
                axis3 = max(self.state["axis3"], key=self.state["axis3"].get, default="neutral")
                print(node["text"].format(axis1=axis1, axis2=axis2, axis3=axis3))

                current_id = node["target"]

            elif node["type"] == "end":
                print(node["text"])
                break

if __name__ == "__main__":
    agent = ReflectionAgent("reflection-tree.json")
    agent.run()
