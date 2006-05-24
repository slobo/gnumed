#!/usr/bin/env python
# -*- coding: ISO-8859-15 -*-
# generated by wxGlade 0.4cvs on Sat Feb  4 22:59:40 2006

from Gnumed.wxpython import gmPhraseWheel, gmDateTimeInput

import wx

class wxgScanIdxPnl(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wxgScanIdxPnl.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.__szr_top_middle_staticbox = wx.StaticBox(self, -1, _("Document Properties"))
        self.__szr_top_right_staticbox = wx.StaticBox(self, -1, _("Pages"))
        self.__szr_top_left_btns_staticbox = wx.StaticBox(self, -1, _("Page Sources"))
        self.__btn_scan = wx.Button(self, -1, _("scan page(s)"))
        self.__btn_load = wx.Button(self, -1, _("pick file(s)"))
        self._PhWheel_episode = gmPhraseWheel.cPhraseWheel(self, -1)
        self._SelBOX_doc_type = wx.Choice(self, -1, choices=[])
        self._TBOX_doc_comment = wx.TextCtrl(self, -1, "")
        self._PhWheel_doc_date = gmDateTimeInput.cFuzzyTimestampInput(self, -1)
        self.__lbl_reviewer = wx.StaticText(self, -1, _("Intended reviewer:"))
        self._PhWheel_reviewer = gmPhraseWheel.cPhraseWheel(self, -1)
        self._ChBOX_reviewed = wx.CheckBox(self, -1, _("mark as reviewed"))
        self._ChBOX_abnormal = wx.CheckBox(self, -1, _("technically abnormal"))
        self._ChBOX_relevant = wx.CheckBox(self, -1, _("clinically relevant"))
        self._LBOX_doc_pages = wx.ListBox(self, -1, choices=[], style=wx.LB_SINGLE|wx.LB_HSCROLL|wx.LB_NEEDED_SB)
        self.__btn_show_page = wx.Button(self, -1, _("show page"))
        self.__btn_del_page = wx.Button(self, -1, _("delete page"))
        self._TBOX_description = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE|wx.TE_LINEWRAP|wx.TE_WORDWRAP|wx.NO_BORDER)
        self.__btn_save = wx.Button(self, -1, _("Save"))
        self.__btn_discard = wx.Button(self, -1, _("Discard"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self._scan_btn_pressed, self.__btn_scan)
        self.Bind(wx.EVT_BUTTON, self._load_btn_pressed, self.__btn_load)
        self.Bind(wx.EVT_CHECKBOX, self._reviewed_box_checked, self._ChBOX_reviewed)
        self.Bind(wx.EVT_BUTTON, self._show_btn_pressed, self.__btn_show_page)
        self.Bind(wx.EVT_BUTTON, self._del_btn_pressed, self.__btn_del_page)
        self.Bind(wx.EVT_BUTTON, self._save_btn_pressed, self.__btn_save)
        self.Bind(wx.EVT_BUTTON, self._startover_btn_pressed, self.__btn_discard)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxgScanIdxPnl.__set_properties
        self.__btn_scan.SetToolTipString(_("Acquire a page from an image source (scanner, camera). This may bring up an intermediate dialog. It uses Sane (Linux) or TWAIN (Windows)."))
        self.__btn_scan.SetFocus()
        self.__btn_scan.SetDefault()
        self.__btn_load.SetToolTipString(_("Add a file from the filesystem as a new page. Shows a file selector dialog."))
        self._PhWheel_episode.SetToolTipString(_("Required: The primary episode this document is to be listed under."))
        self._SelBOX_doc_type.SetToolTipString(_("Required: The type of this document."))
        self._SelBOX_doc_type.SetSelection(0)
        self._TBOX_doc_comment.SetToolTipString(_("Optional: A short comment identifying the document. Good comments give an idea of the content and source of the document."))
        self._PhWheel_doc_date.SetToolTipString(_("Required: The date when the medical information described in the document was produced. This is free text so you can add approximate dates, too, such as 3/2004 where appropriate."))
        self._PhWheel_reviewer.SetToolTipString(_("Required: Enter the provider who will be notified about the new document so it can be reviewed. In most cases this is the primary doctor of the patient."))
        self._ChBOX_reviewed.SetToolTipString(_("Check this to mark the document as reviewed upon import. If checked you can (and must) decide on \"technically abnormal\" and \"clinically relevant\", too. The default can be set by an option."))
        self._ChBOX_abnormal.SetToolTipString(_("Whether this document report technically abormal results."))
        self._ChBOX_abnormal.Enable(False)
        self._ChBOX_relevant.SetToolTipString(_("Whether this document reports clinically relevant results. Note that both normal and abnormal resuslts can be relevant."))
        self._ChBOX_relevant.Enable(False)
        self._LBOX_doc_pages.SetToolTipString(_("This field lists the pages belonging to the current document."))
        self.__btn_show_page.SetToolTipString(_("View the page selected in the above list."))
        self.__btn_del_page.SetToolTipString(_("Remove the page selected in the above list. Will ask before physical deletion from disk."))
        self._TBOX_description.SetToolTipString(_("Optional: A free-text document description."))
        self.__btn_save.SetToolTipString(_("Save finished document."))
        self.__btn_discard.SetToolTipString(_("Start over (discards current data)."))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxgScanIdxPnl.__do_layout
        __szr_main = wx.BoxSizer(wx.VERTICAL)
        __szr_bottom_third = wx.BoxSizer(wx.HORIZONTAL)
        __szr_top_third = wx.BoxSizer(wx.HORIZONTAL)
        __szr_top_right = wx.StaticBoxSizer(self.__szr_top_right_staticbox, wx.VERTICAL)
        __szr_page_actions = wx.BoxSizer(wx.HORIZONTAL)
        __szr_top_middle = wx.StaticBoxSizer(self.__szr_top_middle_staticbox, wx.VERTICAL)
        __szr_top_left_btns = wx.StaticBoxSizer(self.__szr_top_left_btns_staticbox, wx.VERTICAL)
        __szr_top_left_btns.Add(self.__btn_scan, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        __szr_top_left_btns.Add(self.__btn_load, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        __szr_top_third.Add(__szr_top_left_btns, 0, wx.LEFT|wx.EXPAND|wx.ADJUST_MINSIZE, 5)
        __lbl_doc_episode = wx.StaticText(self, -1, _("Associated episode:"))
        __szr_top_middle.Add(__lbl_doc_episode, 0, wx.LEFT|wx.TOP|wx.ADJUST_MINSIZE, 3)
        __szr_top_middle.Add(self._PhWheel_episode, 0, wx.LEFT|wx.EXPAND|wx.ADJUST_MINSIZE, 3)
        __lbl_doc_type = wx.StaticText(self, -1, _("Type:"))
        __szr_top_middle.Add(__lbl_doc_type, 0, wx.LEFT|wx.TOP|wx.ADJUST_MINSIZE, 3)
        __szr_top_middle.Add(self._SelBOX_doc_type, 0, wx.LEFT|wx.EXPAND|wx.ADJUST_MINSIZE, 3)
        __lbl_doc_comment = wx.StaticText(self, -1, _("Comment:"))
        __szr_top_middle.Add(__lbl_doc_comment, 0, wx.LEFT|wx.TOP|wx.ADJUST_MINSIZE, 3)
        __szr_top_middle.Add(self._TBOX_doc_comment, 0, wx.LEFT|wx.EXPAND|wx.ADJUST_MINSIZE, 3)
        __lbl_doc_date = wx.StaticText(self, -1, _("Date of creation:"))
        __szr_top_middle.Add(__lbl_doc_date, 0, wx.LEFT|wx.TOP|wx.ADJUST_MINSIZE, 3)
        __szr_top_middle.Add(self._PhWheel_doc_date, 0, wx.LEFT|wx.EXPAND|wx.ADJUST_MINSIZE, 3)
        __szr_top_middle.Add(self.__lbl_reviewer, 0, wx.LEFT|wx.TOP|wx.ADJUST_MINSIZE, 3)
        __szr_top_middle.Add(self._PhWheel_reviewer, 0, wx.LEFT|wx.EXPAND|wx.ADJUST_MINSIZE, 3)
        __szr_top_middle.Add(self._ChBOX_reviewed, 0, wx.LEFT|wx.TOP|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 3)
        __szr_top_middle.Add(self._ChBOX_abnormal, 0, wx.LEFT|wx.ADJUST_MINSIZE, 9)
        __szr_top_middle.Add(self._ChBOX_relevant, 0, wx.LEFT|wx.ADJUST_MINSIZE, 9)
        __szr_top_third.Add(__szr_top_middle, 1, wx.LEFT|wx.EXPAND|wx.ADJUST_MINSIZE, 5)
        __szr_top_right.Add(self._LBOX_doc_pages, 1, wx.LEFT|wx.EXPAND|wx.ADJUST_MINSIZE, 3)
        __szr_page_actions.Add(self.__btn_show_page, 0, wx.ADJUST_MINSIZE, 0)
        __szr_page_actions.Add(self.__btn_del_page, 0, wx.ADJUST_MINSIZE, 0)
        __szr_top_right.Add(__szr_page_actions, 0, wx.TOP|wx.EXPAND, 4)
        __szr_top_third.Add(__szr_top_right, 1, wx.LEFT|wx.EXPAND|wx.ADJUST_MINSIZE, 5)
        __szr_main.Add(__szr_top_third, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 5)
        __szr_main.Add(self._TBOX_description, 1, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 5)
        __szr_bottom_third.Add(self.__btn_save, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        __szr_bottom_third.Add(self.__btn_discard, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        __szr_main.Add(__szr_bottom_third, 0, wx.LEFT|wx.BOTTOM|wx.EXPAND|wx.ADJUST_MINSIZE, 5)
        self.SetAutoLayout(True)
        self.SetSizer(__szr_main)
        __szr_main.Fit(self)
        __szr_main.SetSizeHints(self)
        # end wxGlade

    def _scan_btn_pressed(self, event): # wxGlade: wxgScanIdxPnl.<event_handler>
        print "Event handler `_scan_btn_pressed' not implemented!"
        event.Skip()

    def _reviewed_box_checked(self, event): # wxGlade: wxgScanIdxPnl.<event_handler>
        print "Event handler `_reviewed_box_checked' not implemented!"
        event.Skip()

    def _show_btn_pressed(self, event): # wxGlade: wxgScanIdxPnl.<event_handler>
        print "Event handler `_show_btn_pressed' not implemented!"
        event.Skip()

    def _del_btn_pressed(self, event): # wxGlade: wxgScanIdxPnl.<event_handler>
        print "Event handler `_del_btn_pressed' not implemented!"
        event.Skip()

    def _save_btn_pressed(self, event): # wxGlade: wxgScanIdxPnl.<event_handler>
        print "Event handler `_save_btn_pressed' not implemented!"
        event.Skip()

    def _startover_btn_pressed(self, event): # wxGlade: wxgScanIdxPnl.<event_handler>
        print "Event handler `_startover_btn_pressed' not implemented!"
        event.Skip()

    def _on_load_btn_pressed(self, event): # wxGlade: wxgScanIdxPnl.<event_handler>
        print "Event handler `_on_load_btn_pressed' not implemented"
        event.Skip()

    def _load_btn_pressed(self, event): # wxGlade: wxgScanIdxPnl.<event_handler>
        print "Event handler `_load_btn_pressed' not implemented"
        event.Skip()

# end of class wxgScanIdxPnl


