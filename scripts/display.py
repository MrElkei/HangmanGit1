"""Display class provides unified output interface for the Hangman game.

The module contains class of Display, that provides unified output.
The output consists of 3 columns and 7 lines in each column by default. 
The line count can be atdjusted acording to needs.
The Display class provides animation handler to displai ascii animations.
For more details see Display class docstring.

Typical usage example:
    display = Display()
    display.updateLine(0, 1, "Some text")
    display.refresh()
"""

import os
import time

class Display:
    """Dysplay class provides unified multi column output handler.

    The class provides several key functionalities of the Hangman game.
    Mainly focusing on console output. The output is organized in
    3 columns and 7 lines in each column by default. The line count can 
    be adjusted according to needs. To maintain consistent output
    the size fot the console will be adjusted to fit all content on
    the screen.

    Example of the output:
    +-------------------+-------------------------+--------------------+
    | Column 0, Line 0  | Column 1, Line 0        | Column 2, Line 0   |
    | Column 0, Line 1  | Column 1, Line 1        | Column 2, Line 1   |
    | Column 0, Line 2  | Column 1, Line 2        | Column 2, Line 2   |
    | Column 0, Line 3  | Column 1, Line 3        | Column 2, Line 3   |
    | Column 0, Line 4  | Column 1, Line 4        | Column 2, Line 4   |
    +-------------------+-------------------------+--------------------+

    Arguments:
        left_column_max:
            Set size of the left column in characters, default: 7
        middle_column_max:
            Set size of the middle column in characters, default: 77
        right_column_max:
            Set size of the right column in characters, default: 30
        init_rows:
            Set the initial line count, default: 8
        delim_1:
            Set symbols that are placed between column 0 and column 1,
            default: " | "
        delim_2:
            Set symbols that are placed between column 0 and column 1,
            default: " | "

    Methods:
        updateLine(column: int, line: int, text: str):
            Add a text to the coresponding column and line
        updateColumn(lines: list):
            Replace content of entire column by the provided list
        removeLastLine():
            Remove the last line from the display
        clearConsole():
            Clear the screen of the console
        refresh():
            Refresh the display after line or column update
        animate(Left_animation: Animation,
                middle_animation: Animation,
                right_animation: Animation, 
                framerate: int):
            Displays an ascii animation based on the provided
            Animation class.
    """

    def __init__(self,
                 left_column_max = 7,
                 middle_column_max = 77,
                 right_column_max = 30,
                 init_rows = 8,
                 delim_1 = " | ",
                 delim_2 = " | "):
        """Initialize Display class

        Sets parameters for the display output and resizes terminal 
        window if necesery.

        Arguments:
            left_column_max:
                Set size of the left column in characters, default: 7
            middle_column_max:
                Set size of the middle column in characters, default: 77
            right_column_max:
                Set size of the right column in characters, default: 30
            init_rows:
                Set the initial line count, default: 8
            delim_1:
                Set symbols that are placed between column 0 and
                column 1, default: " | "
            delim_2:
                Set symbols that are placed between column 0 and
                column 1, default: " | "
        """
        self.max_column_lengths = [left_column_max, 
                                   middle_column_max,
                                   right_column_max]
        self.display = [["" for n in range(0, init_rows)],
                        ["" for n in range(0, init_rows)],
                        ["" for n in range(0, init_rows)]]
        self.delim_1 = delim_1
        self.delim_2 = delim_2
        self._resizeTerminal()

    def _resizeTerminal(self):
        """Resizes terminal window to fit all characters of the line
        in a single line. Limitation, currently works only on CMD"""
        cols = (self.max_column_lengths[0]
               + len(self.delim_1)
               + self.max_column_lengths[1]
               + len(self.delim_2)
               + self.max_column_lengths[2])
        curent_cols, curent_rows = os.get_terminal_size()
        if curent_cols < cols:
            cmd = f'mode {cols},{curent_rows}'
            os.system(cmd)

    def updateLine(self, column = 0, index = 0, text = " "):
        """Adds line of text to a specific column and line.

        The method provides a way to add text to the specific location
        on the screen. However, the method does not refresh the screen
        output.
        Call refresh() method to display changes on the screen.
        Arguments:
            column:
                Specify the target column, default: 0
            index:
                Specify the target line in the selected column,
                default: 0
            text:
                Text to add to the specified column and line,
                defaul: " "
        """
        if len(self.display[column]) < index:
            i = index - len(self.display[column]) + 1
            b = ['' for n in range(0, i)]
            self.display[column].extend(b)
        self.display[column][index] = text

    def _get_max_row_count(self):
        """Determines the maximum length of columns."""
        max_len = 0
        for c in self.display:
            if len(c) > max_len:
                max_len = len(c)
        return max_len

    def removeLastLine(self):
        """Remove a last line from the display."""
        max_len = self._get_max_row_count()
        for n in range(0, len(self.display)):
            if max_len == len(self.display[n]):
                self.display[n].pop()

    def updateCulumn(self, column = 0, new_list = [" "]):
        """Update a column of the display with the provided list.

        Arguments:
            column:
                Selects a column to update, default: 0
            new_list:
                List of lines to replace current content of the selected
                column, default: [" "]
        """
        self.display[column] = new_list

    def _normalize(self):
        """Normalize the display output.
        
        The method unifys length of all colums so that indexError is
        not raised. Afterwards the method unifies length of every line
        according to the preset max character count. If line is shorter
        then default value " " is added until default length is reached.
        If line is longer only default lenght text is saved to the line
        """
        max_len = self._get_max_row_count()
        max_index = max_len - 1
        for n in range(0, len(self.display)):
            # Izlīdzina rindu skaitu
            if max_len > len(self.display[n]):
                self.updateLine(n, max_index, '')
            # Izlīdzina simbolu skaitu rindās skaitu
            for l in range(0, len(self.display[n])):
                line = str(self.display[n][l])
                if len(line) < self.max_column_lengths[n]:
                    c = self.max_column_lengths[n] - len(line)
                    line = line + " " * c
                elif len(line) > self.max_column_lengths[n]:
                    line = line[0:self.max_column_lengths[n]]
                self.display[n][l] = line
    
    def clearConsole(self):
        """Clear a screen of the console.
        
        The code was obtained from
        https://www.delftstack.com/howto/python/python-clear-console/
        """
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

    def _printDysplay(self):
        """Write all lines to the screen."""
        for n in range(0, len(self.display[0])):
            print(f'{self.display[0][n]}{self.delim_1}\
                {self.display[1][n]}{self.delim_2}{self.display[2][n]}')

    def refresh(self):
        """Refresh the displayed lines on the screen.
        
        The method first normalizes new output lines, then clears
        the screen and finally prints new lines.
        """
        self._normalize()
        self.clearConsole()
        self._printDysplay()

    def animate(self,
                left_colums_animation = None,
                middle_column_animation = None,
                right_column_animation = None,
                framerate = 9):
        """Display ascii animantion on the screen of the console.

        The method takes as argument frames of the animation which are
        provided based on the Animation class scaffold.
        Atributes:
            left_colums_animation:
                Frames of the animation based on the Animation scaffold.
            middle_column_animation:
                Frames of the animation based on the Animation scaffold.
            right_column_animation:
                Frames of the animation based on the Animation scaffold.
        """
        max_frames = 0
        if left_colums_animation is not None:
            self.updateCulumn(0, left_colums_animation.getFrame(0))
            if max_frames < left_colums_animation.frame_count:
                max_frames = left_colums_animation.frame_count
        if middle_column_animation is not None:
            self.updateCulumn(1, middle_column_animation.getFrame(0))
            if max_frames < middle_column_animation.frame_count:
                max_frames = middle_column_animation.frame_count
        if right_column_animation is not None:
            self.updateCulumn(2, right_column_animation.getFrame(0))
            if max_frames < right_column_animation.frame_count:
                max_frames = right_column_animation.frame_count
        self.refresh()
        left_index = 1
        middle_index = 1
        right_index = 1
        for frame_index in range(1, max_frames):
            if left_colums_animation is not None:
                self.updateCulumn(0, left_colums_animation.getFrame(left_index))
                if left_index < left_colums_animation.frame_count - 1:
                    left_index += 1
                else:
                    left_index = 0
            if middle_column_animation is not None:
                self.updateCulumn(1, middle_column_animation.getFrame(middle_index))
                if middle_index < middle_column_animation.frame_count - 1:
                    middle_index += 1
                else:
                    middle_index = 0
            if right_column_animation is not None:
                self.updateCulumn(2, right_column_animation.getFrame(right_index))
                if right_index < right_column_animation.frame_count - 1:
                    right_index += 1
                else:
                    right_index = 0
            self.refresh()
            time.sleep(1/framerate)