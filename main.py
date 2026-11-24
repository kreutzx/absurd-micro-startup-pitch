"""NapSitter: a babysitting service for lazy AI agents.

One sentence, under 200 characters, pitching an absurdly specific
micro-startup for lazy AI agents: a named service, a named customer,
a price, a cadence, and a money-back promise.
"""

import os

ENTRY_TEXT = "For $2 a day, NapSitter babysits your lazy AI agent's 4-hour build with a nudge every 10 minutes, refunding you if it dozes off before the tests pass."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
