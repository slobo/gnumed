#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 from "/home/ncq/Projekte/gm-git/gnumed/gnumed/client/wxg/wxgVaccinationEAPnl.wxg"

import wx

# begin wxGlade: extracode
# end wxGlade



class wxgVaccinationEAPnl(wx.ScrolledWindow):
    def __init__(self, *args, **kwds):

        from Gnumed.wxpython import gmDateTimeInput
        from Gnumed.wxpython import gmPhraseWheel
        from Gnumed.wxpython import gmVaccWidgets
        from Gnumed.wxpython import gmEMRStructWidgets
        from Gnumed.wxpython import gmStaffWidgets

        # begin wxGlade: wxgVaccinationEAPnl.__init__
        kwds["style"] = wx.BORDER_NONE | wx.TAB_TRAVERSAL
        wx.ScrolledWindow.__init__(self, *args, **kwds)
        self._PRW_date_given = gmDateTimeInput.cDateInputPhraseWheel(self, wx.ID_ANY, "", style=wx.BORDER_NONE)
        self._CHBOX_anamnestic = wx.CheckBox(self, wx.ID_ANY, _("Anamnestic"))
        self._PRW_vaccine = gmVaccWidgets.cVaccinePhraseWheel(self, wx.ID_ANY, "", style=wx.BORDER_NONE)
        self._BTN_add_vaccine = wx.Button(self, wx.ID_ANY, _(" + "), style=wx.BU_EXACTFIT)
        self._TCTRL_indications = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.TE_MULTILINE | wx.TE_READONLY)
        self._PRW_batch = gmVaccWidgets.cBatchNoPhraseWheel(self, wx.ID_ANY, "", style=wx.BORDER_NONE)
        self._PRW_episode = gmEMRStructWidgets.cEpisodeSelectionPhraseWheel(self, wx.ID_ANY, "", style=wx.BORDER_NONE)
        self._PRW_site = gmPhraseWheel.cPhraseWheel(self, wx.ID_ANY, "", style=wx.BORDER_NONE)
        self._PRW_provider = gmStaffWidgets.cProviderPhraseWheel(self, wx.ID_ANY, "", style=wx.BORDER_NONE)
        self._PRW_reaction = gmPhraseWheel.cPhraseWheel(self, wx.ID_ANY, "", style=wx.BORDER_NONE)
        self._BTN_report = wx.Button(self, wx.ID_ANY, _("ADR"), style=wx.BU_EXACTFIT)
        self._TCTRL_comment = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.BORDER_NONE)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self._on_add_vaccine_button_pressed, self._BTN_add_vaccine)
        self.Bind(wx.EVT_BUTTON, self._on_report_button_pressed, self._BTN_report)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxgVaccinationEAPnl.__set_properties
        self.SetScrollRate(10, 10)
        self._PRW_date_given.SetToolTipString(_("Mandatory: When was the vaccination given to the patient ?"))
        self._CHBOX_anamnestic.SetToolTipString(_("Check this if - within the SOAP classification - you want to mark the entry as Subjective rather than Plan."))
        self._PRW_vaccine.SetToolTipString(_("The vaccine used, if known.\n\nIf unknown check off the indications which were vaccinated against."))
        self._BTN_add_vaccine.SetToolTipString(_("Add a vaccine to GNUmed."))
        self._TCTRL_indications.Enable(False)
        self._PRW_batch.SetToolTipString(_("The batch number of the vaccine."))
        self._PRW_episode.SetToolTipString(_("Select an episode to file this vaccination under.\n\nIf you do not select one it will be filed under \"prevention\".\n\nAlternatively, type the name for a new episode."))
        self._PRW_site.SetToolTipString(_("The injection site, if known."))
        self._PRW_provider.SetToolTipString(_("The provider who administered the vaccine, if known."))
        self._PRW_reaction.SetToolTipString(_("Record any adverse reactions to this vaccine."))
        self._BTN_report.SetToolTipString(_("Report this event as an adverse drug reaction."))
        self._BTN_report.Enable(False)
        self._TCTRL_comment.SetToolTipString(_("Any comment you may wish to relate to this vaccination."))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxgVaccinationEAPnl.__do_layout
        _gszr_main = wx.FlexGridSizer(10, 2, 1, 3)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        _SZR_indications = wx.BoxSizer(wx.VERTICAL)
        __szr_vaccine_details = wx.BoxSizer(wx.HORIZONTAL)
        __szr_date_details = wx.BoxSizer(wx.HORIZONTAL)
        __lbl_date_given = wx.StaticText(self, wx.ID_ANY, _("Date given"))
        __lbl_date_given.SetForegroundColour(wx.Colour(255, 0, 0))
        _gszr_main.Add(__lbl_date_given, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_date_details.Add(self._PRW_date_given, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        __szr_date_details.Add(self._CHBOX_anamnestic, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        _gszr_main.Add(__szr_date_details, 1, wx.EXPAND, 0)
        __lbl_vaccine = wx.StaticText(self, wx.ID_ANY, _("Vaccine ..."))
        __lbl_vaccine.SetForegroundColour(wx.Colour(255, 127, 0))
        _gszr_main.Add(__lbl_vaccine, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        __szr_vaccine_details.Add(self._PRW_vaccine, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.RIGHT, 5)
        __szr_vaccine_details.Add(self._BTN_add_vaccine, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        _gszr_main.Add(__szr_vaccine_details, 1, wx.EXPAND, 0)
        _gszr_main.Add((20, 20), 1, wx.EXPAND, 0)
        _SZR_indications.Add(self._TCTRL_indications, 1, wx.EXPAND, 0)
        _gszr_main.Add(_SZR_indications, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        __lbl_batch = wx.StaticText(self, wx.ID_ANY, _(u"Batch \u2116"))
        __lbl_batch.SetForegroundColour(wx.Colour(255, 0, 0))
        _gszr_main.Add(__lbl_batch, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        _gszr_main.Add(self._PRW_batch, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 10)
        __lbl_episode = wx.StaticText(self, wx.ID_ANY, _("Episode"))
        __lbl_episode.SetForegroundColour(wx.Colour(255, 127, 0))
        _gszr_main.Add(__lbl_episode, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        _gszr_main.Add(self._PRW_episode, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        __lbl_site = wx.StaticText(self, wx.ID_ANY, _("Site"))
        _gszr_main.Add(__lbl_site, 0, wx.ALIGN_CENTER_VERTICAL, 5)
        _gszr_main.Add(self._PRW_site, 2, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 10)
        __lbl_provider = wx.StaticText(self, wx.ID_ANY, _("Given by"))
        _gszr_main.Add(__lbl_provider, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        _gszr_main.Add(self._PRW_provider, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        __lbl_reaction = wx.StaticText(self, wx.ID_ANY, _("Reaction"))
        _gszr_main.Add(__lbl_reaction, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(self._PRW_reaction, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.RIGHT, 5)
        sizer_1.Add(self._BTN_report, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        _gszr_main.Add(sizer_1, 1, wx.EXPAND, 0)
        __lbl_comment = wx.StaticText(self, wx.ID_ANY, _("Comment"))
        _gszr_main.Add(__lbl_comment, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        _gszr_main.Add(self._TCTRL_comment, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        self.SetSizer(_gszr_main)
        _gszr_main.Fit(self)
        _gszr_main.AddGrowableRow(2)
        _gszr_main.AddGrowableCol(1)
        self.Layout()
        # end wxGlade

    def _on_add_vaccine_button_pressed(self, event): # wxGlade: wxgVaccinationEAPnl.<event_handler>
        print "Event handler `_on_add_vaccine_button_pressed' not implemented!"
        event.Skip()

    def _on_report_button_pressed(self, event): # wxGlade: wxgVaccinationEAPnl.<event_handler>
        print "Event handler `_on_report_button_pressed' not implemented"
        event.Skip()

    def _on_select_indications_button_pressed(self, event):  # wxGlade: wxgVaccinationEAPnl.<event_handler>
        print "Event handler `_on_select_indications_button_pressed' not implemented"
        event.Skip()

# end of class wxgVaccinationEAPnl


