import threading

def print_numbers():
    for i in range(1, 11):
        print(i)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

print("Finished executing the threads.")
