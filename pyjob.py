import timer

parameters = []

with open("manifest.txt", "r") as file_:
    parameters += file_.read().split("\n")

session_length = float(parameters[0])
stdsize = float(parameters[1])
positive_mark = float(parameters[2])
negative_mark = float(parameters[3])
unattempted_mark = float(parameters[4])

default = input("Run session with default settings? (y/n)\t").lower()
his = input("Contribute to history? (y/n)\t").lower()

if default == "y":
    timer.start_session(questions=stdsize,
    allotted_time=float(parameters[0]),
    positive=positive_mark,
    negative=negative_mark,
    unattempted=unattempted_mark,
    contribute_to_history=(True if his == "y" else False))
else:
    qc = int(input(f"How many questions? (default {stdsize})\t"))
    mt = float(input(f"How long, in minutes? (default {session_length / 60})?\t")) * 60
    c = float(input(f"Correct answer: (default {positive_mark})\t"))
    w = float(input(f"Wrong answer: (default {negative_mark})\t"))
    u =  float(input(f"Unattempted: (default {unattempted_mark})\t"))

    timer.start_session(qc, mt, c, w, u,
    contribute_to_history=(True if his == "y" else False))
