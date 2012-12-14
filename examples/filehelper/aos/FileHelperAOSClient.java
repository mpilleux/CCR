/*******************************************************************************
 * ALMA - Atacama Large Millimeter Array
 * Copyright (c) AUI - Associated Universities Inc., 2011
 * (in the framework of the ALMA collaboration).
 * All rights reserved.
 * 
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 * 
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA
 *******************************************************************************/
package cl.alma.adc.sw.ws.clients.filehelper.aos;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.rmi.RemoteException;
import java.util.Properties;
import java.util.logging.Logger;

import cl.alma.adc.sw.ws.clients.filehelper.FileHelperSTEClient;

public class FileHelperAOSClient implements FileHelperSTEClient {
	Logger logger = Logger.getLogger("FileHelperAOSClient");
	
	
	public String getConnectionString() {
		String property = "archive.tmcdb.connection";
		return getPropertiesFromPropertyFile(property);
	}

	
	
	public String getConnectionLogin() {
		String property = "archive.tmcdb.user";
		return getPropertiesFromPropertyFile(property);
	}

	
	
	public String getConnectionPassword() {
		String property = "archive.tmcdb.passwd";
		return getPropertiesFromPropertyFile(property);
	}

	
	
	public String getPropertiesFromPropertyFile(String property) {
		try {
			String archiveConfigPropertiesString = getArchiveConfigProperties();
			Properties properties = new Properties();
			ByteArrayInputStream archiveConfigPropertiesInputStream = new ByteArrayInputStream(
					archiveConfigPropertiesString.getBytes());
			properties.load(archiveConfigPropertiesInputStream);
			archiveConfigPropertiesInputStream.close();
			String value = properties.getProperty(property);
			return value;
		} catch (IOException e) {
			e.printStackTrace();
			return null;
		}
	}

	
	
	public String getArchiveConfigProperties() {
		try {
			String filename = "/alma/ACS-current/acsdata/config/archiveConfig.properties";
			String hostname = "gns";

			FileHelperStub client = null;
			FileHelperStub.GetFile request = null;
			FileHelperStub.GetFileResponse response = null;

			client = new FileHelperStub();
			request = new FileHelperStub.GetFile();
			request.setArgs0(filename);
			request.setArgs1(hostname);
			response = client.getFile(request);

			String archiveProperties = response.get_return();
			return archiveProperties;
		} catch (RemoteException excepcionDeInvocacion) {
			logger.info("Problem creating FileHandle SW Client.");
			System.err.println(excepcionDeInvocacion.toString());
			return null;
		} catch (ExceptionException e) {
			e.printStackTrace();
			return null;
		}
	}

/*		public static void main(String[] args) throws Exception {
		FileHelperAOSClient c = new FileHelperAOSClient();
		String passwd = c.getPropertiesFromPropertyFile("archive.tmcdb.passwd");
		String login = c.getPropertiesFromPropertyFile("archive.tmcdb.user");
		String url = c.getPropertiesFromPropertyFile("archive.tmcdb.connection");
		c.logger.info(passwd);
		c.logger.info(login);
		c.logger.info(url);
	}
*/
}
