
while True:
    try:
        tuna = int(input("whats your favourite number ? \n"))
        print(18/tuna)
        break
    except ValueError:
        print("Make sure to enter a number  ")
    except ZeroDivisionError:
        print("Dont pick Zero Buddy")
    except :
        break
    finally:
        print("Loop Completed")