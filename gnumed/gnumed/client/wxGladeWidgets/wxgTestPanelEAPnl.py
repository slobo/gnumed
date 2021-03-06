# -*- coding: UTF-8 -*-
#
# generated by wxGlade
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
from Gnumed.wxpython.gmListWidgets import cReportListCtrl
from Gnumed.wxpython.gmLOINCWidgets import cLOINCPhraseWheel
# end wxGlade


class wxgTestPanelEAPnl(wx.ScrolledWindow):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgTestPanelEAPnl.__init__
		kwds["style"] = kwds.get("style", 0) | wx.BORDER_NONE | wx.TAB_TRAVERSAL
		wx.ScrolledWindow.__init__(self, *args, **kwds)
		self._TCTRL_description = wx.TextCtrl(self, wx.ID_ANY, "")
		self._TCTRL_comment = wx.TextCtrl(self, wx.ID_ANY, "")
		self._PRW_loinc = cLOINCPhraseWheel(self, wx.ID_ANY, "")
		self._BTN_add_loinc = wx.Button(self, wx.ID_ANY, _("&Add"), style=wx.BU_EXACTFIT)
		self._LBL_loinc = wx.StaticText(self, wx.ID_ANY, "")
		self._LCTRL_loincs = cReportListCtrl(self, wx.ID_ANY, style=wx.BORDER_NONE | wx.LC_REPORT)
		self._BTN_remove_loinc = wx.Button(self, wx.ID_ANY, _("&Remove"), style=wx.BU_EXACTFIT)

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_BUTTON, self._on_add_loinc_button_pressed, self._BTN_add_loinc)
		self.Bind(wx.EVT_BUTTON, self._on_remove_loinc_button_pressed, self._BTN_remove_loinc)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: wxgTestPanelEAPnl.__set_properties
		self.SetScrollRate(10, 10)
		self._TCTRL_description.SetToolTip(_("A short description for this test panel."))
		self._TCTRL_comment.SetToolTip(_("A comment on, or long-form description of, this test panel."))
		self._BTN_add_loinc.SetToolTip(_("Add the selected LOINC to the test panel."))
		self._BTN_remove_loinc.SetToolTip(_("Remove selected LOINC from test panel."))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: wxgTestPanelEAPnl.__do_layout
		_gszr_main = wx.FlexGridSizer(6, 2, 1, 3)
		__szr_loinc = wx.BoxSizer(wx.HORIZONTAL)
		__lbl_description = wx.StaticText(self, wx.ID_ANY, _("Description"))
		_gszr_main.Add(__lbl_description, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		_gszr_main.Add(self._TCTRL_description, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_comment = wx.StaticText(self, wx.ID_ANY, _("Comment"))
		_gszr_main.Add(__lbl_comment, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		_gszr_main.Add(self._TCTRL_comment, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_loinc = wx.StaticText(self, wx.ID_ANY, _("LOINC"))
		_gszr_main.Add(__lbl_loinc, 1, wx.ALIGN_CENTER_VERTICAL, 5)
		__szr_loinc.Add(self._PRW_loinc, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.RIGHT, 3)
		__szr_loinc.Add(self._BTN_add_loinc, 0, wx.ALIGN_CENTER_VERTICAL, 3)
		_gszr_main.Add(__szr_loinc, 1, wx.EXPAND, 0)
		_gszr_main.Add((20, 20), 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		_gszr_main.Add(self._LBL_loinc, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		_gszr_main.Add((20, 20), 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		_gszr_main.Add(self._LCTRL_loincs, 1, wx.EXPAND, 0)
		_gszr_main.Add((20, 20), 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		_gszr_main.Add(self._BTN_remove_loinc, 0, wx.ALIGN_CENTER, 0)
		self.SetSizer(_gszr_main)
		_gszr_main.Fit(self)
		_gszr_main.AddGrowableRow(4)
		_gszr_main.AddGrowableCol(1)
		self.Layout()
		# end wxGlade

	def _on_add_loinc_button_pressed(self, event):  # wxGlade: wxgTestPanelEAPnl.<event_handler>
		print("Event handler '_on_add_loinc_button_pressed' not implemented!")
		event.Skip()

	def _on_remove_loinc_button_pressed(self, event):  # wxGlade: wxgTestPanelEAPnl.<event_handler>
		print("Event handler '_on_remove_loinc_button_pressed' not implemented!")
		event.Skip()

# end of class wxgTestPanelEAPnl
