#!/usr/bin/env python
# -*- coding: utf8 -*-
# generated by wxGlade 0.6.3 from "/home/ncq/Projekte/gm-cvs/branches/HEAD/gnumed/gnumed/client/wxg/wxgSoapPluginPnl.wxg"

import wx

# begin wxGlade: extracode
# end wxGlade



class wxgSoapPluginPnl(wx.ScrolledWindow):
    def __init__(self, *args, **kwds):

        from Gnumed.wxpython.gmNarrativeWidgets import cSoapNoteInputNotebook
        from Gnumed.wxpython.gmNarrativeWidgets import cVisualSoapPnl
        from Gnumed.wxpython.gmDateTimeInput import cFuzzyTimestampInput
        from Gnumed.wxpython.gmEMRStructWidgets import cEncounterTypePhraseWheel
        from Gnumed.wxpython.gmCodingWidgets import cGenericCodesPhraseWheel
        from Gnumed.wxpython import gmListWidgets

        # begin wxGlade: wxgSoapPluginPnl.__init__
        kwds["style"] = wx.NO_BORDER|wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self._splitter_main = wx.SplitterWindow(self, -1, style=wx.SP_3D|wx.SP_BORDER|wx.SP_PERMIT_UNSPLIT)
        self.__splitter_main_right_pnl = wx.Panel(self._splitter_main, -1, style=wx.NO_BORDER|wx.TAB_TRAVERSAL)
        self._NB_soap_editors = cSoapNoteInputNotebook(self.__splitter_main_right_pnl, -1, style=0)
        self.__splitter_main_left_pnl = wx.Panel(self._splitter_main, -1, style=wx.NO_BORDER)
        self._splitter_left = wx.SplitterWindow(self.__splitter_main_left_pnl, -1, style=wx.SP_3D|wx.SP_BORDER|wx.SP_PERMIT_UNSPLIT)
        self.__splitter_left_bottom_pnl = wx.Panel(self._splitter_left, -1, style=wx.NO_BORDER)
        self.__splitter_left_top_pnl = wx.Panel(self._splitter_left, -1, style=wx.NO_BORDER)
        self._SZR_recent_notes_staticbox = wx.StaticBox(self.__splitter_left_bottom_pnl, -1, _("Most recent notes on above problem"))
        self.__szr_right_staticbox = wx.StaticBox(self.__splitter_main_right_pnl, -1, _("New notelets in current encounter"))
        self._SZR_problem_list_staticbox = wx.StaticBox(self.__splitter_left_top_pnl, -1, _("Active problems"))
        self._CHBOX_show_closed_episodes = wx.CheckBox(self.__splitter_left_top_pnl, -1, _("Closed episodes"))
        self._CHBOX_irrelevant_issues = wx.CheckBox(self.__splitter_left_top_pnl, -1, _("Non-relevant issues"))
        self._LCTRL_active_problems = gmListWidgets.cReportListCtrl(self.__splitter_left_top_pnl, -1, style=wx.LC_REPORT|wx.NO_BORDER)
        self._TCTRL_recent_notes = wx.TextCtrl(self.__splitter_left_bottom_pnl, -1, _("In this area GNUmed will place the notes of the\nprevious encounter as well as notes by other\nstaff for the current encounter.\n\nNote that this may change depending on which\nactive problem is selected in the editor below."), style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP|wx.NO_BORDER)
        self._PRW_encounter_type = cEncounterTypePhraseWheel(self.__splitter_main_right_pnl, -1, "", style=wx.NO_BORDER)
        self._PRW_encounter_start = cFuzzyTimestampInput(self.__splitter_main_right_pnl, -1, "", style=wx.NO_BORDER)
        self._PRW_encounter_end = cFuzzyTimestampInput(self.__splitter_main_right_pnl, -1, "", style=wx.NO_BORDER)
        self._TCTRL_rfe = wx.TextCtrl(self.__splitter_main_right_pnl, -1, "", style=wx.NO_BORDER)
        self._PRW_rfe_codes = cGenericCodesPhraseWheel(self.__splitter_main_right_pnl, -1, "", style=wx.NO_BORDER)
        self._TCTRL_aoe = wx.TextCtrl(self.__splitter_main_right_pnl, -1, "", style=wx.NO_BORDER)
        self._PRW_aoe_codes = cGenericCodesPhraseWheel(self.__splitter_main_right_pnl, -1, "", style=wx.NO_BORDER)
        self.notebook_1_pane_1 = wx.Panel(self._NB_soap_editors, -1)
        self._BTN_new_editor = wx.Button(self.__splitter_main_right_pnl, -1, _("&New"), style=wx.BU_EXACTFIT)
        self._BTN_clear_editor = wx.Button(self.__splitter_main_right_pnl, -1, _("&Clear"), style=wx.BU_EXACTFIT)
        self._BTN_discard_editor = wx.Button(self.__splitter_main_right_pnl, -1, _("&Discard"), style=wx.BU_EXACTFIT)
        self._BTN_save_note = wx.Button(self.__splitter_main_right_pnl, -1, _("&Save"), style=wx.BU_EXACTFIT)
        self._BTN_save_note_under = wx.Button(self.__splitter_main_right_pnl, -1, _("Save &under"), style=wx.BU_EXACTFIT)
        self._BTN_image = wx.Button(self.__splitter_main_right_pnl, -1, _("&Image"), style=wx.BU_EXACTFIT)
        self._BTN_new_encounter = wx.Button(self.__splitter_main_right_pnl, -1, _("New"), style=wx.BU_EXACTFIT)
        self._BTN_save_encounter = wx.Button(self.__splitter_main_right_pnl, -1, _("Save"), style=wx.BU_EXACTFIT)
        self._BTN_save_all = wx.Button(self.__splitter_main_right_pnl, -1, _("Save &all"), style=wx.BU_EXACTFIT)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_CHECKBOX, self._on_show_closed_episodes_checked, self._CHBOX_show_closed_episodes)
        self.Bind(wx.EVT_CHECKBOX, self._on_irrelevant_issues_checked, self._CHBOX_irrelevant_issues)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_problem_selected, self._LCTRL_active_problems)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self._on_problem_activated, self._LCTRL_active_problems)
        self.Bind(wx.EVT_LIST_ITEM_FOCUSED, self._on_problem_focused, self._LCTRL_active_problems)
        self.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self._on_problem_rclick, self._LCTRL_active_problems)
        self.Bind(wx.EVT_BUTTON, self._on_new_editor_button_pressed, self._BTN_new_editor)
        self.Bind(wx.EVT_BUTTON, self._on_clear_editor_button_pressed, self._BTN_clear_editor)
        self.Bind(wx.EVT_BUTTON, self._on_discard_editor_button_pressed, self._BTN_discard_editor)
        self.Bind(wx.EVT_BUTTON, self._on_save_note_button_pressed, self._BTN_save_note)
        self.Bind(wx.EVT_BUTTON, self._on_save_note_under_button_pressed, self._BTN_save_note_under)
        self.Bind(wx.EVT_BUTTON, self._on_image_button_pressed, self._BTN_image)
        self.Bind(wx.EVT_BUTTON, self._on_new_encounter_button_pressed, self._BTN_new_encounter)
        self.Bind(wx.EVT_BUTTON, self._on_save_encounter_button_pressed, self._BTN_save_encounter)
        self.Bind(wx.EVT_BUTTON, self._on_save_all_button_pressed, self._BTN_save_all)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxgSoapPluginPnl.__set_properties
        self._CHBOX_show_closed_episodes.SetToolTipString(_("Show closed episodes as pseudo-problems ?"))
        self._CHBOX_irrelevant_issues.SetToolTipString(_("Show issues marked clinically NOT relevant."))
        self._LCTRL_active_problems.SetToolTipString(_("This shows the list of active problems, They include open episodes as well as active health issues."))
        self._TCTRL_recent_notes.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DFACE))
        self._PRW_encounter_type.SetToolTipString(_("Select the type of encounter."))
        self._PRW_encounter_start.SetToolTipString(_("Date and time when the current (!) encounter started."))
        self._PRW_encounter_end.SetToolTipString(_("Date and time when the current (!) encounter ends."))
        self._TCTRL_rfe.SetToolTipString(_("This documents why the encounter takes place.\n\nIt may be due to a patient request or it may be prompted by other reasons. Often initially collected at the front desk and put into a waiting list comment. May turn out to just be a proxy request for why the patient really is here.\n\nAlso known as the Reason For Encounter/Visit (RFE)."))
        self._PRW_rfe_codes.SetToolTipString(_("Enter codes relevant to this Reason for Encounter."))
        self._TCTRL_aoe.SetToolTipString(_("This summarizes the outcome/assessment of the consultation from the doctors point of view. Note that this summary spans all the problems discussed during this encounter."))
        self._PRW_aoe_codes.SetToolTipString(_("Enter codes relevant to this Outcome of Encounter."))
        self._BTN_new_editor.SetToolTipString(_("Open a new progress note editor.\n\nThere is a configuration item on whether to allow several new-episode editors at once."))
        self._BTN_clear_editor.SetToolTipString(_("Clear the editor for the displayed progress note."))
        self._BTN_discard_editor.SetToolTipString(_("Discard the editor for the displayed progress note."))
        self._BTN_save_note.SetToolTipString(_("Save the currently displayed progress note under the current encounter."))
        self._BTN_save_note_under.SetToolTipString(_("Save the currently displayed note into an encounter selected from a list of encounters."))
        self._BTN_image.SetToolTipString(_("Add a visual progress note for this episode."))
        self._BTN_new_encounter.SetToolTipString(_("Start a new encounter. If there are any changes to the current encounter you will be asked whether to save them."))
        self._BTN_save_encounter.SetToolTipString(_("Save the encounter details."))
        self._BTN_save_all.SetToolTipString(_("Save encounter details and all progress notes."))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxgSoapPluginPnl.__do_layout
        __szr_main = wx.BoxSizer(wx.HORIZONTAL)
        __szr_right = wx.StaticBoxSizer(self.__szr_right_staticbox, wx.VERTICAL)
        __szr_buttons = wx.BoxSizer(wx.HORIZONTAL)
        __gszr_encounter_details = wx.FlexGridSizer(3, 2, 2, 5)
        __szr_aoe = wx.BoxSizer(wx.HORIZONTAL)
        __szr_rfe_details = wx.BoxSizer(wx.HORIZONTAL)
        __szr_encounter_details = wx.BoxSizer(wx.HORIZONTAL)
        __szr_left = wx.BoxSizer(wx.HORIZONTAL)
        _SZR_recent_notes = wx.StaticBoxSizer(self._SZR_recent_notes_staticbox, wx.VERTICAL)
        _SZR_problem_list = wx.StaticBoxSizer(self._SZR_problem_list_staticbox, wx.VERTICAL)
        __szr_problem_filter = wx.BoxSizer(wx.HORIZONTAL)
        __lbl_problem_filter = wx.StaticText(self.__splitter_left_top_pnl, -1, _("Include:"))
        __szr_problem_filter.Add(__lbl_problem_filter, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 10)
        __szr_problem_filter.Add(self._CHBOX_show_closed_episodes, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_problem_filter.Add(self._CHBOX_irrelevant_issues, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_problem_filter.Add((20, 20), 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        _SZR_problem_list.Add(__szr_problem_filter, 0, wx.EXPAND, 0)
        _SZR_problem_list.Add(self._LCTRL_active_problems, 1, wx.EXPAND, 0)
        self.__splitter_left_top_pnl.SetSizer(_SZR_problem_list)
        _SZR_recent_notes.Add(self._TCTRL_recent_notes, 1, wx.EXPAND, 0)
        self.__splitter_left_bottom_pnl.SetSizer(_SZR_recent_notes)
        self._splitter_left.SplitHorizontally(self.__splitter_left_top_pnl, self.__splitter_left_bottom_pnl)
        __szr_left.Add(self._splitter_left, 1, wx.EXPAND, 0)
        self.__splitter_main_left_pnl.SetSizer(__szr_left)
        __lbl_encounter_details = wx.StaticText(self.__splitter_main_right_pnl, -1, _("Encounter"))
        __gszr_encounter_details.Add(__lbl_encounter_details, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_encounter_details.Add(self._PRW_encounter_type, 1, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 10)
        __szr_encounter_details.Add(self._PRW_encounter_start, 1, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        __lbl_until = wx.StaticText(self.__splitter_main_right_pnl, -1, _("until"))
        __szr_encounter_details.Add(__lbl_until, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_encounter_details.Add(self._PRW_encounter_end, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        __gszr_encounter_details.Add(__szr_encounter_details, 1, wx.EXPAND, 0)
        __lbl_rfe = wx.StaticText(self.__splitter_main_right_pnl, -1, _("Purpose"))
        __gszr_encounter_details.Add(__lbl_rfe, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_rfe_details.Add(self._TCTRL_rfe, 2, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        __lbl_rfe_codes = wx.StaticText(self.__splitter_main_right_pnl, -1, _("Codes:"))
        __szr_rfe_details.Add(__lbl_rfe_codes, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_rfe_details.Add(self._PRW_rfe_codes, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __gszr_encounter_details.Add(__szr_rfe_details, 1, wx.EXPAND, 0)
        __lbl_aoe = wx.StaticText(self.__splitter_main_right_pnl, -1, _("Summary"))
        __gszr_encounter_details.Add(__lbl_aoe, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_aoe.Add(self._TCTRL_aoe, 2, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        __lbl_aoe_codes = wx.StaticText(self.__splitter_main_right_pnl, -1, _("Codes:"))
        __szr_aoe.Add(__lbl_aoe_codes, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_aoe.Add(self._PRW_aoe_codes, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __gszr_encounter_details.Add(__szr_aoe, 0, wx.EXPAND, 3)
        __gszr_encounter_details.AddGrowableCol(1)
        __szr_right.Add(__gszr_encounter_details, 0, wx.RIGHT|wx.TOP|wx.BOTTOM|wx.EXPAND, 3)
        self._NB_soap_editors.AddPage(self.notebook_1_pane_1, _("tab1"))
        __szr_right.Add(self._NB_soap_editors, 4, wx.EXPAND, 3)
        __lbl_editor = wx.StaticText(self.__splitter_main_right_pnl, -1, _("Notelet:"))
        __szr_buttons.Add(__lbl_editor, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_buttons.Add(self._BTN_new_editor, 0, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 3)
        __szr_buttons.Add(self._BTN_clear_editor, 0, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 3)
        __szr_buttons.Add(self._BTN_discard_editor, 0, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 3)
        __szr_buttons.Add(self._BTN_save_note, 0, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 3)
        __szr_buttons.Add(self._BTN_save_note_under, 0, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 3)
        __szr_buttons.Add(self._BTN_image, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_buttons.Add((1, 1), 1, wx.EXPAND, 0)
        __lbl_encounter = wx.StaticText(self.__splitter_main_right_pnl, -1, _("Encounter:"))
        __szr_buttons.Add(__lbl_encounter, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_buttons.Add(self._BTN_new_encounter, 0, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 3)
        __szr_buttons.Add(self._BTN_save_encounter, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 3)
        __szr_buttons.Add((1, 1), 1, wx.EXPAND, 0)
        __szr_buttons.Add(self._BTN_save_all, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_right.Add(__szr_buttons, 0, wx.RIGHT|wx.TOP|wx.EXPAND, 3)
        self.__splitter_main_right_pnl.SetSizer(__szr_right)
        self._splitter_main.SplitVertically(self.__splitter_main_left_pnl, self.__splitter_main_right_pnl)
        __szr_main.Add(self._splitter_main, 1, wx.EXPAND, 0)
        self.SetSizer(__szr_main)
        __szr_main.Fit(self)
        # end wxGlade

    def _on_save_all_button_pressed(self, event): # wxGlade: wxgSoapPluginPnl.<event_handler>
        print "Event handler `_on_save_all_button_pressed' not implemented!"
        event.Skip()

    def _on_save_encounter_button_pressed(self, event): # wxGlade: wxgSoapPluginPnl.<event_handler>
        print "Event handler `_on_save_encounter_button_pressed' not implemented!"
        event.Skip()

    def _on_save_note_button_pressed(self, event): # wxGlade: wxgSoapPluginPnl.<event_handler>
        print "Event handler `_on_save_note_button_pressed' not implemented!"
        event.Skip()

    def _on_new_editor_button_pressed(self, event): # wxGlade: wxgSoapPluginPnl.<event_handler>
        print "Event handler `_on_new_editor_button_pressed' not implemented!"
        event.Skip()

    def _on_clear_editor_button_pressed(self, event): # wxGlade: wxgSoapPluginPnl.<event_handler>
        print "Event handler `_on_clear_editor_button_pressed' not implemented!"
        event.Skip()

    def _on_discard_editor_button_pressed(self, event): # wxGlade: wxgSoapPluginPnl.<event_handler>
        print "Event handler `_on_discard_editor_button_pressed' not implemented!"
        event.Skip()

    def _on_problem_activated(self, event): # wxGlade: wxgSoapPluginPnl.<event_handler>
        print "Event handler `_on_problem_activated' not implemented"
        event.Skip()

    def _on_new_encounter_button_pressed(self, event): # wxGlade: wxgSoapPluginPnl.<event_handler>
        print "Event handler `_on_new_encounter_button_pressed' not implemented"
        event.Skip()

    def _on_problem_selected(self, event): # wxGlade: wxgSoapPluginPnl.<event_handler>
        print "Event handler `_on_problem_selected' not implemented"
        event.Skip()

    def _on_problem_focused(self, event): # wxGlade: wxgSoapPluginPnl.<event_handler>
        print "Event handler `_on_problem_focused' not implemented"
        event.Skip()

    def _on_show_closed_episodes_checked(self, event): # wxGlade: wxgSoapPluginPnl.<event_handler>
        print "Event handler `_on_show_closed_episodes_checked' not implemented"
        event.Skip()

    def _on_irrelevant_issues_checked(self, event): # wxGlade: wxgSoapPluginPnl.<event_handler>
        print "Event handler `_on_irrelevant_issues_checked' not implemented"
        event.Skip()

    def _on_image_button_pressed(self, event): # wxGlade: wxgSoapPluginPnl.<event_handler>
        print "Event handler `_on_image_button_pressed' not implemented"
        event.Skip()

    def _on_save_note_under_button_pressed(self, event): # wxGlade: wxgSoapPluginPnl.<event_handler>
        print "Event handler `_on_save_note_under_button_pressed' not implemented"
        event.Skip()

    def _on_problem_rclick(self, event): # wxGlade: wxgSoapPluginPnl.<event_handler>
        print "Event handler `_on_problem_rclick' not implemented"
        event.Skip()

# end of class wxgSoapPluginPnl


