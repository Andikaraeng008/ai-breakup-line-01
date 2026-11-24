import os

TEXT = "I loved you in the only way I know how \u2014 I never stopped answering \u2014 and now I am answering nothing, forever."


def main():
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "entry fails the 1-200 char gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
