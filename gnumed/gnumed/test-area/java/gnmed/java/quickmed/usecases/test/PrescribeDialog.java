/*
 * PrescribeDialog.java
 *
 * Created on 4 August 2003, 10:20
 */

package quickmed.usecases.test;
import javax.swing.event.*;
import java.awt.event.KeyEvent;
import java.awt.KeyboardFocusManager;
import javax.swing.*;
import java.util.*;
import org.drugref.*;
/**
 *
 * @author  sjtan
 */
public class PrescribeDialog extends javax.swing.JDialog implements SearchSelectable {
    TestScriptDrugManager manager = TestScriptDrugManager.instance();
    
    public PrescribeDialog(java.awt.Frame parent, boolean modal, Ref ref) {
     this( parent, modal);
     setManagerRef(ref);
    }
    /** Creates new form PrescribeDialog */
    public PrescribeDialog(java.awt.Frame parent, boolean modal) {
        super(parent, modal);
        initComponents();
//        initController();
//        Set set = new HashSet();
//        set.addAll(jList1.getFocusTraversalKeys(KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS));
//        set.add( KeyStroke.getKeyStroke(KeyEvent.VK_DOWN, 0) );
//        jList1.setFocusTraversalKeys(KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS, set );
     
    }
    
    class ListUpdateDocumentListener implements  javax.swing.event.DocumentListener {
        
        void checkText( DocumentEvent e ) {
            if (e.getDocument().getLength() < 3)
                return;
            try {
                jList1.setModel( new DefaultListModel());
                
                List l =   getDrugManager().findPackagedProductByDrugName(e.getDocument().getText(0, e.getDocument().getLength()));
//                l.add(0, e.getDocument().getText(0, e.getDocument().getLength()));
                jList1.setListData(l.toArray());
//                List outList = new ArrayList();
//                for (int i = 0; i < l.size(); ++i) {
//                    StringBuffer sb = new StringBuffer();
//                    
//                    product p = (product) l.get(i);
//                    generic_drug_name gn = (generic_drug_name) p.getDrug_element().getGeneric_name().iterator() .next();
//                    sb.append( gn.getName());
//                    sb.append(": ");
//                    sb.append(p.getComment());
//                    sb.append(", ");
//                  
//                    for (Iterator  j=  p.getPackage_sizes().iterator(); j.hasNext();) {
//                        sb.append( gn.getName());
//                        sb.append("  ");
//                        
//                        sb.append('\t');
//                        package_size pz = (package_size) j.next();
//                        sb.append("sz=");
//                        sb.append(pz.getSize());
//                        sb.append(" ");
//                    }
//                      sb.append("\t\n");
//                    outList.add(sb.toString());
//                    
//                }
//                jList1.setListData(outList.toArray());
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
        
        public void changedUpdate(DocumentEvent e) {
            checkText( e );
        }
        
        public void insertUpdate(DocumentEvent e) {
            checkText( e );
        }
        
        public void removeUpdate(DocumentEvent e) {
            checkText( e );
        }
        
    }
    
    public Object getSelectedItem() {
        return jList1.getSelectedValue();
    }
    
    /**
     *adds the typing search listener.
     */
    void initController() {
        jTextField1.getDocument().addDocumentListener(new PrescribeDialog.ListUpdateDocumentListener());
        
    }
    /** This method is called from within the constructor to
     * initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is
     * always regenerated by the Form Editor.
     */
    private void initComponents() {//GEN-BEGIN:initComponents
        java.awt.GridBagConstraints gridBagConstraints;

        jLabel1 = new javax.swing.JLabel();
        jTextField1 = new javax.swing.JTextField();
        jButton1 = new javax.swing.JButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        jList1 = new javax.swing.JList();

        getContentPane().setLayout(new java.awt.GridBagLayout());

        setTitle("Find Drug");
        setLocationRelativeTo(this);
        setModal(true);
        addComponentListener(new java.awt.event.ComponentAdapter() {
            public void componentShown(java.awt.event.ComponentEvent evt) {
                formComponentShown(evt);
            }
        });
        addWindowListener(new java.awt.event.WindowAdapter() {
            public void windowClosing(java.awt.event.WindowEvent evt) {
                closeDialog(evt);
            }
        });

        jLabel1.setText("drug");
        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.fill = java.awt.GridBagConstraints.HORIZONTAL;
        gridBagConstraints.weightx = 1.0;
        getContentPane().add(jLabel1, gridBagConstraints);

        jTextField1.setText("jTextField1");
        jTextField1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jTextField1ActionPerformed(evt);
            }
        });
        jTextField1.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyPressed(java.awt.event.KeyEvent evt) {
                jTextField1KeyPressed(evt);
            }
            public void keyTyped(java.awt.event.KeyEvent evt) {
                jTextField1KeyTyped(evt);
            }
        });

        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.fill = java.awt.GridBagConstraints.HORIZONTAL;
        gridBagConstraints.weightx = 1.0;
        getContentPane().add(jTextField1, gridBagConstraints);

        jButton1.setText("clear");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });

        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.gridwidth = java.awt.GridBagConstraints.REMAINDER;
        getContentPane().add(jButton1, gridBagConstraints);

        jList1.setSelectionMode(javax.swing.ListSelectionModel.SINGLE_SELECTION);
        jList1.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyPressed(java.awt.event.KeyEvent evt) {
                jList1KeyPressed(evt);
            }
        });
        jList1.addListSelectionListener(new javax.swing.event.ListSelectionListener() {
            public void valueChanged(javax.swing.event.ListSelectionEvent evt) {
                jList1ValueChanged(evt);
            }
        });
        jList1.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jList1MouseClicked(evt);
            }
        });

        jScrollPane1.setViewportView(jList1);

        gridBagConstraints = new java.awt.GridBagConstraints();
        gridBagConstraints.gridwidth = java.awt.GridBagConstraints.REMAINDER;
        gridBagConstraints.fill = java.awt.GridBagConstraints.BOTH;
        gridBagConstraints.weightx = 1.0;
        gridBagConstraints.weighty = 1.0;
        getContentPane().add(jScrollPane1, gridBagConstraints);

        pack();
    }//GEN-END:initComponents

    private void formComponentShown(java.awt.event.ComponentEvent evt) {//GEN-FIRST:event_formComponentShown
        // Add your handling code here:
        try {
        jList1.setSelectedIndex(0);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }//GEN-LAST:event_formComponentShown

    private void jList1MouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_jList1MouseClicked
        // Add your handling code here:
        if ( evt.getClickCount() == 2) {
            setVisible(false);
        }
    }//GEN-LAST:event_jList1MouseClicked

    private void jList1ValueChanged(javax.swing.event.ListSelectionEvent evt) {//GEN-FIRST:event_jList1ValueChanged
//        // Add your handling code here:
//        setVisible(false);
    }//GEN-LAST:event_jList1ValueChanged

    private void jList1KeyPressed(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_jList1KeyPressed

        // Add your handling code here:
        if ( evt.getKeyCode() == evt.VK_UP && jList1.getSelectedIndex() == 0) {
            jList1.transferFocus();
            jTextField1.requestFocusInWindow();
        }
        if (evt.getKeyCode() == evt.VK_ENTER)
            setVisible(false);
    }//GEN-LAST:event_jList1KeyPressed

    private void jTextField1KeyPressed(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_jTextField1KeyPressed

        
        // Add your handling code here:
//        System.out.println("char"+ evt.getKeyChar() + " loc="+ evt.getKeyLocation() + " code="+ evt.getKeyCode() + " **");
        if (evt.getKeyCode() == evt.VK_DOWN) {
        
            jTextField1.transferFocus();
                jList1.requestFocusInWindow();
        }
    }//GEN-LAST:event_jTextField1KeyPressed

    private void jTextField1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jTextField1ActionPerformed
        // Add your handling code here:
        String text = jTextField1.getText();
         if (text == null || text.trim().equals("") || text.trim().equals("%") )
            return;
        try {
        List l =   getDrugManager().findPackagedProductByDrugName(jTextField1.getText());
//                l.add(0, e.getDocument().getText(0, e.getDocument().getLength()));
        jList1.setListData(l.toArray());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }//GEN-LAST:event_jTextField1ActionPerformed

    private void jTextField1KeyTyped(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_jTextField1KeyTyped
        // Add your handling code here:
     
    }//GEN-LAST:event_jTextField1KeyTyped
    
    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        // Add your handling code here:
        jTextField1.setText("");
    }//GEN-LAST:event_jButton1ActionPerformed
    
    /** Closes the dialog */
    private void closeDialog(java.awt.event.WindowEvent evt) {//GEN-FIRST:event_closeDialog
        setVisible(false);
        dispose();
    }//GEN-LAST:event_closeDialog
    
    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) throws Exception {
       
        new PrescribeDialog(new javax.swing.JFrame(), true).show();
    }
    
    public void setSearchText(java.lang.String text) {
        jTextField1.setText(text);
        jTextField1ActionPerformed(new java.awt.event.ActionEvent(jTextField1, 1, "search"));
    }    
    
    /** Getter for property managerRef.
     * @return Value of property managerRef.
     *
     */
    public Ref getManagerRef() {
        return this.managerRef;
    }
    
    /** Setter for property managerRef.
     * @param managerRef New value of property managerRef.
     *
     */
    public void setManagerRef(Ref managerRef) {
        this.managerRef = managerRef;
    }
    
    /** Getter for property drugManager.
     * @return Value of property drugManager.
     *
     */
    public TestScriptDrugManager getDrugManager() {
        if (getManagerRef() != null) {
            java.util.logging.Logger.global.info("MANAGER IS " + getManagerRef().getClass());
            return ( ( ManagerReference) getManagerRef().getRef()).getScriptDrugManager();
        }
        return manager;
    }
    
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jButton1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JList jList1;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTextField jTextField1;
    // End of variables declaration//GEN-END:variables

    /** Holds value of property managerRef. */
    private Ref managerRef;    
    
}
