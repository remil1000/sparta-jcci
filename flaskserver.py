from flask import Flask, Response
from flask_cors import CORS, cross_origin
from xml.etree import ElementTree as ET
import json
import os
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
import logging

import socket

app = Flask(__name__)

SPARTA_DATA_DIR = os.getenv("SPARTA_DATA_DIR", 'data/')
APP_PORT = int(os.getenv('SPARTA_PORT', 5004))
SPARTA_EXPOSED_HOST = os.getenv('SPARTA_EXPOSED_HOST', socket.gethostname())
SPARTA_EXPOSED_PORT = os.getenv('SPARTA_EXPOSED_PORT', APP_PORT)
SPARTA_ORG = os.getenv('SPARTA_ORG', 'null')

@app.route('/getCapabilities')
@cross_origin()
def getCapabilities():
	result = jsondata2xmlresult("description.json", "getCapabilities")
	return Response(result, mimetype='text/xml')

@app.route('/getData')
@cross_origin()
def getData():
	result = jsondata2xmlresult("data.json", "getData")
	return Response(result, mimetype='text/xml')

@app.route('/getTools')
@cross_origin()
def getTools():
	result = jsondata2xmlresult("tools.json", "getTools")
	return Response(result, mimetype='text/xml')

@app.route('/getServices')
@cross_origin()
def getServices():
	result = jsondata2xmlresult("services.json", "getServices")
	return Response(result, mimetype='text/xml')

@app.route('/getInteraction')
@cross_origin()
def getInteracton():
	result = jsondata2xmlresult("interaction.json", "getInteraction")
	return Response(result, mimetype='text/xml')

@app.route('/getLearningData')
@cross_origin()
def getLearningData():
	result = jsondata2xmlresult("learning/learning_data.json", "getData")
	return Response(result, mimetype='text/xml')

@app.route('/getLearningTools')
@cross_origin()
def getLearningTools():
	result = jsondata2xmlresult("learning/learning_tools.json", "getTools")
	return Response(result, mimetype='text/xml')

@app.route('/getLearningServices')
@cross_origin()
def getLearningServices():
	result = jsondata2xmlresult("learning/learning_services.json", "getServices")
	return Response(result, mimetype='text/xml')

@app.route('/getLearningInteraction')
@cross_origin()
def getLearningInteracton():
	result = jsondata2xmlresult("learning/learning_interaction.json", "getInteraction")
	return Response(result, mimetype='text/xml')

def jsondata2xmlresult(path, method):
	json_path = os.path.join(SPARTA_DATA_DIR, path)
	data = readfromjson(json_path)
	info = json2xml.Json2xml(data,wrapper="datainfo", pretty=True, attr_type=False).to_xml()

	wadl_path = "wadl_capabilities.xml"
	tree = ET.parse(wadl_path)
	root = tree.getroot()

	res = tree.find('resources')
	res.set('base', f'{SPARTA_EXPOSED_HOST}:{SPARTA_EXPOSED_PORT}')
	res.set('name', SPARTA_ORG)

	for elem in root.iter('method'):
		if(elem.attrib['id'] == method):
			for ff in elem.iter('result'):
				ff.insert(1,ET.fromstring(info))

	result = ET.tostring(root, encoding='utf8', method='xml')
	return result

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=APP_PORT)
