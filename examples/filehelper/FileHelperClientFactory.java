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
/**
 * 
 */
package cl.alma.adc.sw.ws.clients.filehelper;

import cl.alma.adc.sw.ws.clients.filehelper.aos.FileHelperAOSClient;
import cl.alma.adc.sw.ws.clients.filehelper.sco.FileHelperSCOClient;
import cl.alma.adc.sw.ws.clients.filehelper.tfeng.FileHelperTFENGClient;
import cl.alma.adc.sw.ws.clients.filehelper.tfint.FileHelperTFINTClient;
import cl.alma.adc.sw.ws.clients.filehelper.tfohg.FileHelperTFOHGClient;
import cl.alma.adc.sw.ws.clients.filehelper.tfsd.FileHelperTFSDClient;

/**
 * @author nsaez
 * 
 */
public class FileHelperClientFactory {

	public FileHelperSTEClient getClient(String steName) {

		if (steName.equalsIgnoreCase("AOS")) {
			FileHelperAOSClient client = new FileHelperAOSClient();
			return client;
		}
		
		if (steName.equalsIgnoreCase("TFENG")) {
			FileHelperTFENGClient client = new FileHelperTFENGClient();
			return client;
		}
		
		if (steName.equalsIgnoreCase("TFINT")) {
			FileHelperTFINTClient client = new FileHelperTFINTClient();
			return client;
		}
		
		if (steName.equalsIgnoreCase("TFSD")) {
			FileHelperTFSDClient client = new FileHelperTFSDClient();
			return client;
		}
		
		if (steName.equalsIgnoreCase("TFOHG")) {
			FileHelperTFOHGClient client = new FileHelperTFOHGClient();
			return client;
		}
		
		if (steName.equalsIgnoreCase("SCO")) {
			FileHelperSCOClient client = new FileHelperSCOClient();
			return client;
		}
		
		return null;
	}
}
