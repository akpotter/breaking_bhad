#!/usr/bin/python
import sys
import base64

request = """POST /upnp/control/rules1 HTTP/1.1\r\nSOAPAction: "urn:Belkin:service:rules:1#GetRulesDBVersion"\r\nHost: 192.168.1.143:49153\r\nContent-Type: text/xml\r\nContent-Length: 306\r\n\r\n<?xml version="1.0"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<SOAP-ENV:Body>
	<m:GetRulesDBVersion xmlns:m="urn:Belkin:service:rules:1">

	</m:GetRulesDBVersion>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>
"""
sys.stdout.write(request)
