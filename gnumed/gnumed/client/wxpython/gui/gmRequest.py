"""This is a basic requests panel.

Status: hacking

    Copyright (C) 2004 Ian Haywood

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""
__author__ = "Ian Haywood <ihaywood@gnu.org>"

from Gnumed.wxpython import gmPlugin, gmGuiHelpers
from Gnumed.business import gmForms
from Gnumed.wxpython.gmPhraseWheel import cPhraseWheel
from Gnumed.pycommon import gmLog

if __name__ == '__main__':
	_ = lambda x:x

# generated by wxGlade 0.3.3 on Tue Jun 15 13:29:57 2004

import wx

class RequestsPanel(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: RequestsPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.label_1 = wxStaticText(self, -1, _("Type"))
        self.wheel_type = cPhraseWheel(self, -1, "")
        self.label_2 = wxStaticText(self, -1, _("Form"))
        self.wheel_form = cPhraseWheel(self, -1, "")
        self.label_3 = wxStaticText(self, -1, _("Request"))
        self.text_ctrl_request = wx.TextCtrl(self, -1, "")
        self.label_4 = wxStaticText(self, -1, _("Clinical"))
        self.text_ctrl_clinical = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER|wx.TE_MULTILINE)
        self.label_5 = wxStaticText(self, -1, _("Instructions"))
        self.text_ctrl_instructions = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER|wx.TE_MULTILINE)
        self.button_OK = wx.Button(self, -1, _("OK"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: RequestsPanel.__set_properties
        pass
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: RequestsPanel.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wxFlexGridSizer(5, 2, 0, 0)
        grid_sizer_1.Add(self.label_1, 0, 0, 0)
        grid_sizer_1.Add(self.wheel_type, 0, wxEXPAND, 0)
        grid_sizer_1.Add(self.label_2, 0, 0, 0)
        grid_sizer_1.Add(self.wheel_form, 0, wxEXPAND, 0)
        grid_sizer_1.Add(self.label_3, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_request, 0, wxEXPAND, 0)
        grid_sizer_1.Add(self.label_4, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_clinical, 0, wxEXPAND, 0)
        grid_sizer_1.Add(self.label_5, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_instructions, 0, wxEXPAND, 0)
        grid_sizer_1.AddGrowableRow(3)
        grid_sizer_1.AddGrowableRow(4)
        grid_sizer_1.AddGrowableCol(1)
        sizer_1.Add(grid_sizer_1, 1, wxEXPAND, 0)
        sizer_1.Add(self.button_OK, 0, wxALIGN_CENTER_HORIZONTAL, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        # end wxGlade

# end of class RequestsPanel




class cActiveRequestsPanel (RequestsPanel):
    """
    A descendant of the autogenerated class to add activity
    """
    def __init__ (self, parent, id):
        RequestsPanel.__init__ (self, parent, id)
        self.wheel_type.matcher = gmForms.FormTypeMP()
        self.wheel_form.matcher = gmForms.FormMP()
        wx.EVT_BUTTON (self.button_OK, self.button_OK.GetId (), self._ok_pressed)

    def _ok_pressed (self, event):
        form_id = self.wheel_form.getData ()
        print "Form id: %s" % form_id
        type_id = self.wheel_type.getData ()
        print "Type : %s" % type_id
        if form_id and type_id:
            try:
                form = gmForms.get_form (form_id)
                params = {}
                params['type'] = self.wheel_type.GetValue ()
                params['request'] = self.text_ctrl_request.GetValue ()
                params['clinical_notes'] = self.text_ctrl_clinical.GetValue ()
                params['instructions'] = self.text_ctrl_instructions.GetValue ()
                form.store (params)
                form.process (params)
                form.printout ()
            except gmForms.FormError, e:
                gmGuiHelpers.gm_show_error (str(e), _("Error processing form"))
            except:
                gmLog.gmDefLog.LogException( "forms printing", sys.exc_info(), verbose=0)
        else:
            gmGuiHelpers.gm_show_error (_("You must slect a form and type"), _("Missing field"))
            
            


class gmRequest (gmPlugin.cNotebookPluginOld):

    tab_name = _("Request")

    def name (self):
        return gmRequest.tab_name

    def MenuInfo (self):
        return ("view", _("&Request"))

    def GetWidget (self, parent):
        return cActiveRequestsPanel (parent, -1)

    def can_receive_focus(self):
        # need patient
        if not self._verify_patient_avail():
            return None
        return 1
