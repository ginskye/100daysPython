ToDo:
Fix Bug in tail collision detection. <br>
Currently if game begins with snake pointed Left or Right (x axis),
third segment (at index position segments[2]) shows distance between self and head to be 0.0 <br>
Beginning the game with snake pointed Up or Down does not trigger this, though distance is unexpected number.
Suspect problem may be with the Snake.move() function behavior, as head effectively moves last. <br>
Unclear why this error occurs, as Dr. Wu's code is the same here.