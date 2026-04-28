class DecisionTree:
    def __init__(self):
        self.tree = {
            "Start": {
                "Did you complete your tasks today?": {
                    "Yes": {
                        "Did you face challenges?": {
                            "Yes": "Reflect on how you overcame challenges.",
                            "No": "Celebrate your productivity!"
                        }
                    },
                    "No": {
                        "Was it due to external factors?": {
                            "Yes": "Identify what was beyond your control.",
                            "No": "Plan how to improve tomorrow."
                        }
                    }
                }
            }
        }

    def traverse(self, node=None):
        if node is None:
            node = self.tree["Start"]

        question = list(node.keys())[0]
        print(question)

        answer = input("Answer (Yes/No): ").strip().capitalize()
        next_node = node[question].get(answer)

        if isinstance(next_node, dict):
            self.traverse(next_node)
        else:
            print("Reflection:", next_node)


if __name__ == "__main__":
    dtree = DecisionTree()
    dtree.traverse()
