# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.4cvs on Sat Dec 31 00:13:54 2005

import wx
from Gnumed.pycommon import gmDispatcher
from Gnumed.business import gmPerson, gmVaccination

#utilities 

def expand_tree(t, root, nonzero = -1):
    	if not nonzero:
		return
	t.Expand(root)
	c, cookie = t.GetFirstChild(root)
	#import pdb
	#pdb.set_trace()
	while c.IsOk():
		t.Expand(c)
		if t.GetChildrenCount(c) > 0:
			expand_tree(t, c, nonzero -1 )
		c, cookie = t.GetNextChild(root, cookie)

def stringify_days( d):
			orig_d = d
			if not d:
				return ' none'
			unit= ' days'

			if abs(d - int(d) ) < 0.001:
				d = int(d)

			if d < 0.5 :
				d *= 24
				d = int(d)
				unit=' hours'
			
			elif d > 29:
				unit =  ' months'
				d /= 30
				
				if d != int (d/10) * 10:
					d = int( d* 10) / 10
					
				if  d > 23 :
					unit = ' years'
					d = orig_d / 365
				
					if d != int (d/10) * 10:
						d = int (  d * 10) / 10
				
			return str(d) + unit

#<1136015544262341759wxGlade replace dependencies>
class cAU_VaccV01Panel(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: cAU_VaccV01Panel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, -1, style=0)
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, -1)
        self.window_1 = wx.SplitterWindow(self.notebook_1_pane_2, -1, style=wx.SP_3D|wx.SP_BORDER)
        self.window_1_pane_2 = wx.Panel(self.window_1, -1)
        self.window_1_pane_1 = wx.Panel(self.window_1, -1)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, -1)
        self.window_2 = wx.SplitterWindow(self.notebook_1_pane_1, -1, style=wx.SP_3D|wx.SP_BORDER|wx.CLIP_CHILDREN)
        self.window_3 = wx.SplitterWindow(self.window_2, -1, style=wx.CLIP_CHILDREN)
        self.window_3_pane_2 = wx.Panel(self.window_3, -1)
        self.window_3_pane_1 = wx.Panel(self.window_3, -1)
        self.window_2_pane_1 = wx.Panel(self.window_2, -1)
        self.sizer_20_staticbox = wx.StaticBox(self.window_3_pane_1, -1, "vaccs scheduled")
        self.sizer_18_staticbox = wx.StaticBox(self.window_1_pane_1, -1, "Vacc Regimes -  X  selected ,  O - not selected")
        self.sizer_19_staticbox = wx.StaticBox(self.window_1_pane_2, -1, "vaccinations in selected regimes")
        self.sizer_21_staticbox = wx.StaticBox(self.window_2_pane_1, -1, "Vacc Given")
        self.list_ctrl_1 = wx.ListCtrl(self.window_2_pane_1, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.tree_ctrl_2 = wx.TreeCtrl(self.window_3_pane_1, -1, style=wx.TR_HAS_BUTTONS|wx.TR_NO_LINES|wx.TR_HIDE_ROOT|wx.TR_DEFAULT_STYLE|wx.SUNKEN_BORDER)
        self.label_2 = wx.StaticText(self.window_3_pane_1, -1, "vaccinations given")
        self.list_box_1 = wx.ListBox(self.window_3_pane_1, -1, choices=[])
        self.label_3 = wx.StaticText(self.window_3_pane_2, -1, "date")
        self.combo_box_1 = wx.ComboBox(self.window_3_pane_2, -1, choices=[], style=wx.CB_DROPDOWN)
        self.checkbox_1 = wx.CheckBox(self.window_3_pane_2, -1, "mark schedule\nupto current age")
        self.label_9 = wx.StaticText(self.window_3_pane_2, -1, "narrative")
        self.text_ctrl_1 = wx.TextCtrl(self.window_3_pane_2, -1, "", style=wx.TE_MULTILINE)
        self.label_4 = wx.StaticText(self.window_3_pane_2, -1, "vacc")
        self.checkbox_dtpa = wx.CheckBox(self.window_3_pane_2, -1, "DTPa")
        self.checkbox_2_ipv = wx.CheckBox(self.window_3_pane_2, -1, "IPV")
        self.checkbox_paed_hepb = wx.CheckBox(self.window_3_pane_2, -1, "paed HepB")
        self.checkbox_hib = wx.CheckBox(self.window_3_pane_2, -1, "HIB")
        self.checkbox_7pneumo = wx.CheckBox(self.window_3_pane_2, -1, "7VPneumo")
        self.checkbox_varicella = wx.CheckBox(self.window_3_pane_2, -1, "varicella")
        self.checkbox_mmr = wx.CheckBox(self.window_3_pane_2, -1, "MMR")
        self.checkbox_mening_c = wx.CheckBox(self.window_3_pane_2, -1, "mening-C")
        self.checkbox_tick_enceph = wx.CheckBox(self.window_3_pane_2, -1, "tick-borne encephalitis")
        self.static_line_1 = wx.StaticLine(self.window_3_pane_2, -1)
        self.checkbox_opv = wx.CheckBox(self.window_3_pane_2, -1, "OPV")
        self.label_8 = wx.StaticText(self.window_3_pane_2, -1, "  not listed", style=wx.ALIGN_RIGHT)
        self.combo_box_3 = wx.ComboBox(self.window_3_pane_2, -1, choices=[], style=wx.CB_DROPDOWN)
        self.checkbox_Dtpa = wx.CheckBox(self.window_3_pane_2, -1, "Dtpa( less antigen, >3prev)")
        self.checkbox_ADT = wx.CheckBox(self.window_3_pane_2, -1, "ADT")
        self.checkbox_tettox = wx.CheckBox(self.window_3_pane_2, -1, "Tet Tox")
        self.static_line_2 = wx.StaticLine(self.window_3_pane_2, -1)
        self.checkbox_23vpneum = wx.CheckBox(self.window_3_pane_2, -1, "23VPneum")
        self.checkbox_influenza = wx.CheckBox(self.window_3_pane_2, -1, "influenza")
        self.static_line_3 = wx.StaticLine(self.window_3_pane_2, -1)
        self.checkbox_paed_hepa = wx.CheckBox(self.window_3_pane_2, -1, "paed HepA")
        self.checkbox_adult_hepa = wx.CheckBox(self.window_3_pane_2, -1, "adult HepA")
        self.checkbox_adult_hepb = wx.CheckBox(self.window_3_pane_2, -1, "adult HepB")
        self.checkbox_typhoid = wx.CheckBox(self.window_3_pane_2, -1, "typhoid")
        self.checkbox_mening_acwy = wx.CheckBox(self.window_3_pane_2, -1, "mening-ACWY")
        self.checkbox_yellow_fever = wx.CheckBox(self.window_3_pane_2, -1, "yellow fever")
        self.checkbox_cholera = wx.CheckBox(self.window_3_pane_2, -1, "cholera")
        self.static_line_4 = wx.StaticLine(self.window_3_pane_2, -1)
        self.checkbox_rabies = wx.CheckBox(self.window_3_pane_2, -1, "rabies")
        self.checkbox_japan_enceph = wx.CheckBox(self.window_3_pane_2, -1, "Japanese Enceph")
        self.checkbox_qfever = wx.CheckBox(self.window_3_pane_2, -1, "Q Fever")
        self.label_5 = wx.StaticText(self.window_3_pane_2, -1, "batch no")
        self.combo_box_2 = wx.ComboBox(self.window_3_pane_2, -1, choices=[], style=wx.CB_DROPDOWN)
        self.checkbox_18 = wx.CheckBox(self.window_3_pane_2, -1, "save batch no")
        self.button_2 = wx.Button(self.window_3_pane_2, -1, "delete this no")
        self.label_6 = wx.StaticText(self.window_3_pane_2, -1, "site")
        self.radio_box_side = wx.RadioBox(self.window_3_pane_2, -1, "side", choices=["left", "right"], majorDimension=0, style=wx.RA_SPECIFY_COLS)
        self.radio_box_site = wx.RadioBox(self.window_3_pane_2, -1, "site", choices=["thigh", "deltoid", "gluteal"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_route = wx.RadioBox(self.window_3_pane_2, -1, "route", choices=["im", "sc", "po"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.button_1 = wx.Button(self.window_3_pane_2, -1, "add vaccination /\nnarrative / override", style=wx.BU_RIGHT)
        self.tree_ctrl_1 = wx.TreeCtrl(self.window_1_pane_1, -1, style=wx.TR_HAS_BUTTONS|wx.TR_NO_LINES|wx.TR_HIDE_ROOT|wx.TR_DEFAULT_STYLE|wx.SUNKEN_BORDER)
        self.list_ctrl_2 = wx.ListCtrl(self.window_1_pane_2, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_LIST_DELETE_ITEM, self.delete_vacc_history_item, self.list_ctrl_1)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.vacc_history_item_activated, self.list_ctrl_1)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.double_clicked_vaccination_given, self.list_box_1)
        self.Bind(wx.EVT_TEXT, self.date_being_entered, self.combo_box_1)
        self.Bind(wx.EVT_COMBOBOX, self.select_combo_date, self.combo_box_1)
        self.Bind(wx.EVT_TEXT, self.narrative_text, self.text_ctrl_1)
        self.Bind(wx.EVT_CHECKBOX, self.combo_with_hep_b_selected, self.checkbox_hib)
        self.Bind(wx.EVT_TEXT, self.unlisted_text_changed, self.combo_box_3)
        self.Bind(wx.EVT_COMBOBOX, self.unlisted_combo_selected, self.combo_box_3)
        self.Bind(wx.EVT_TEXT, self.check_for_similiar_batchno, self.combo_box_2)
        self.Bind(wx.EVT_COMBOBOX, self.get_batchno_for_vacc, self.combo_box_2)
        self.Bind(wx.EVT_BUTTON, self.delete_this_batchno, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.add_vaccination, self.button_1)
        self.Bind(wx.EVT_TREE_DELETE_ITEM, self.deleting_node, self.tree_ctrl_1)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.activating_node, self.tree_ctrl_1)
        # end wxGlade

	# gnumed events
	gmDispatcher.connect(signal = u'post_patient_selection', receiver=self._on_post_patient_selection)


    def __set_properties(self):
        # begin wxGlade: cAU_VaccV01Panel.__set_properties
        self.list_box_1.SetMinSize((145, 63))
        self.combo_box_1.SetSelection(-1)
        self.checkbox_1.SetFont(wx.Font(6, wx.MODERN, wx.NORMAL, wx.LIGHT, 0, ""))
        self.combo_box_3.SetSelection(-1)
        self.combo_box_2.SetSelection(-1)
        self.radio_box_side.SetSelection(0)
        self.radio_box_site.SetSelection(0)
        self.radio_box_route.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: cAU_VaccV01Panel.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_17 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_19 = wx.StaticBoxSizer(self.sizer_19_staticbox, wx.HORIZONTAL)
        sizer_18 = wx.StaticBoxSizer(self.sizer_18_staticbox, wx.HORIZONTAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_25 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1 = wx.FlexGridSizer(6, 2, 0, 0)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_16 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_22 = wx.BoxSizer(wx.VERTICAL)
        sizer_24 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_20 = wx.StaticBoxSizer(self.sizer_20_staticbox, wx.HORIZONTAL)
        sizer_21 = wx.StaticBoxSizer(self.sizer_21_staticbox, wx.HORIZONTAL)
        sizer_21.Add(self.list_ctrl_1, 1, wx.EXPAND, 0)
        self.window_2_pane_1.SetAutoLayout(True)
        self.window_2_pane_1.SetSizer(sizer_21)
        sizer_21.Fit(self.window_2_pane_1)
        sizer_21.SetSizeHints(self.window_2_pane_1)
        sizer_20.Add(self.tree_ctrl_2, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_20, 1, wx.EXPAND, 0)
        sizer_3.Add(self.label_2, 0, wx.ADJUST_MINSIZE, 0)
        sizer_3.Add(self.list_box_1, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_24.Add(sizer_3, 1, wx.EXPAND, 0)
        self.window_3_pane_1.SetAutoLayout(True)
        self.window_3_pane_1.SetSizer(sizer_24)
        sizer_24.Fit(self.window_3_pane_1)
        sizer_24.SetSizeHints(self.window_3_pane_1)
        grid_sizer_1.Add(self.label_3, 0, wx.ADJUST_MINSIZE, 0)
        sizer_22.Add(self.combo_box_1, 0, wx.ADJUST_MINSIZE, 0)
        sizer_22.Add(self.checkbox_1, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_2.Add(sizer_22, 0, wx.EXPAND, 0)
        sizer_16.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_16.Add(self.label_9, 0, wx.ADJUST_MINSIZE, 0)
        sizer_16.Add(self.text_ctrl_1, 1, wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(sizer_16, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_4, 0, wx.ADJUST_MINSIZE, 0)
        sizer_6.Add(self.checkbox_dtpa, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 19)
        sizer_6.Add(self.checkbox_2_ipv, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 26)
        sizer_6.Add(self.checkbox_paed_hepb, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 20)
        sizer_6.Add(self.checkbox_hib, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 12)
        sizer_6.Add(self.checkbox_7pneumo, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 12)
        sizer_5.Add(sizer_6, 0, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_7.Add(self.checkbox_varicella, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 17)
        sizer_7.Add(self.checkbox_mmr, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 16)
        sizer_7.Add(self.checkbox_mening_c, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 16)
        sizer_7.Add(self.checkbox_tick_enceph, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 16)
        sizer_5.Add(sizer_7, 0, wx.EXPAND, 0)
        sizer_5.Add(self.static_line_1, 0, wx.EXPAND, 0)
        sizer_15.Add(self.checkbox_opv, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 23)
        sizer_15.Add(self.label_8, 0, wx.ALIGN_RIGHT|wx.ADJUST_MINSIZE, 0)
        sizer_15.Add(self.combo_box_3, 1, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_5.Add(sizer_15, 0, wx.EXPAND, 0)
        sizer_8.Add(self.checkbox_Dtpa, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 20)
        sizer_8.Add(self.checkbox_ADT, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 14)
        sizer_8.Add(self.checkbox_tettox, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 14)
        sizer_5.Add(sizer_8, 0, wx.EXPAND, 0)
        sizer_5.Add(self.static_line_2, 0, wx.EXPAND, 0)
        sizer_9.Add(self.checkbox_23vpneum, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 12)
        sizer_9.Add(self.checkbox_influenza, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 20)
        sizer_5.Add(sizer_9, 0, wx.EXPAND, 0)
        sizer_5.Add(self.static_line_3, 0, wx.EXPAND, 0)
        sizer_10.Add(self.checkbox_paed_hepa, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 20)
        sizer_10.Add(self.checkbox_adult_hepa, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 18)
        sizer_10.Add(self.checkbox_adult_hepb, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 20)
        sizer_5.Add(sizer_10, 0, wx.EXPAND, 0)
        sizer_12.Add(self.checkbox_typhoid, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 26)
        sizer_12.Add(self.checkbox_mening_acwy, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 20)
        sizer_12.Add(self.checkbox_yellow_fever, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 20)
        sizer_12.Add(self.checkbox_cholera, 0, wx.ADJUST_MINSIZE, 20)
        sizer_5.Add(sizer_12, 0, wx.EXPAND, 0)
        sizer_5.Add(self.static_line_4, 0, wx.EXPAND, 0)
        sizer_13.Add(self.checkbox_rabies, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 23)
        sizer_13.Add(self.checkbox_japan_enceph, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 15)
        sizer_13.Add(self.checkbox_qfever, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 18)
        sizer_5.Add(sizer_13, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(sizer_5, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_5, 0, wx.ADJUST_MINSIZE, 0)
        sizer_11.Add(self.combo_box_2, 1, wx.ADJUST_MINSIZE, 0)
        sizer_11.Add(self.checkbox_18, 0, wx.ADJUST_MINSIZE, 0)
        sizer_11.Add(self.button_2, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(sizer_11, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_6, 0, wx.ADJUST_MINSIZE, 0)
        sizer_4.Add(self.radio_box_side, 0, wx.ADJUST_MINSIZE, 0)
        sizer_4.Add(self.radio_box_site, 0, wx.ADJUST_MINSIZE, 0)
        sizer_4.Add(self.radio_box_route, 0, wx.ADJUST_MINSIZE, 0)
        sizer_4.Add(self.button_1, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE|wx.FIXED_MINSIZE, 0)
        grid_sizer_1.Add(sizer_4, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, wx.ADJUST_MINSIZE, 0)
        sizer_25.Add(grid_sizer_1, 0, wx.EXPAND, 0)
        self.window_3_pane_2.SetAutoLayout(True)
        self.window_3_pane_2.SetSizer(sizer_25)
        sizer_25.Fit(self.window_3_pane_2)
        sizer_25.SetSizeHints(self.window_3_pane_2)
        self.window_3.SplitVertically(self.window_3_pane_1, self.window_3_pane_2)
        self.window_2.SplitHorizontally(self.window_2_pane_1, self.window_3, 10)
        sizer_14.Add(self.window_2, 1, wx.EXPAND, 0)
        self.notebook_1_pane_1.SetAutoLayout(True)
        self.notebook_1_pane_1.SetSizer(sizer_14)
        sizer_14.Fit(self.notebook_1_pane_1)
        sizer_14.SetSizeHints(self.notebook_1_pane_1)
        sizer_18.Add(self.tree_ctrl_1, 1, wx.EXPAND, 0)
        self.window_1_pane_1.SetAutoLayout(True)
        self.window_1_pane_1.SetSizer(sizer_18)
        sizer_18.Fit(self.window_1_pane_1)
        sizer_18.SetSizeHints(self.window_1_pane_1)
        sizer_19.Add(self.list_ctrl_2, 1, wx.EXPAND, 0)
        self.window_1_pane_2.SetAutoLayout(True)
        self.window_1_pane_2.SetSizer(sizer_19)
        sizer_19.Fit(self.window_1_pane_2)
        sizer_19.SetSizeHints(self.window_1_pane_2)
        self.window_1.SplitHorizontally(self.window_1_pane_1, self.window_1_pane_2)
        sizer_17.Add(self.window_1, 1, wx.EXPAND, 0)
        self.notebook_1_pane_2.SetAutoLayout(True)
        self.notebook_1_pane_2.SetSizer(sizer_17)
        sizer_17.Fit(self.notebook_1_pane_2)
        sizer_17.SetSizeHints(self.notebook_1_pane_2)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "vaccinations")
        self.notebook_1.AddPage(self.notebook_1_pane_2, "enrolled vaccinations")
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        # end wxGlade

    def delete_vacc_history_item(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `delete_vacc_history_item' not implemented"
        event.Skip()

    def vacc_history_item_activated(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `vacc_history_item_activated' not implemented"
        event.Skip()

    def recommended_vacc_given(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `recommended_vacc_given' not implemented"
        event.Skip()

    def recommended_vacc_selected(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `recommended_vacc_selected' not implemented"
        event.Skip()

    def double_clicked_vaccination_given(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `double_clicked_vaccination_given' not implemented"
        event.Skip()

    def date_being_entered(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `date_being_entered' not implemented"
        event.Skip()

    def select_combo_date(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `select_combo_date' not implemented"
        event.Skip()

    def combo_with_hep_b_selected(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `combo_with_hep_b_selected' not implemented"
        event.Skip()

    def unlisted_text_changed(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `unlisted_text_changed' not implemented"
        event.Skip()

    def unlisted_combo_selected(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `unlisted_combo_selected' not implemented"
        event.Skip()

    def check_for_similiar_batchno(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `check_for_similiar_batchno' not implemented"
        event.Skip()

    def get_batchno_for_vacc(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `get_batchno_for_vacc' not implemented"
        event.Skip()

    def delete_this_batchno(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `delete_this_batchno' not implemented"
        event.Skip()
	
    def add_vaccination(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `add_vaccination' not implemented"
        event.Skip() 
	l = [	self.checkbox_dtpa.GetValue(),
		self.checkbox_2_ipv .GetValue(),      
		self.checkbox_paed_hepb.GetValue(),
		self.checkbox_hib.GetValue(),        
		self.checkbox_7pneumo .GetValue(),
		self.checkbox_varicella.GetValue(),
		self.checkbox_mmr .GetValue(),
		self.checkbox_mening_c .GetValue(),
		self.checkbox_tick_enceph .GetValue(),      
		self.checkbox_opv .GetValue(),
		self.checkbox_Dtpa.GetValue(),
		self.checkbox_ADT.GetValue(),
		self.checkbox_tettox.GetValue(),
		self.checkbox_23vpneum.GetValue(),
		self.checkbox_influenza  .GetValue(),
		self.checkbox_paed_hepa.GetValue(),
		self.checkbox_adult_hepa.GetValue(),
		self.checkbox_adult_hepb.GetValue(),
		self.checkbox_typhoid.GetValue(),
		self.checkbox_mening_acwy.GetValue(),
		self.checkbox_yellow_fever.GetValue(),
		self.checkbox_cholera.GetValue(),
		self.checkbox_rabies.GetValue(),
		self.checkbox_japan_enceph.GetValue(),
		self.checkbox_qfever.GetValue()

		]
	[dtp , ipv,  phb ,hib,  p7, var, mmr, mc, tick, opv, dTpa, adt, tt, p23, flu, pha, aha, ahb, ty, acwy, yf, chol, rab, jap, qf ] = l
	
	# nb the indication strings must be identical if the same indication
	# so 'pol' and 'polio' are not allowed
	
	
	to_ind = zip ( [ ('diph','tet', 'pert'),('polio',), ( 'hepatitis B',), ('haemophilus',), ('pneum',), ('varicella',), ( 'measles','mumps', 'rubella'), ('meningococcus C',), ('tick',), ('polio',), ('diph', 'tet', 'pert'), ('diph','tet'), ('tet',), ('pneum',), ('influ',), ('hepatitis A',), ('hepatitis A',), ('hepatitis B',), ('typhoid',), ('meningococcus ACWY',), ('yellow fever',), ('cholera',), ('rabies',), ('japanese enc',), ('Q fever',) ], l )
	for i , c in to_ind:
		print "DEBUG to_ind ", i, c
	def get_unique_indications ( indset_chosen_list):
		"""indset_chosen_list is a list of 2-tuples, 
			the 2-tuple is a tuple of indications, and a boolean value 'chosen'
		
		   returns matching vaccines that have all the indications chosen

		   usage: a tuple of indications can represent a combo vaccine's set of indications. 
		"""
		all_ind = [] 
		for ind, chosen in to_ind:
			if chosen:
				for x in ind:
					if x not in all_ind:
						all_ind.append(x)
		return all_ind 
	all_ind = get_unique_indications ( to_ind)
	#import pdb
	#pdb.set_trace()
	vaccines = gmVaccination.get_matching_vaccines_for_indications(all_ind)

	nchecked = len( [ x for x in l if x] )
	
	
	class NoVaccChosen ( Exception):
		pass
	class IllegalCombo (Exception):
		pass
	
	def _or(x, y):
		return x or y
	
	try:
		
		# can replace this with dynamic checking of vaccine and lnk_vaccine2ind
#		
#		if nchecked == 0:
#			raise NoVaccChosen, _('No vaccine was selected')
#			
#		elif nchecked == 1:
#			pass # ok single vaccine 
#		
#		
#		elif nchecked == 2 and dtp and not ipv:
#			raise IllegalCombo, _('only binary vaccine with dtp is with ipv')
#		
#		elif nchecked == 3 and dtp and not ipv and not hepb :
#			raise IllegalCombo, _('Illegal combination not recognized')
#		
#		elif nchecked == 4 and dtp and not ipv and not hepb and not hib:
#			raise IllegalCombo, _('5 dtp vaccine combo is with IPV and hep B and HIB')
#		
#
#		
#		elif nchecked == 2 and hib and not  ipv and not phb :
#			raise IllegalCombo, _('hib combo with ipv or paed hep B only')
#
#		elif nchecked == 2 and phb and not pha and not ty:
#			raise IllegalCombo, _('paed hep b only with paed hep a or hib or typhoid ')
#
#		elif nchecked == 2 and aha and not ty and  not ahb:
#			raise IllegalCombo, _('adult hep A only in combo with typhoid or adult hep b')
#		else:
#			raise IllegalCombo, _('unrecognized combined vaccination')
#			
		if not nchecked:
			raise NoVaccChosen, _("No vaccines were chosen")
		if not len(vaccines):
			raise IllegalCombo, _("Combination of indications , %s , not found in any vaccine" % ', '.join ( all_ind) )
	except NoVaccChosen, s:
		wx.MessageDialog( self, str(s), style = wx.OK).ShowModal()
		return 
		
	except IllegalCombo , s:
		wx.MessageDialog( self, str(s), style = wx.OK).ShowModal()
		return 

	wx.MessageDialog( self,"Accepted add", style = wx.OK).ShowModal()
	

    def _on_post_patient_selection(self):
    
    	self._populate_vaccination_history_list()
    	self._populate_vacc_regime_tree()
    	self._populate_missing_vaccinations()
			
    def _populate_vaccination_history_list(self):
    	# populate vaccination history
    	print self, "got on patient selected"
	p = gmPerson.gmCurrentPatient()	
	emr = p.get_emr()
	vv = emr.get_vaccinations()
	l = self.list_ctrl_1
	l.ClearAll()
	cols =  [ _('Date'), _('Vaccine'), _('Sequence'), _('Batch'), _('Site'), _('Narrative'), _('Vaccinator') ]
	for c, i in zip(cols, range(len(cols)) ):
		l.InsertColumn( i, c)
	
	fields = [ 'date', 'vaccine', 'seq_no', 'batch_no', 'site', 'narrative', 'pk_provider' ]
	for v, i  in zip( vv, range(len(vv))):
		for f, j in zip(fields,range(len(fields)) ):	
			if j == 0:
				l.InsertStringItem( i,  str(v[f])) 
			else:
				l.SetStringItem(i, j, str(v[f]) )
	
	for i in range(len(cols)):
		l.SetColumnWidth( i, wx.LIST_AUTOSIZE)
		w1 = l.GetColumnWidth(i)
		l.SetColumnWidth( i, wx.LIST_AUTOSIZE_USEHEADER)
		w2 = l.GetColumnWidth(i)
		if w1 > w2:
			l.SetColumnWidth(i, w1)
			
			
    	#print vv
	#import pdb
	#pdb.set_trace)
    def _update_age_ordered_vacc_tree( self, t, v, rec_node, age_node, last_min_age):
			s = '#'+str(v['seq_no'])+ ' : ' + v['regime'] 
			s += '; min age due = ' +  stringify_days( v['min_age_due']) 
		
			s += ' ; min interval: ' + stringify_days(v['min_interval'])
								
			if v['min_age_due'] != last_min_age:
				
				age_node = t.AppendItem(  rec_node, 'Minimum age due : ' + stringify_days(v['min_age_due']) )
				last_min_age = v['min_age_due']
			
			
			def_node = t.AppendItem( age_node, s, data = wx.TreeItemData( v) )
                        return t, v, age_node, last_min_age, def_node
	
    def _populate_vacc_regime_tree(self):
	# populate vacc regime choice tree
	p = gmPerson.gmCurrentPatient()	
	self._vreg, self._active_recs = gmVaccination.get_vacc_regimes_by_recommender_ordered( int ( p.ID ) )
	vreg = self._vreg
	t = self.tree_ctrl_1
	t.DeleteAllItems()
	root = t.AddRoot( _('Vaccinations by Recommender (X = patient on regime, O = patient not on regime) ') )
	
	self._rec_nodes = []
	for recommender in vreg[1]:
		
		
		rec_node = t.AppendItem( root, str(recommender) , data = wx.TreeItemData(recommender) )	
		self._rec_nodes .append(rec_node)
		
		last_min_age = -1
		age_node = None

		on_rec = False
		
		for v in vreg[0][recommender]:
			t, v, age_node, last_min_age, def_node = self._update_age_ordered_vacc_tree( t, v, rec_node, age_node, last_min_age)
		
			if int(v['pk_regime']) in self._active_recs:		
		
				marker = ' - x'
				colour = wx.GREEN
			else:
				marker = ' - O'
				colour = wx.RED
				
			t.SetItemText( def_node, t.GetItemText(def_node) + marker)
			t.SetItemTextColour( def_node, colour)
	expand_tree(t, root , 2)
    
    def _populate_missing_vaccinations(self):
    	t = self.tree_ctrl_2
	t.DeleteAllItems()
    	p = gmPerson.gmCurrentPatient()	
	emr = p.get_emr()
	mv = gmVaccination.get_missing_vaccinations_ordered_min_due( p.ID )
	lmv = [ dict( [ (field, v[i] ) for field, i  in zip(
		['indication', 'regime', 
		'pk_regime', 
		'pk_recommended_by', 
		'seq_no' , 
		'min_age_due', 
		'max_age_due',
		'min_interval' ] , range( len(v) ) ) ] ) for v in mv ]
	
	age_node, last_min_age = None, -1
	root = t.AddRoot(_('enrolled regime vaccinations not yet given') )
	for v in lmv:
		t, v, age_node, last_min_age, def_node = self._update_age_ordered_vacc_tree( t, v, root, age_node, last_min_age) 
	expand_tree(t, root, 2)
		
	print "DEBUG missing vaccs len=", len(mv)
	#for  x in mv:
	#	print x
	#import pdb
	#pbd.set_trace()
	
    def narrative_text(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `narrative_text' not implemented"
        event.Skip()

    def deleting_node(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `deleting_node' not implemented"
        event.Skip()

    def activating_node(self, event): # wxGlade: cAU_VaccV01Panel.<event_handler>
        print "Event handler `activating_node' not implemented"
	n = event.GetItem()

        event.Skip(1)
	t = self.tree_ctrl_1
	#import pdb
	#pdb.set_trace()
	
	if n in self._rec_nodes:
		recommender = t.GetItemData( n).GetData()
		active = True
		for v in self._vreg[0][recommender]:
			if not v['pk_regime'] in self._active_recs:
				active = False
				break

		if active:
			msg = " unenrolling in the selected recommenders' regimes ( will fail if any vaccinations linked to regime)"
		else:
			msg = "enroll in regime of recommender " + str( recommender) 
			
		answ = wx.MessageDialog(self, _("Proceed with " + msg + "?")).ShowModal()
		failures = []
		success = []
		#import pdb
		#pdb.set_trace()
		if answ == wx.ID_OK and not active:
			for v in self._vreg[0][recommender]:
				result = False
				id = gmPerson.gmCurrentPatient().ID
				if v['pk_regime'] in success:
					continue
				if id:
					result,msg = gmVaccination.put_patient_on_schedule(id, v['pk_regime'])
				if not result:
					failures.append(v)
				else:
					success.append(v['pk_regime'])
			if len(failures):
				wx.MessageDialog(self, _("Failed to enrol patient in %s") % ',  '.join( [ f['regime'] for f in failures] ) , style = wx.OK  ).ShowModal()
				
		if answ == wx.ID_OK and active:
			for v in self._vreg[0][recommender]:
				result = False
				id = gmPerson.gmCurrentPatient().ID
				if v['pk_regime'] in success:
					continue
				if id:
					result,msg = gmVaccination.remove_patient_from_schedule(id, v['pk_regime'])
				if not result:
					failures.append(v)
				else:
					success.append(v['pk_regime'])
			if len(failures):
				wx.MessageDialog(self, _("Failed to  delist patient from %s") % ',  '.join( [ f['regime'] for f in failures] ) , style = wx.OK  ).ShowModal()
	
	self._on_post_patient_selection()
		
# end of class cAU_VaccV01Panel


