/*
 * TestPrintPreviewInnerFrame.java
 *
 * Created on 3 September 2003, 22:53
 */

package quickmed.usecases.test;
import org.gnumed.gmIdentity.*;
import org.gnumed.gmClinical.link_script_drug;
import java.util.*;
import java.util.logging.*;
/**
 *
 * @author  syan
 */
public class TestPrintPreviewInnerFrame extends javax.swing.JInternalFrame {
    TestScriptPreviewPanel panel = new TestScriptPreviewPanel();
    /** Creates new form TestPrintPreviewInnerFrame */
    public TestPrintPreviewInnerFrame() {
        initComponents();
    }
    public TestPrintPreviewInnerFrame(identity patient, List link_script_drugs ) {
        initComponents();
        BasicScriptPrintable printable = new MedicareBasicScriptPrintable();
        printable.setPatient(patient);
        if (Globals.userIdentity != null)
            printable.setPrescriber(Globals.userIdentity);
        else 
            printable.setPrescriber(new identity());
        
        printable.setScriptDate(new Date());
        Logger.global.info("SETTING SCRIPT ITEMS = " + link_script_drugs + " size = " + link_script_drugs.size());
        printable.setScriptItems(link_script_drugs);
        panel.setBasicScriptPrintable(printable);
        setContentPane(panel);
	int width = 
	 (( MedicareBasicScriptPrintable)printable).getSplitWidth() ;
        setSize(width *2 , width * 2);
    }
    
    
    /** This method is called from within the constructor to
     * initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is
     * always regenerated by the Form Editor.
     */
    private void initComponents() {//GEN-BEGIN:initComponents

        setClosable(true);
        setIconifiable(true);
        setMaximizable(true);
        setResizable(true);
        setTitle(java.util.ResourceBundle.getBundle("SummaryTerms").getString("print_preview"));
        pack();
    }//GEN-END:initComponents
    
    
    // Variables declaration - do not modify//GEN-BEGIN:variables
    // End of variables declaration//GEN-END:variables
    
}
