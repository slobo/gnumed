#!/usr/bin/env python
# -*- coding: utf8 -*-
# generated by wxGlade 0.6.3 from "/home/ncq/Projekte/gm-cvs/branches/HEAD/gnumed/gnumed/client/wxg/wxgProcedureEAPnl.wxg"

import wx

# begin wxGlade: extracode
# end wxGlade



class wxgProcedureEAPnl(wx.ScrolledWindow):
    def __init__(self, *args, **kwds):

        from Gnumed.wxpython import gmPhraseWheel
        from Gnumed.wxpython import gmEMRStructWidgets
        from Gnumed.wxpython import gmDateTimeInput

        # begin wxGlade: wxgProcedureEAPnl.__init__
        kwds["style"] = wx.NO_BORDER|wx.TAB_TRAVERSAL
        wx.ScrolledWindow.__init__(self, *args, **kwds)
        self._DPRW_date = gmDateTimeInput.cFuzzyTimestampInput(self, -1, "", style=wx.NO_BORDER)
        self._PRW_hospital_stay = gmEMRStructWidgets.cHospitalStayPhraseWheel(self, -1, "", style=wx.NO_BORDER)
        self._BTN_add_stay = wx.Button(self, -1, _("+"), style=wx.BU_EXACTFIT)
        self._PRW_location = gmPhraseWheel.cPhraseWheel(self, -1, "", style=wx.NO_BORDER)
        self._PRW_episode = gmEMRStructWidgets.cEpisodeSelectionPhraseWheel(self, -1, "", style=wx.NO_BORDER)
        self._PRW_procedure = gmPhraseWheel.cPhraseWheel(self, -1, "", style=wx.NO_BORDER)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self._on_add_hospital_stay_button_pressed, self._BTN_add_stay)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxgProcedureEAPnl.__set_properties
        self.SetScrollRate(10, 10)
        self._DPRW_date.SetToolTipString(_("When did this procedure take place ?"))
        self._PRW_hospital_stay.SetToolTipString(_("During which hospital stay was this procedure performed."))
        self._BTN_add_stay.SetToolTipString(_("Add a hospital stay."))
        self._PRW_location.SetToolTipString(_("The location (praxis, clinic, ...) this procedure was performed at.\n\nMutually exclusive with \"Hospital stay\". Requires \"Episode\"."))
        self._PRW_episode.SetToolTipString(_("The episode this procedure was performed under.\n\nMutually exclusive with \"Hospital stay\". Requires \"Location\"."))
        self._PRW_procedure.SetToolTipString(_("The actual procedure performed on the patient."))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxgProcedureEAPnl.__do_layout
        _gszr_main = wx.FlexGridSizer(6, 2, 1, 3)
        __szr_stay = wx.BoxSizer(wx.HORIZONTAL)
        __lbl_date = wx.StaticText(self, -1, _("Date"))
        _gszr_main.Add(__lbl_date, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        _gszr_main.Add(self._DPRW_date, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __lbl_stay = wx.StaticText(self, -1, _("Hospital stay"))
        _gszr_main.Add(__lbl_stay, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_stay.Add(self._PRW_hospital_stay, 1, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        __szr_stay.Add(self._BTN_add_stay, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        _gszr_main.Add(__szr_stay, 1, wx.EXPAND, 0)
        __lbl_or = wx.StaticText(self, -1, _("... or ..."))
        _gszr_main.Add(__lbl_or, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        _gszr_main.Add((20, 20), 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __lbl_location = wx.StaticText(self, -1, _("Location"))
        _gszr_main.Add(__lbl_location, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        _gszr_main.Add(self._PRW_location, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __lbl_episode = wx.StaticText(self, -1, _("and Episode"))
        _gszr_main.Add(__lbl_episode, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        _gszr_main.Add(self._PRW_episode, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        __lbl_procedure = wx.StaticText(self, -1, _("Procedure"))
        _gszr_main.Add(__lbl_procedure, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        _gszr_main.Add(self._PRW_procedure, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(_gszr_main)
        _gszr_main.Fit(self)
        _gszr_main.AddGrowableCol(1)
        # end wxGlade

    def _on_add_hospital_stay_button_pressed(self, event): # wxGlade: wxgProcedureEAPnl.<event_handler>
        print "Event handler `_on_add_hospital_stay_button_pressed' not implemented!"
        event.Skip()

# end of class wxgProcedureEAPnl

