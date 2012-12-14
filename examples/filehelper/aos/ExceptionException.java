
/**
 * ExceptionException.java
 *
 * This file was auto-generated from WSDL
 * by the Apache Axis2 version: 1.5.5  Built on : May 28, 2011 (08:30:56 CEST)
 */

package cl.alma.adc.sw.ws.clients.filehelper.aos;

public class ExceptionException extends java.lang.Exception{
    
    private cl.alma.adc.sw.ws.clients.filehelper.aos.FileHelperStub.ExceptionE faultMessage;

    
        public ExceptionException() {
            super("ExceptionException");
        }

        public ExceptionException(java.lang.String s) {
           super(s);
        }

        public ExceptionException(java.lang.String s, java.lang.Throwable ex) {
          super(s, ex);
        }

        public ExceptionException(java.lang.Throwable cause) {
            super(cause);
        }
    

    public void setFaultMessage(cl.alma.adc.sw.ws.clients.filehelper.aos.FileHelperStub.ExceptionE msg){
       faultMessage = msg;
    }
    
    public cl.alma.adc.sw.ws.clients.filehelper.aos.FileHelperStub.ExceptionE getFaultMessage(){
       return faultMessage;
    }
}
    