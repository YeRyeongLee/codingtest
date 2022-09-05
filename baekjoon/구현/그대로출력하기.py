def run():
    for _ in range(100):
        try:
            text = input()
            print(text)
        except:
            break

if __name__ == "__main__":
    run()