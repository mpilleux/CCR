
/**
 * FileHelperCallbackHandler.java
 *
 * This file was auto-generated from WSDL
 * by the Apache Axis2 version: 1.5.5  Built on : May 28, 2011 (08:30:56 CEST)
 */

    package cl.alma.adc.sw.ws.clients.filehelper.aos;

    /**
     *  FileHelperCallbackHandler Callback class, Users can extend this class and implement
     *  their own receiveResult and receiveError methods.
     */
    public abstract class FileHelperCallbackHandler{



    protected Object clientData;

    /**
    * User can pass in any object that needs to be accessed once the NonBlocking
    * Web service call is finished and appropriate method of this CallBack is called.
    * @param clientData Object mechanism by which the user can pass in user data
    * that will be avilable at the time this callback is called.
    */
    public FileHelperCallbackHandler(Object clientData){
        this.clientData = clientData;
    }

    /**
    * Please use this constructor if you don't want to set any clientData
    */
    public FileHelperCallbackHandler(){
        this.clientData = null;
    }

    /**
     * Get the client data
     */

     public Object getClientData() {
        return clientData;
     }

        
           /**
            * auto generated Axis2 call back method for getFile method
            * override this method for handling normal response from getFile operation
            */
           public void receiveResultgetFile(
                    cl.alma.adc.sw.ws.clients.filehelper.aos.FileHelperStub.GetFileResponse result
                        ) {
           }

          /**
           * auto generated Axis2 Error handler
           * override this method for handling error response from getFile operation
           */
            public void receiveErrorgetFile(java.lang.Exception e) {
            }
                
           /**
            * auto generated Axis2 call back method for existsFile method
            * override this method for handling normal response from existsFile operation
            */
           public void receiveResultexistsFile(
                    cl.alma.adc.sw.ws.clients.filehelper.aos.FileHelperStub.ExistsFileResponse result
                        ) {
           }

          /**
           * auto generated Axis2 Error handler
           * override this method for handling error response from existsFile operation
           */
            public void receiveErrorexistsFile(java.lang.Exception e) {
            }
                


    }
    