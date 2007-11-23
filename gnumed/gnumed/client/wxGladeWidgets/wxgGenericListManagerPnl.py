#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.5 on Wed Nov 14 15:59:11 2007 from /home/ncq/Projekte/gm-cvs/branches/HEAD/gnumed/gnumed/client/wxg/wxgGenericListManagerPnl.wxg

import wx

class wxgGenericListManagerPnl(wx.ScrolledWindow):
    def __init__(self, *args, **kwds):

        from Gnumed.wxpython import gmListWidgets

        # begin wxGlade: wxgGenericListManagerPnl.__init__
        kwds["style"] = wx.NO_BORDER|wx.TAB_TRAVERSAL
        wx.ScrolledWindow.__init__(self, *args, **kwds)
        self._LBL_message = wx.StaticText(self, -1, "", style=wx.ALIGN_CENTRE)
        self._LCTRL_items = gmListWidgets.cReportListCtrl(self, -1, style=wx.LC_REPORT|wx.LC_HRULES|wx.NO_BORDER)
        self._BTN_add = wx.Button(self, wx.ID_ADD, "")
        self._BTN_edit = wx.Button(self, -1, _("Edit"))
        self._BTN_remove = wx.Button(self, wx.ID_REMOVE, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self._on_list_item_deselected, self._LCTRL_items)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_list_item_selected, self._LCTRL_items)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self._on_list_item_activated, self._LCTRL_items)
        self.Bind(wx.EVT_BUTTON, self._on_add_button_pressed, self._BTN_add)
        self.Bind(wx.EVT_BUTTON, self._on_edit_button_pressed, self._BTN_edit)
        self.Bind(wx.EVT_BUTTON, self._on_remove_button_pressed, self._BTN_remove)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxgGenericListManagerPnl.__set_properties
        self.SetScrollRate(10, 10)
        self._BTN_add.SetToolTipString(_("Add a new item to the list."))
        self._BTN_add.Enable(False)
        self._BTN_edit.SetToolTipString(_("Edit the selected item."))
        self._BTN_edit.Enable(False)
        self._BTN_remove.SetToolTipString(_("Remove the selected item(s) from the list."))
        self._BTN_remove.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxgGenericListManagerPnl.__do_layout
        __szr_main = wx.BoxSizer(wx.VERTICAL)
        __szr_buttons = wx.BoxSizer(wx.HORIZONTAL)
        __szr_main.Add(self._LBL_message, 0, wx.BOTTOM|wx.EXPAND, 6)
        __szr_main.Add(self._LCTRL_items, 1, wx.EXPAND, 0)
        __szr_buttons.Add((20, 20), 2, wx.ADJUST_MINSIZE, 0)
        __szr_buttons.Add(self._BTN_add, 0, 0, 0)
        __szr_buttons.Add((20, 20), 1, wx.ADJUST_MINSIZE, 0)
        __szr_buttons.Add(self._BTN_edit, 0, 0, 0)
        __szr_buttons.Add((20, 20), 1, wx.ADJUST_MINSIZE, 0)
        __szr_buttons.Add(self._BTN_remove, 0, 0, 0)
        __szr_buttons.Add((20, 20), 2, wx.ADJUST_MINSIZE, 0)
        __szr_main.Add(__szr_buttons, 0, wx.TOP|wx.EXPAND, 5)
        self.SetSizer(__szr_main)
        __szr_main.Fit(self)
        # end wxGlade

    def _on_list_item_deselected(self, event): # wxGlade: wxgGenericListManagerPnl.<event_handler>
        print "Event handler `_on_list_item_deselected' not implemented!"
        event.Skip()

    def _on_list_item_selected(self, event): # wxGlade: wxgGenericListManagerPnl.<event_handler>
        print "Event handler `_on_list_item_selected' not implemented!"
        event.Skip()

    def _on_list_item_activated(self, event): # wxGlade: wxgGenericListManagerPnl.<event_handler>
        print "Event handler `_on_list_item_activated' not implemented!"
        event.Skip()

    def _on_add_button_pressed(self, event): # wxGlade: wxgGenericListManagerPnl.<event_handler>
        print "Event handler `_on_add_button_pressed' not implemented!"
        event.Skip()

    def _on_edit_button_pressed(self, event): # wxGlade: wxgGenericListManagerPnl.<event_handler>
        print "Event handler `_on_edit_button_pressed' not implemented!"
        event.Skip()

    def _on_remove_button_pressed(self, event): # wxGlade: wxgGenericListManagerPnl.<event_handler>
        print "Event handler `_on_remove_button_pressed' not implemented!"
        event.Skip()

# end of class wxgGenericListManagerPnl

