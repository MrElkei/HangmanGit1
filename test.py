from scripts.display import Display
from animations.animationWelcome import AnimationWelcome
from animations.animationHangman import AnimationHangman

display = Display()

display.animate(left_colums_animation=AnimationHangman(), middle_column_animation=AnimationWelcome())
