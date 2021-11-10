import os
import sys

class Display:

    def __init__(self, left_column_max = 7, middle_column_max = 77, right_column_max = 30, init_rows = 8, delim_1 = " | ", delim_2 = " | "):
        # Displeja izvades parametri
        self.max_column_lengths = [left_column_max, middle_column_max, right_column_max]
        self.display = [["" for n in range(0, init_rows)], ["" for n in range(0, init_rows)], ["" for n in range(0, init_rows)]]
        self.delim_1 = delim_1
        self.delim_2 = delim_2
        
        self._resizeTerminal()

    # Strādā tikai uz Windows
    # TODO pievienot linux un mac OS atbalstu
    def _resizeTerminal(self):
        cols = self.max_column_lengths[0] + len(self.delim_1) + self.max_column_lengths[1] + len(self.delim_2) + self.max_column_lengths[2]
        curent_cols, curent_rows = os.get_terminal_size()
        if curent_cols < cols:
            cmd = f'mode {cols},{curent_rows}'
            os.system(cmd)

    # ierakstīt tekstu noteiktā displeja kolonā un rindā
    def updateLine(self, column = 0, index = 0, text = ""):
        try:
            if len(self.display[column]) < index:
                i = index - len(self.display[column]) + 1
                b = ['' for n in range(0, i)]
                self.display[column].extend(b)
            
            self.display[column][index] = text

        except IndexError as msg:
            print('updateLine metode saskārās ar IndexError, visticamāk column vērtība ir lielāka par 2')
            print(msg)
            sys.exit()

    # Noskaidrojam maksimālo rindu skaitu displeja kolonās
    def _get_max_row_count(self):
        max_len = 0
        for c in self.display:
            if len(c) > max_len:
                max_len = len(c)
        
        return max_len

    # Izdzēst pēdējo rindu no displeja izvades
    def removeLastLine(self):
        max_len = self._get_max_row_count()
        for n in range(0, len(self.display)):
            if max_len == len(self.display[n]):
                self.display[n].pop()


    # ierakstīt noteiktas kolonas saturu kā sarakstu
    def updateCulumn(self, column = 0, new_list = []):
        try:
            self.display[column] = new_list

        except IndexError as msg:
            print('updateCulumn metode saskārās ar IndexError, visticamāk column vērtība ir lielāka par 2')
            print(msg)
            sys.exit()

    # Izlīdzina līniju garumu un līniju skaitu displejā
    def _normalize(self):
        max_len = self._get_max_row_count()

        # Izlīdzina rindu un simbolu skaitu visās kolonās
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
    
    # Notīra displeju
    # Kods ņemts no https://www.delftstack.com/howto/python/python-clear-console/
    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    # Atjaunina displeja izvadi
    def refresh(self):
        self._normalize()
        self.clearConsole()
        for n in range(0, len(self.display[0])):
            print(f'{self.display[0][n]}{self.delim_1}{self.display[1][n]}{self.delim_2}{self.display[2][n]}')
