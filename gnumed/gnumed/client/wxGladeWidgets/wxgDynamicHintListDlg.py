#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.7.2
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
from Gnumed.wxpython.gmTextCtrl import cTextCtrl
from Gnumed.wxpython.gmListWidgets import cReportListCtrl
# end wxGlade


class wxgDynamicHintListDlg(wx.Dialog):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgDynamicHintListDlg.__init__
		kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER
		wx.Dialog.__init__(self, *args, **kwds)
		self._TCTRL_header = wx.TextCtrl(self, wx.ID_ANY, _("Dynamic hints"), style=wx.BORDER_NONE | wx.TE_CENTRE | wx.TE_READONLY)
		self._LCTRL_hints = cReportListCtrl(self, wx.ID_ANY, style=wx.BORDER_SIMPLE | wx.LC_REPORT | wx.LC_SINGLE_SEL)
		self._TCTRL_hint = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_WORDWRAP)
		self._TCTRL_source = wx.TextCtrl(self, wx.ID_ANY, _("<hint source>"), style=wx.BORDER_NONE | wx.TE_CENTRE | wx.TE_READONLY)
		self._URL_info = wx.HyperlinkCtrl(self, wx.ID_ANY, _("Further information"), _("http://www.duckduckgo.com"), style=wx.HL_DEFAULT_STYLE)
		self._TCTRL_rationale = cTextCtrl(self, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.TE_MULTILINE | wx.TE_WORDWRAP)
		self._LBL_previous_rationale = wx.StaticText(self, wx.ID_ANY, _("Previous\nrationale"))
		self._TCTRL_previous_rationale = cTextCtrl(self, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_WORDWRAP)
		self._BTN_OK = wx.Button(self, wx.ID_OK, "")
		self._BTN_suppress = wx.Button(self, wx.ID_ANY, _("&Suppress"))
		self._BTN_manage_hints = wx.Button(self, wx.ID_ANY, _("&Manage"), style=wx.BU_EXACTFIT)

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_BUTTON, self._on_suppress_button_pressed, self._BTN_suppress)
		self.Bind(wx.EVT_BUTTON, self._on_manage_hints_button_pressed, self._BTN_manage_hints)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: wxgDynamicHintListDlg.__set_properties
		self.SetTitle(_("Dynamic hint"))
		self.SetSize((400, 615))
		self._TCTRL_header.SetBackgroundColour(wx.Colour(255, 0, 0))
		self._TCTRL_header.SetForegroundColour(wx.Colour(255, 255, 0))
		self._TCTRL_header.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		self._TCTRL_hint.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_BACKGROUND))
		self._TCTRL_source.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_BACKGROUND))
		self._URL_info.Enable(False)
		self._TCTRL_rationale.SetToolTipString(_("Enter a rationale for suppressing this hint."))
		self._TCTRL_previous_rationale.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_BACKGROUND))
		self._BTN_OK.SetToolTipString(_("Dismiss this hint for now."))
		self._BTN_OK.SetFocus()
		self._BTN_suppress.SetToolTipString(_("Suppress this hint in this patient (needs a rationale)."))
		self._BTN_suppress.Enable(False)
		self._BTN_manage_hints.SetToolTipString(_("Manage dynamic hints."))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: wxgDynamicHintListDlg.__do_layout
		__szr_main = wx.BoxSizer(wx.VERTICAL)
		__szr_buttons = wx.BoxSizer(wx.HORIZONTAL)
		__gszr_rationale = wx.FlexGridSizer(2, 2, 3, 5)
		__szr_main.Add(self._TCTRL_header, 0, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 3)
		__szr_main.Add(self._LCTRL_hints, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 0)
		__szr_main.Add(self._TCTRL_hint, 1, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 3)
		__szr_main.Add(self._TCTRL_source, 0, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 3)
		__szr_main.Add(self._URL_info, 0, wx.ALIGN_CENTER | wx.BOTTOM, 5)
		__lbl_rationale = wx.StaticText(self, wx.ID_ANY, _("Rationale for\nsuppression\nfor this patient"))
		__gszr_rationale.Add(__lbl_rationale, 0, wx.ALIGN_CENTER_VERTICAL, 3)
		__gszr_rationale.Add(self._TCTRL_rationale, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__gszr_rationale.Add(self._LBL_previous_rationale, 0, wx.ALIGN_CENTER_VERTICAL, 3)
		__gszr_rationale.Add(self._TCTRL_previous_rationale, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__gszr_rationale.AddGrowableRow(0)
		__gszr_rationale.AddGrowableCol(1)
		__szr_main.Add(__gszr_rationale, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.LEFT | wx.RIGHT, 3)
		__szr_buttons.Add((20, 20), 2, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__szr_buttons.Add(self._BTN_OK, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 10)
		__szr_buttons.Add((20, 20), 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__szr_buttons.Add(self._BTN_suppress, 0, wx.ALIGN_CENTER_VERTICAL, 5)
		__szr_buttons.Add((20, 20), 2, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__szr_buttons.Add(self._BTN_manage_hints, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_buttons.Add((20, 20), 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__szr_main.Add(__szr_buttons, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 3)
		self.SetSizer(__szr_main)
		self.Layout()
		# end wxGlade

	def _on_suppress_button_pressed(self, event):  # wxGlade: wxgDynamicHintListDlg.<event_handler>
		print "Event handler '_on_suppress_button_pressed' not implemented!"
		event.Skip()

	def _on_manage_hints_button_pressed(self, event):  # wxGlade: wxgDynamicHintListDlg.<event_handler>
		print "Event handler '_on_manage_hints_button_pressed' not implemented!"
		event.Skip()

# end of class wxgDynamicHintListDlg
