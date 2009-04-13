#!/usr/bin/env python
# -*- coding: utf8 -*-
# generated by wxGlade HG on Thu Apr  9 10:01:05 2009

import wx

# begin wxGlade: extracode
# end wxGlade

class wxgCardiacDevicePluginPnl(wx.ScrolledWindow):
    def __init__(self, *args, **kwds):

	from Gnumed.wxpython.gmNarrativeWidgets import cSoapNoteInputNotebook
        from Gnumed.wxpython.gmDateTimeInput import cFuzzyTimestampInput
        from Gnumed.wxpython.gmEMRStructWidgets import cEncounterTypePhraseWheel
        from Gnumed.wxpython import gmListWidgets

        # begin wxGlade: wxgCardiacDevicePluginPnl.__init__
        kwds["style"] = wx.NO_BORDER|wx.TAB_TRAVERSAL
        wx.ScrolledWindow.__init__(self, *args, **kwds)
        self._splitter_main = wx.SplitterWindow(self, -1, style=wx.SP_3D|wx.SP_BORDER|wx.SP_PERMIT_UNSPLIT)
        self.__splitter_main_right_pnl = wx.Panel(self._splitter_main, -1, style=wx.NO_BORDER)
        self._splitter_right = wx.SplitterWindow(self.__splitter_main_right_pnl, -1, style=wx.SP_3D|wx.SP_BORDER|wx.SP_PERMIT_UNSPLIT)
        self.__splitter_right_bottom_pnl = wx.ScrolledWindow(self._splitter_right, -1, style=wx.NO_BORDER)
        self.__splitter_right_top_pnl = wx.Panel(self._splitter_right, -1, style=wx.NO_BORDER)
        self._NB_device_editors = cSoapNoteInputNotebook(self.__splitter_right_top_pnl, -1, style=0)
        self.__splitter_main_left_pnl = wx.Panel(self._splitter_main, -1, style=wx.NO_BORDER|wx.FULL_REPAINT_ON_RESIZE)
        self.__splitter_left_bottom_pnl = wx.Panel(self.__splitter_main_left_pnl, -1, style=wx.NO_BORDER)
        self.__splitter_left_middle_pnl = wx.Panel(self.__splitter_main_left_pnl, -1, style=wx.NO_BORDER)
        self.__splitter_left_top_pnl = wx.Panel(self.__splitter_main_left_pnl, -1)
        self.__szr_middle_left_staticbox = wx.StaticBox(self.__splitter_left_middle_pnl, -1, _("Active Problems"))
        self.__szr_bottom_left_staticbox = wx.StaticBox(self.__splitter_left_bottom_pnl, -1, _("Most Recent Related Notes"))
        self.__szr_top_right_staticbox = wx.StaticBox(self.__splitter_right_top_pnl, -1, _("New notes in current encounter"))
        self.__szr_bottom_right_staticbox = wx.StaticBox(self.__splitter_right_bottom_pnl, -1, _("Tips and Hints"))
        self.__szr_top_left_staticbox = wx.StaticBox(self.__splitter_left_top_pnl, -1, _("Active Device Settings"))
        self._TCTRL_current_status = wx.TextCtrl(self.__splitter_left_top_pnl, -1, _("In this area GNUmed will place the status of all cardiac devices and device parts. There can be more than one device at a time\n\nIt potentially looks like this\n----------------------------------------------------------------------------------------------------------------\nDevice: SJM Atlas DR (active)     Battery: 2.4V (MOL)      Implanted:  Feb 09 2008\n\nRA: Medtronic Sprint fidelis (active, flaky, replacement)             Implanted: Feb 09 2008\nSensing: 2 (1.5) mV    Threshold: 0.7/0.5 (1/0.4) V/ms       Impedance: 800 (900) Ohm\n\nRV: Medtronic Sprint fidelis (active, flaky, replacement)             Implanted: Feb 09 2008\nSensing: 7 (15) mV    Threshold: 0.7/0.5 (1/0.4) V/ms       Impedance: 800 (900) Ohm\n\nLV: Medtronic Sprint fidelis (active, flaky, Y-connector)             Implanted: Feb 09 2008\nSensing: 7 ( ?) mV    Threshold: 1/1.5 (1/1) V/ms       Impedance: 800 (900) Ohm\n----------------------------------------------------------------------------------------------------------------\nDevice: Medtronic Relia SR (inactive)     Batttery 2.1V (EOL)   Implanted: Jan 23 2000\n\nDevice: Medtronic Kappa SR (explanted)     Batttery 2.1V (EOL)   Explanted: Jan 23 2000 (Jan 23 1995)\n-----------------------------------------------------------------------------------------------------------------\nRA Lead: Medtronic ? (inactive, capped)             Implanted: Jan 23 2000\nRV Lead: Medtronic ? (explanted)                        Explanted: Feb 09 2008"), style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP|wx.NO_BORDER)
        self._LCTRL_active_problems = gmListWidgets.cReportListCtrl(self.__splitter_left_middle_pnl, -1, style=wx.LC_REPORT|wx.NO_BORDER|wx.FULL_REPAINT_ON_RESIZE)
        self._TCTRL_recent_notes = wx.TextCtrl(self.__splitter_left_bottom_pnl, -1, _("In this area GNUmed will place the notes of the\nprevious encounter as well as notes by other\nstaff for the current encounter.\n\nNote that this may change depending on which\nactive problem is selected in the editor below."), style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP|wx.NO_BORDER)
        self._PRW_encounter_type = cEncounterTypePhraseWheel(self.__splitter_right_top_pnl, -1, "", style=wx.NO_BORDER)
        self._PRW_encounter_start = cFuzzyTimestampInput(self.__splitter_right_top_pnl, -1, "", style=wx.NO_BORDER)
        self._PRW_encounter_end = cFuzzyTimestampInput(self.__splitter_right_top_pnl, -1, "", style=wx.NO_BORDER)
        self._BTN_new_encounter = wx.Button(self.__splitter_right_top_pnl, -1, _("New"), style=wx.BU_EXACTFIT)
        self._TCTRL_rfe = wx.TextCtrl(self.__splitter_right_top_pnl, -1, "", style=wx.NO_BORDER)
        self.notebook_1_pane_1 = wx.Panel(self._NB_device_editors, -1)
        self._TCTRL_aoe = wx.TextCtrl(self.__splitter_right_top_pnl, -1, "", style=wx.NO_BORDER)
        self._BTN_save_all = wx.Button(self.__splitter_right_top_pnl, -1, _("&All"), style=wx.BU_EXACTFIT)
        self._BTN_save_encounter = wx.Button(self.__splitter_right_top_pnl, -1, _("&Encounter"), style=wx.BU_EXACTFIT)
        self._BTN_save_note = wx.Button(self.__splitter_right_top_pnl, -1, _("&Note"), style=wx.BU_EXACTFIT)
        self._BTN_new_editor = wx.Button(self.__splitter_right_top_pnl, -1, _("&New"), style=wx.BU_EXACTFIT)
        self._BTN_clear_editor = wx.Button(self.__splitter_right_top_pnl, -1, _("&Clear"), style=wx.BU_EXACTFIT)
        self._BTN_discard_editor = wx.Button(self.__splitter_right_top_pnl, -1, _("&Discard"), style=wx.BU_EXACTFIT)
        self._lbl_hints = wx.StaticText(self.__splitter_right_bottom_pnl, -1, _("In this area GNUmed will place hints and tips\nrelated to the current interrogation note and patient.\n\nThose hints will be derived from a variety of\nsources such as classifications (ICD, ...), \nsafety warnings, online resources (Google\nand friends), device databases, etc.\n\nEventually, those hints will be active in that you\ncan click on them and be taken to the relevant\ninformation/an appropriate action be performed."))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self._on_problem_activated, self._LCTRL_active_problems)
        self.Bind(wx.EVT_BUTTON, self._on_new_encounter_button_pressed, self._BTN_new_encounter)
        self.Bind(wx.EVT_BUTTON, self._on_save_all_button_pressed, self._BTN_save_all)
        self.Bind(wx.EVT_BUTTON, self._on_save_encounter_button_pressed, self._BTN_save_encounter)
        self.Bind(wx.EVT_BUTTON, self._on_save_note_button_pressed, self._BTN_save_note)
        self.Bind(wx.EVT_BUTTON, self._on_new_editor_button_pressed, self._BTN_new_editor)
        self.Bind(wx.EVT_BUTTON, self._on_clear_editor_button_pressed, self._BTN_clear_editor)
        self.Bind(wx.EVT_BUTTON, self._on_discard_editor_button_pressed, self._BTN_discard_editor)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxgCardiacDevicePluginPnl.__set_properties
        self.SetScrollRate(10, 10)
        self._TCTRL_current_status.Enable(False)
        self._LCTRL_active_problems.SetToolTipString(_("This shows the list of active problems, They include open episodes as well as active health issues."))
        self._TCTRL_recent_notes.Enable(False)
        self._PRW_encounter_type.SetToolTipString(_("Select the type of encounter."))
        self._PRW_encounter_start.SetToolTipString(_("Date and time when the current (!) encounter started."))
        self._PRW_encounter_end.SetToolTipString(_("Date and time when the current (!) encounter ends."))
        self._BTN_new_encounter.SetToolTipString(_("Start a new encounter. If there are any changes to the current encounter you will be asked whether to save them."))
        self._TCTRL_rfe.SetToolTipString(_("This documents why the encounter takes place.\n\nIt may be due to a patient request or it may be prompted by other reasons. Often initially collected at the front desk and put into a waiting list comment. May turn out to just be a proxy request for why the patient really is here.\n\nAlso known as the Reason For Encounter/Visit (RFE)."))
        self._TCTRL_aoe.SetToolTipString(_("This summarizes the outcome/assessment of the consultation from the doctors point of view. Note that this summary spans all the problems discussed during this encounter."))
        self._BTN_save_all.SetToolTipString(_("Save encounter details and all progress notes."))
        self._BTN_save_encounter.SetToolTipString(_("Save the encounter details."))
        self._BTN_save_note.SetToolTipString(_("Save the currently displayed progress note."))
        self._BTN_new_editor.SetToolTipString(_("Open a new progress note editor.\n\nThere is a configuration item on whether to allow several new-episode editors at once."))
        self._BTN_clear_editor.SetToolTipString(_("Clear the editor for the displayed progress note."))
        self._BTN_discard_editor.SetToolTipString(_("Discard the editor for the displayed progress note."))
        self.__splitter_right_bottom_pnl.SetScrollRate(10, 10)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxgCardiacDevicePluginPnl.__do_layout
        __szr_main = wx.BoxSizer(wx.HORIZONTAL)
        __szr_right = wx.BoxSizer(wx.VERTICAL)
        __szr_bottom_right = wx.StaticBoxSizer(self.__szr_bottom_right_staticbox, wx.VERTICAL)
        __szr_top_right = wx.StaticBoxSizer(self.__szr_top_right_staticbox, wx.VERTICAL)
        __szr_buttons = wx.BoxSizer(wx.HORIZONTAL)
        __szr_aoe = wx.BoxSizer(wx.HORIZONTAL)
        __gszr_encounter_details = wx.FlexGridSizer(2, 2, 2, 5)
        __szr_encounter_details = wx.BoxSizer(wx.HORIZONTAL)
        __szr_device_status = wx.BoxSizer(wx.VERTICAL)
        __szr_bottom_left = wx.StaticBoxSizer(self.__szr_bottom_left_staticbox, wx.VERTICAL)
        __szr_middle_left = wx.StaticBoxSizer(self.__szr_middle_left_staticbox, wx.VERTICAL)
        __szr_top_left = wx.StaticBoxSizer(self.__szr_top_left_staticbox, wx.VERTICAL)
        __szr_top_left.Add(self._TCTRL_current_status, 1, wx.EXPAND, 0)
        self.__splitter_left_top_pnl.SetSizer(__szr_top_left)
        __szr_device_status.Add(self.__splitter_left_top_pnl, 1, wx.EXPAND, 0)
        __szr_middle_left.Add(self._LCTRL_active_problems, 1, wx.EXPAND, 0)
        self.__splitter_left_middle_pnl.SetSizer(__szr_middle_left)
        __szr_device_status.Add(self.__splitter_left_middle_pnl, 0, wx.EXPAND, 0)
        __szr_bottom_left.Add(self._TCTRL_recent_notes, 1, wx.EXPAND, 0)
        self.__splitter_left_bottom_pnl.SetSizer(__szr_bottom_left)
        __szr_device_status.Add(self.__splitter_left_bottom_pnl, 0, wx.EXPAND, 0)
        self.__splitter_main_left_pnl.SetSizer(__szr_device_status)
        __lbl_encounter_details = wx.StaticText(self.__splitter_right_top_pnl, -1, _("Encounter"))
        __gszr_encounter_details.Add(__lbl_encounter_details, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_encounter_details.Add(self._PRW_encounter_type, 1, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 10)
        __szr_encounter_details.Add(self._PRW_encounter_start, 1, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        __lbl_until = wx.StaticText(self.__splitter_right_top_pnl, -1, _("until"))
        __szr_encounter_details.Add(__lbl_until, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_encounter_details.Add(self._PRW_encounter_end, 1, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_encounter_details.Add(self._BTN_new_encounter, 0, wx.EXPAND, 0)
        __gszr_encounter_details.Add(__szr_encounter_details, 1, wx.EXPAND, 0)
        __lbl_rfe = wx.StaticText(self.__splitter_right_top_pnl, -1, _("Request"))
        __gszr_encounter_details.Add(__lbl_rfe, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __gszr_encounter_details.Add(self._TCTRL_rfe, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __gszr_encounter_details.AddGrowableCol(1)
        __szr_top_right.Add(__gszr_encounter_details, 0, wx.RIGHT|wx.EXPAND, 3)
        self._NB_device_editors.AddPage(self.notebook_1_pane_1, _("tab1"))
        __szr_top_right.Add(self._NB_device_editors, 1, wx.RIGHT|wx.TOP|wx.EXPAND, 3)
        __lbl_aoe = wx.StaticText(self.__splitter_right_top_pnl, -1, _("Summary"))
        __szr_aoe.Add(__lbl_aoe, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_aoe.Add(self._TCTRL_aoe, 1, wx.RIGHT|wx.TOP|wx.BOTTOM|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_top_right.Add(__szr_aoe, 0, wx.RIGHT|wx.TOP|wx.EXPAND, 3)
        __lbl_save = wx.StaticText(self.__splitter_right_top_pnl, -1, _("Save:"))
        __szr_buttons.Add(__lbl_save, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_buttons.Add(self._BTN_save_all, 0, wx.RIGHT|wx.EXPAND, 3)
        __szr_buttons.Add(self._BTN_save_encounter, 0, wx.RIGHT|wx.EXPAND, 3)
        __szr_buttons.Add(self._BTN_save_note, 0, wx.EXPAND, 0)
        __szr_buttons.Add((1, 1), 1, 0, 0)
        __lbl_editor = wx.StaticText(self.__splitter_right_top_pnl, -1, _("Editor:"))
        __szr_buttons.Add(__lbl_editor, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_buttons.Add(self._BTN_new_editor, 0, wx.RIGHT|wx.EXPAND, 3)
        __szr_buttons.Add(self._BTN_clear_editor, 0, wx.RIGHT|wx.EXPAND, 3)
        __szr_buttons.Add(self._BTN_discard_editor, 0, wx.EXPAND, 0)
        __szr_buttons.Add((1, 1), 1, 0, 0)
        __szr_top_right.Add(__szr_buttons, 0, wx.RIGHT|wx.TOP|wx.EXPAND, 3)
        self.__splitter_right_top_pnl.SetSizer(__szr_top_right)
        __szr_bottom_right.Add(self._lbl_hints, 0, wx.EXPAND, 0)
        self.__splitter_right_bottom_pnl.SetSizer(__szr_bottom_right)
        self._splitter_right.SplitHorizontally(self.__splitter_right_top_pnl, self.__splitter_right_bottom_pnl)
        __szr_right.Add(self._splitter_right, 1, wx.EXPAND, 0)
        self.__splitter_main_right_pnl.SetSizer(__szr_right)
        self._splitter_main.SplitVertically(self.__splitter_main_left_pnl, self.__splitter_main_right_pnl)
        __szr_main.Add(self._splitter_main, 1, wx.EXPAND, 0)
        self.SetSizer(__szr_main)
        __szr_main.Fit(self)
        # end wxGlade

    def _on_problem_activated(self, event): # wxGlade: wxgCardiacDevicePluginPnl.<event_handler>
        print "Event handler `_on_problem_activated' not implemented!"
        event.Skip()

    def _on_new_encounter_button_pressed(self, event): # wxGlade: wxgCardiacDevicePluginPnl.<event_handler>
        print "Event handler `_on_new_encounter_button_pressed' not implemented!"
        event.Skip()

    def _on_save_all_button_pressed(self, event): # wxGlade: wxgCardiacDevicePluginPnl.<event_handler>
        print "Event handler `_on_save_all_button_pressed' not implemented!"
        event.Skip()

    def _on_save_encounter_button_pressed(self, event): # wxGlade: wxgCardiacDevicePluginPnl.<event_handler>
        print "Event handler `_on_save_encounter_button_pressed' not implemented!"
        event.Skip()

    def _on_save_note_button_pressed(self, event): # wxGlade: wxgCardiacDevicePluginPnl.<event_handler>
        print "Event handler `_on_save_note_button_pressed' not implemented!"
        event.Skip()

    def _on_new_editor_button_pressed(self, event): # wxGlade: wxgCardiacDevicePluginPnl.<event_handler>
        print "Event handler `_on_new_editor_button_pressed' not implemented!"
        event.Skip()

    def _on_clear_editor_button_pressed(self, event): # wxGlade: wxgCardiacDevicePluginPnl.<event_handler>
        print "Event handler `_on_clear_editor_button_pressed' not implemented!"
        event.Skip()

    def _on_discard_editor_button_pressed(self, event): # wxGlade: wxgCardiacDevicePluginPnl.<event_handler>
        print "Event handler `_on_discard_editor_button_pressed' not implemented!"
        event.Skip()

# end of class wxgCardiacDevicePluginPnl


