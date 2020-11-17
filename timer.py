# timer.py
# aravind suresh thakidayil

import time
import csv

def start_session(questions, allotted_time, positive, negative, unattempted,
contribute_to_history):
    qL = [0, 0, 0]
    qNo = 1
    time_taken = -1 * time.time()
    score = 0

    scheme = {"c": (positive, 0), "w": (negative, 1), "u": (unattempted, 2)}

    while qNo <= questions:
        print(f"Question no {qNo} \t\t\t\t {questions-qNo} left")
        k = input().lower()
        if k in ["c", "w", "u"]:
            score += scheme[k][0]
            qL[scheme[k][1]] += 1
            qNo += 1
        else:
            print("Try that last operation again.")
            continue

    time_taken += time.time()

    print(f"""\n\n\n\n time taken: {int(time_taken)}s 
(allotted_time: {allotted_time}s) \n\n Total questions: {questions}
\n\n Correct answers are scored {positive} and wrong answers scored
{negative}. Unattempted questions carry a penalty of {unattempted}.
\n\n Correct \t\t\t\t Incorrect \t\t\t\t Unattempted \n {'-'*100} \n
 {qL[0]} \t\t\t\t {qL[1]} \t\t\t\t {qL[2]} \n\n\n Total score: \t\t
{score} = {qL[0] * positive} + {qL[1] * negative} +
 {qL[2] * unattempted} \n\n Average time per question:
 {time_taken / questions} s \n Score per minute:
 {score * 60 / time_taken * 1.00}\n\n""")

    if contribute_to_history:
        with open("historical.csv", "a") as file_:
            writer = csv.writer(file_)
            writer.writerow([f"{time.strftime('%d')}/{time.strftime('%m')}/{time.strftime('%y')}",
            input("Session name = "), questions, qL[0], qL[1], qL[2],
            allotted_time, time_taken, score])

        print("Your performance has been recorded.")

