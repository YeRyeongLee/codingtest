def run():
    text = input()

    for i in range(len(text)//10+1):
        print(text[i*10:i*10+10])
    
    return 0


if __name__ == "__main__":
    run()