inputs = {"keyboard", "mouse", "joystick", "lightpen", "stylus", "mic"}
outputs = {"printers", "monitor", "speaker"}

devices = inputs.union(outputs) # union() joints the two sets to form a new set
print(devices)

set1 = {10, 20 , 30, 40}
set2 = {50, 60, 70, "EIGHTY", 90.00, 'Hundred'}
print(set1)
print(set2)
set1.update(set2) # updates set1 with set2 values
print(set1)