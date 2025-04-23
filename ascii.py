import pyfiglet

def generate_ascii_art(text: str) -> str:
    ascii_art = pyfiglet.figlet_format(text, font="standard")
    return ascii_art

if __name__ == "__main__":
    RED = "\033[91m"
    RESET = "\033[0m"

    print(f"{RED}=== ASCII Текст Генератор ==={RESET}")
    user_text = input("Введи текст: ")

    result = generate_ascii_art(user_text)
    print("\nРезультат:\n")
    print(result)
    print(f"{RED}=== Конец ==={RESET}")
