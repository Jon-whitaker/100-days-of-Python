import json
import logging
import datetime
import requests
import sys
import aocsnow
from helper import log
import helper
import automationassets

global snow_instance,snow_username,snow_password,incident_assignment_group

snow_username = automationassets.get_automation_variable('snow_username_p2')
snow_password = automationassets.get_automation_variable('snow_password_p2')
snow_instance = automationassets.get_automation_variable('snow_instance_p2')

def format_alert_payload(inputObject, parameters):
    json_data = {}
    for parameter in parameters:
        for input in inputObject:
            if input['name'] == parameter:
                json_data[parameter] = input['value']
    return json_data


def get_ci_name(payload):
    start = payload.find("RequestBody")
    end = payload.find("RequestHeader")
    requestBody = payload[start+12:end-1]
    jsonbody = json.loads(str(requestBody))
    ci = format_alert_payload(jsonbody['data']['context']['condition']['allOf'][0]['dimensions'],['Computer'])
    ciname = ci['Computer']
    status = jsonbody['data']['status']
    return ciname, status

def analysis_ci(ci):
    #splan = 'high cpu'
    #ci = helper.Separate_ci_name(ci)
    log.info("Analysing SNOW for " + ci)
    auth_token = aocsnow.get_authtoken(snow_username,snow_password)
    #ci_cmdb = aocsnow.get_table(snow_instance,'cmdb_ci_server','name',ci,auth_token)                log.info("Creating incident......")
    ci_incident = aocsnow.create_incident_v3(
        snow_instance,
        'Not Used',
        str(ci),
        'Hardware',
        'cpu',
        '3',
        'High CPU ' + str(ci),
        'IBM-CDO-UK-Technology_Support',
        auth_token
    )


if __name__ == "__main__":
    
    payload = ''
    for index in range(len(sys.argv)):
        payload += str(sys.argv[index]).strip()
    ci, alert_status = get_ci_name(payload)
    if alert_status == 'Activated':
        analysis_ci(ci)
    else:               
        log.info('Alert trigger status is Deactivate')