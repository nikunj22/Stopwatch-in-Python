import time

#Press Enter to Start the Stopwatch.
#Press CTRL + C to Stop the StopWatch.

while True:
    try:
        input()
        start_time = time.time()
        print("Stopwatch started...")

    except KeyboardInterrupt:
        print("Stopwatch Stopped...")
        end_time = time.time()
        print("The total time : ",round(end_time - start_time,2),"Second")
        break