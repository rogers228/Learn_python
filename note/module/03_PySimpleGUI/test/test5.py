import PySimpleGUI as sg

class Table(sg.Table):

    def get_all_iids(self):
        """
        Return list of unique id for each row in table, all iid start from '1'
        """
        return list(self.Widget.get_children())

    def select_to_iid(self, select):
        """
        Convert id of selected row into iid
        """
        return list(map(lambda item:str(item+1), select))

    def delete_iids(self, *iids):
        self.Widget.delete(*iids)

    def delete(self, select, position):
        """
        Delete selected rows in table
        select: list of id of selected rows, all PSG id start from 0
        """
        if select == []:
            self.status.update('No row selected to delete !')
            return
        if sg.popup_yes_no("Are you sure to delete ?") == 'Yes':
            select_iid = self.select_to_iid(select)
            self.delete_iids(*select_iid)
            self.tree_ids = self.get_all_iids() # update iid list of PSG table
            self.update(select_rows=[])         # Deselect rows of table

    def move_up(self, select, position):
        """
        Move selected rows one step up
        select: list of id of selected rows, all PSG id start from 0
        """
        if select == []:
            self.status.update('No row selected to move up !')
            return
        iids = self.get_all_iids()
        select_iid = self.select_to_iid(select)
        index = list(map(iids.index, select_iid))   # move index one step up
        if index[0] == 0:                           # if on the top of table
            self.status.update('Selected rows are already on the top of table !')
            return
        for i in index:                             # switch with previous one
            iids[i], iids[i-1] = iids[i-1], iids[i]
        self.Widget.set_children('', *iids)         # update iid list of table
        self.Widget.see(select_iid[0])              # ensure top one visible
        self.tree_ids = iids                        # update PSG iid table

    def move_down(self, select, position):
        """
        Move selected rows one step down
        select: list of id of selected rows, all PSG id start from 0
        """
        if select == []:
            self.status.update('No row selected to move down !')
            return
        iids = self.get_all_iids()
        select_iid = self.select_to_iid(select)
        index = list(map(iids.index, select_iid))
        if index[-1] == len(iids)-1:                # if on bottom of table
            self.status.update('Selected rows are already on the bottom of table !')
            return
        for i in reversed(index):                   # switch with next one
            iids[i], iids[i+1] = iids[i+1], iids[i]
        self.Widget.set_children('', *iids)         # update iid list of table
        self.Widget.see(select_iid[-1])             # ensure bottom one visible
        self.tree_ids = iids                        # update PSG iid table

    def edit(self, select, position):
        """
        Edit data of selected row on another popup window
        select: list of id of selected rows, all PSG id start from 0
        """
        if len(select) != 1:                        # Only one row to go edit
            self.status.update('Select only one row to edit !')
            return
        iid = self.select_to_iid(select)[0]         # get first iid
        values = self.Widget.set(iid)               # get values of row iid
        size = (max(map(len, self.header)), 1)      # size of header text
        layout = [
            [sg.Text(column, size=size), sg.Input(values[column], key=column)]
                for column in self.header] + [[sg.OK(), sg.Cancel()]]
        win = sg.Window('Edit', layout, modal=True, finalize=True)
        self.remove_dash_box(win)
        while True:
            evt, vals = win.read()
            if evt in (sg.WINDOW_CLOSED, 'Cancel'):
                break
            elif evt == 'OK':
                for column in self.header:          # update value of all columns
                    self.Widget.set(iid, column=column, value=vals[column])
                break
        win.close()

    def get_new_iid(self):
        """
        Generate one new unique iid
        """
        iids = self.get_all_iids()
        i = 1
        while str(i) in iids:
            i += 1
        return str(i)

    def insert(self, select, position):
        """
        Insert one blank row into table.
        select: list of id of selected rows, all PSG id start from 0
        position: where to insert, can be 'Before' or 'After' selected rows,
            'Top' or 'Bottom' of table.
        """
        if position in ('Before', 'After') and select == []:
            self.status.update(f'Select one row to insert {position.lower()} !')
            return
        layout = [
            [sg.Text(column, size=(12, 1)), sg.Input('', key=column)]
                for column in self.header
        ] + [[sg.OK(), sg.Cancel()]]
        win = sg.Window('Insert', layout, modal=True, finalize=True)
        self.remove_dash_box(win)

        while True:
            evt, vals = win.read()
            if evt in (sg.WINDOW_CLOSED, 'Cancel'):
                break
            elif evt == 'OK':
                iids = self.get_all_iids()
                select_iid = self.select_to_iid(select)
                if position == 'Before':            # Find index for insertion
                    index = iids.index(select_iid[0])
                elif position == 'After':
                    index = iids.index(select_iid[-1])+1
                elif position == 'Top':
                    index = 0
                else:
                    index = len(iids)
                # Insert new row with new values into table
                values = [vals[column] for column in self.header]
                iid = self.get_new_iid()
                self.Widget.insert('', index, iid=iid, values=values)
                self.Widget.see(iid)                # ensure new one visible
                self.tree_ids = self.get_all_iids() # update PSG iid table
                # new row iid converted into selected id, then new row selected
                self.update(select_rows=[int(iid)-1])
                break
        win.close()

    def copy(self, select, position):
        """
        Copy values of each selected row to clipboard
        select: list of id of selected rows, all PSG id start from 0
        """
        if select == []:
            self.status.update('No row selected to copy !')
            return
        select_iid = self.select_to_iid(select)
        self.clipboard = []
        for iid in select_iid:
            data_dict = self.Widget.set(iid)        # get row data
            self.clipboard.append([data_dict[column] for column in self.header])

    def paste(self, select, position):
        """
        Paste content of clipboard into table
        select: list of id of selected rows, all PSG id start from 0
        position: where to paste, can be 'Before' or 'After' selected rows,
            'Top' or 'Bottom' of table.
        """
        if self.clipboard == None:
            self.status.update('No data to paste !')
            return
        if position in ('Before', 'After') and select == []:
            self.status.update(f'Select rows to paste {position.lower()} !')
            return
        iids = self.get_all_iids()
        select_iid = self.select_to_iid(select)
        if position == 'Before':            # Find index for insertion
            index = iids.index(select_iid[0])
        elif position == 'After':
            index = iids.index(select_iid[-1])+1
        elif position == 'Top':
            index = 0
        else:
            index = len(iids)
        id_list = []
        for i, values in enumerate(self.clipboard): # paste content of clipboard
            iid = self.get_new_iid()
            id_list.append(int(iid)-1)
            self.Widget.insert('', index+i, iid=iid, values=values)
        self.tree_ids = self.get_all_iids()         # update PSG iid list
        self.update(select_rows=id_list)            # pasted rows selected
        self.Widget.see(str(id_list[-1]+1))         # ensure last row visible
        self.Widget.see(str(id_list[0]+1))          # ensure first row visible

    def align_headings(self, alignment):
        """
        Aligment for headings of table
        alignment: list of anchor string for each column of headings
            anchor string can be one of
                'nw', 'n', 'ne', 'w', 'center', 'e', 'sw', 's', 'se'.
        """
        for cid, anchor in enumerate(alignment):
            self.Widget.heading(cid, anchor=anchor)

    def align_columns(self, alignment):
        """
        Aligment for columns of table
        alignment: list of anchor string for each column of table
            anchor string can be one of
                'nw', 'n', 'ne', 'w', 'center', 'e', 'sw', 's', 'se'.
        """
        for cid, anchor in enumerate(alignment):
            self.Widget.column(cid, anchor=anchor)

    def double_click(self, event):
        """
        Additional event for double-click on header
        event: class event
        """
        self.status.update('')  # Widget event, so clear status bar here.
        # what part clicked
        region = self.Widget.identify("region", event.x, event.y)
        if region == 'heading': # Only care double-clock on headings
            # check which column clicked
            cid = int(self.Widget.identify_column(event.x)[1:])-1
            values = self.get_all_values()  # gete all values and sorting by key
            values = sorted(values, key=lambda item:String(item[cid]),
                reverse=self.reverse[cid])  # reverse all the time
            self.update(values=values)        # update full table with sorted values
            self.clipboard = None           # clear clipboard after sorting
            self.reverse[cid] = not self.reverse[cid]   # reverse sorting

    def initial(self, status, header, header_alignment, column_alignment):
        """
        Initial setting for related information
        status: statusbar element to show status
        header: list of string, headings of table.
        header_alignment: list of anchor string for headings
        column_alignment: list of anchor string for columns
        """
        self.status, self.header = status, header
        self.align_headings(header_alignment)
        self.align_columns(column_alignment)
        # Initialize reverse settings of sorting for each heading
        self.reverse = [False]*len(header)
        # Add binding of double-click event on headings
        self.Widget.bind('<Double-1>', self.double_click, add='+')

    def remove_dash_box(self, win):
        """
        Remove dash box of element, skip Input-related elements.
        """
        for key, element in win.AllKeysDict.items():    # all elements with key
            if not isinstance(element,
                    (sg.InputText, sg.InputCombo, sg.InputOptionMenu)):
                element.Widget.configure(takefocus=0)   # no keyboard focus

    def get_all_values(self):
        """
        Get values of all rows in existing table.
        """
        return [self.Widget.item(row)['values'] for row in self.get_all_iids()]

class String():
    """
    String for comparison in sorting
    """
    def __init__(self, value):
        self.value = value
        try:
            self.value = float(value)
            self.type = 'number'
        except:
            self.value = value
            self.type = 'string'

    def __gt__(self, value):
        if self.type == value.type:
            result = self.value > value.value
        else:
            result = False if self.type == 'string' else True
        return result

    def __ge__(self, value):
        if self.type == value.type:
            result = self.value >= value.value
        else:
            result = False if self.type == 'string' else True
        return result

    def __lt__(self, value):
        if self.type == value.type:
            result = self.value < value.value
        else:
            result = True if self.type == 'string' else False
        return result

    def __le__(self, value):
        if self.type == value.type:
            result = self.value <= value.value
        else:
            result = True if self.type == 'string' else False
        return result

    def __eq__(self, value):
        if self.type == value.type:
            result = self.value == value.value
        else:
            result = False
        return result

    def __repr__(self):
        return str(self.value)


# All data should be in string format for no conversion when edit in sg.Input
data = [
    ["Name",         "Cases/All", "Case/Day", "Deaths/All", "Death/Day"],
    ["Global",       "80773033",    "563983",    "1783619",     "11784"],
    ["USA",          "19147627",    "174814",     "332423",      "1779"],
    ["India",        "10244852",     "20549",     "148439",       "286"],
    ["Brazil",        "7504833",     "20548",     "191570",       "431"],
    ["Russian",       "3131550",     "26513",      "56426",       "599"],
    ["France",        "2530400",     "11295",      "63701",       "969"],
    ["UK",            "2382869",     "53135",      "71567",       "458"],
    ["Italy",         "2067487",     "11210",      "73029",       "659"],
    ["Spain",         "1893502",      "7717",      "50442",        "36"],
    ["Germany",       "1687185",     "22459",      "32107",      "1129"],
    ["Colombia",      "1603807",      "9310",      "42374",       "203"],
    ["Argentina",     "1590513",      "6586",      "42868",       "218"],
    ["Mexico",        "1389430",      "5996",     "122855",       "429"],
    ["Turkey",        "1364242",     "15805",      "20388",       "253"],
    ["Poland",        "1281414",     "12780",      "28019",       "565"],
    ["Iran",          "1212481",      "6108",      "54946",       "132"],
    ["Ukraine",       "1045348",      "7986",      "18324",       "243"],
    ["South Africa",  "1021451",      "9580",      "27568",       "497"],
    ["Peru",          "1008908",      "1251",      "37525",        "51"],
    ["Netherlands",    "778293",      "7561",      "11218",       "171"],
]

sg.theme('DarkBlue')
sg.set_options(button_element_size=(6, 1), auto_size_buttons=False,
    button_color=('white', 'blue'), font='Courier 11')

frame_button = [[sg.Button('Edit'), sg.Button('Delete'), sg.Button('Insert')]]
frame_copy   = [[sg.Button('Copy')], [sg.Button('Paste')]]
frame_move   = [[sg.Button('MoveUp')], [sg.Button('MoveDn')]]
frame_radio  = [
    [sg.Radio('Before', 'Position', size=(8, 1), key='Before'),
     sg.Radio('After',  'Position', size=(8, 1), key='After')],
    [sg.Radio('Top',    'Position', size=(8, 1), key='Top'),
     sg.Radio('Bottom', 'Position', size=(8, 1), key='Bottom', default=True)]]

layout = [
    [sg.Column(frame_button), sg.Column(frame_radio), sg.Column(frame_copy),
     sg.Column(frame_move)],
    [Table(data[1:], headings=data[0], auto_size_columns=False,
        def_col_width=13, enable_events=True, key='-TABLE-')],
    [sg.StatusBar('Double click header to do sorting', size=(60, 1),
        key='-STATUS-')],
]

window = sg.Window('Table', layout, use_default_focus=False, finalize=True)
table, status = window['-TABLE-'], window['-STATUS-']
table.initial(status, data[0], ['center']*5, ['center']+['e']*4)
table.remove_dash_box(window)

function = {
    'Edit'  :table.edit, 'Delete':table.delete, 'Insert':table.insert,
    'Copy'  :table.copy, 'Paste' :table.paste,  'MoveUp':table.move_up,
    'MoveDn':table.move_down}

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    # print(event, values)
    status.update('')   # Clear status bar
    select = values['-TABLE-']
    position = 'Bottom'
    for key in ('Before', 'After', 'Top', 'Bottom'):
        if values[key]:
            position = key
            break
    if event in function:
        function[event](select, position)

window.close()