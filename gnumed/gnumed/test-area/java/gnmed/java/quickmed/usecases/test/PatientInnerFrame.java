/*
 * PatientInnerFrame.java
 *
 * Created on 1 August 2003, 19:30
 */

package quickmed.usecases.test;
import org.gnumed.gmIdentity.*;
import java.util.*;

/**
 *
 * @author  sjtan
 */
public class PatientInnerFrame extends javax.swing.JInternalFrame {
    final static String TERMS = "SummaryTerms";
    /** Creates new form PatientInnerFrame */
    SummaryPanel summaryPanel1;
    public PatientInnerFrame() {
        initComponents();
        addViews();
    }
    
    void addViews() {
        summaryPanel1 = new SummaryPanel();
        jScrollPane1.setViewportView(summaryPanel1);
        pack();
    }
    
    /** This method is called from within the constructor to
     * initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is
     * always regenerated by the Form Editor.
     */
    private void initComponents() {//GEN-BEGIN:initComponents
        jScrollPane1 = new javax.swing.JScrollPane();

        setClosable(true);
        setIconifiable(true);
        setMaximizable(true);
        setResizable(true);
        setTitle("Medical Record");
        addInternalFrameListener(new javax.swing.event.InternalFrameListener() {
            public void internalFrameActivated(javax.swing.event.InternalFrameEvent evt) {
            }
            public void internalFrameClosed(javax.swing.event.InternalFrameEvent evt) {
                onCloseFinalizeIdentity(evt);
            }
            public void internalFrameClosing(javax.swing.event.InternalFrameEvent evt) {
                formInternalFrameClosing(evt);
            }
            public void internalFrameDeactivated(javax.swing.event.InternalFrameEvent evt) {
            }
            public void internalFrameDeiconified(javax.swing.event.InternalFrameEvent evt) {
            }
            public void internalFrameIconified(javax.swing.event.InternalFrameEvent evt) {
            }
            public void internalFrameOpened(javax.swing.event.InternalFrameEvent evt) {
            }
        });

        getContentPane().add(jScrollPane1, java.awt.BorderLayout.CENTER);

        pack();
    }//GEN-END:initComponents
    
    private void formInternalFrameClosing(javax.swing.event.InternalFrameEvent evt) {//GEN-FIRST:event_formInternalFrameClosing
        // Add your handling code here:
        summaryPanel1.transferFormToModel();
        try {
            ( (ManagerReference)summaryPanel1.getIdentity().getPersister()).setConnected(true);
            
        } catch (Exception e) {
           System.out.println(e);
        }
        gnmed.test.DomainPrinter.getInstance().printIdentity( System.out, summaryPanel1.getIdentity());
        try {
            ((ManagerReference)summaryPanel1.getIdentity().getPersister()).getIdentityManager().save(summaryPanel1.getIdentity());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }//GEN-LAST:event_formInternalFrameClosing
    
    private void onCloseFinalizeIdentity(javax.swing.event.InternalFrameEvent evt) {//GEN-FIRST:event_onCloseFinalizeIdentity
        
    }//GEN-LAST:event_onCloseFinalizeIdentity
    
    /** Getter for property identity.
     * @return Value of property identity.
     *
     */
    public identity getIdentity() {
        if (summaryPanel1 == null)
            return null;
        return summaryPanel1.getIdentity();
    }
    
    /** Setter for property identity.
     * @param identity New value of property identity.
     *
     */
    public void setIdentity(identity identity) {
        
        summaryPanel1.setIdentity(identity);
        
        changeTitle();
    }
    
    void changeTitle() {
        if (getIdentity() != null && getIdentity().getNamess().size() >0) {
            Iterator j =  getIdentity().getNamess().iterator();
            if ( j.hasNext()) {
                Names n = (Names) j.next();
                
                StringBuffer sb = new StringBuffer();
                
                sb.append(n.getFirstnames() ).append(' ').append( n.getLastnames()).
                append(' ').append(ResourceBundle.getBundle(TERMS).getString("born") ).
                append(' ').
                append(java.text.DateFormat.getDateInstance(java.text.DateFormat.MEDIUM)
                .format(getIdentity().getDob()) ).
                append(", ").
                append( ResourceBundle.getBundle(TERMS).getString("medical_record") );
                
                setTitle(sb.toString());
            }
        }
    }
    
    /** Getter for property demographicsFrozen.
     * @return Value of property demographicsFrozen.
     *
     */
    public boolean isDemographicsFrozen() {
        return summaryPanel1.isDemographicsFrozen();
    }
    
    /** Setter for property demographicsFrozen.
     * @param demographicsFrozen New value of property demographicsFrozen.
     *
     */
    public void setDemographicsFrozen(boolean demographicsFrozen) {
        summaryPanel1.setDemographicsFrozen(demographicsFrozen);
    }
    
    //
    //    public String getTitle() {
    //        if (getIdentity() != null) {
    //
    //        }
    //        return ResourceBundle.getBundle(TERMS).getString("medical_record");
    //    }
    
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JScrollPane jScrollPane1;
    // End of variables declaration//GEN-END:variables
    
    
}
