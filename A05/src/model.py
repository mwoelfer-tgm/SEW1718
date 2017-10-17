import requests
import xml.etree.ElementTree as ET

class Model:
    def __init__(self):
        """
        No member attributes need to be created
        """
        pass

    def get_route(self, start, destination, is_xml):
        """
        Creates a query to the google drive API, either parses the XML or JSON File
        :param start: the string which holds the information where the route is to be started
        :param destination: the string which holds the information where the route ends
        :param is_xml: boolean which determines whether a XML or JSON file is to be requested
        :return: A html-formatted string where the route is described and a status for the GUI
        """
        output = ""
        if is_xml:
            # GET is used because no information is posted, only received
            # important: the parameter mode=driving and language=de might seem unnecessary, but its important
            # that these are at the beginning to prevent injection-strings, for example 'Jägerstraße&mode=walking'
            response = requests.get(
                url="https://maps.googleapis.com/maps/api/directions/xml?mode=driving&language=de&origin=%s&destination=%s" % (
                    start, destination))
            # get the root element of the XML structure
            xml_data = ET.fromstring(response.text)
            # get the status, which is the first child element
            status = xml_data[0].text
            # check for certain statuses, and return if certain where returned
            if status == 'NOT_FOUND' or status == 'INVALID_REQUEST' or status == 'ZERO_RESULTS':
                return [output, "Es wurde der Status %s zurückgegeben, Eingabe überprüfen!" % (status)]
            else:
                status_ok = "Berechnung Ok!"

            # get the legend
            leg = xml_data[1][1]
            # from the legend extract the information how long the trip is in duration and distance
            output += "<p>Die Gesamtdauer beträgt <b>%s</b>, die Gesamtentfernung: <b>%s</b> </p>" % (
                leg.find('duration')[1].text, leg.find('distance')[1].text)
            
            # iterate through all steps in the legend
            for step in leg.findall('step'):
                # append the html_instruction, distance and duration information to the output string
                output += "%s, Entfernung %s, Dauer %s <br>" % (
                step.find('html_instructions').text, step.find('distance')[1].text, step.find('duration')[1].text)
            # return the route information and the status
            return [output, status_ok]
        else:
            # request json response
            response = requests.get(
                url="https://maps.googleapis.com/maps/api/directions/json?mode=driving&language=de&origin=%s&destination=%s" % (
                start, destination))
            # the requests module is able to convert json into a dictionary which is more easy to work with
            json_data = response.json()
            status = json_data["status"]
            # again check for certain statuses and return if a bad one was returned
            if status == 'NOT_FOUND' or status == 'INVALID_REQUEST' or status == 'ZERO_RESULTS':
                return [output, "Es wurde der Status %s zurückgegeben, Eingabe überprüfen!" % (status)]
            else:
                status_ok = "Berechnung Ok!"
            
            # get the legend information
            legs = json_data["routes"][0]["legs"][0]
            # get all steps
            steps = legs["steps"]
            # also extract the total duration and distance for the route from the legend
            output += "<p>Die Gesamtdauer beträgt <b>%s</b>, die Gesamtentfernung: <b>%s</b> </p>" % (legs["duration"]["text"], legs["distance"]["text"])

            # iterate through the steps
            for step in steps:
                # append the html_instructions, distance and duration to the output string
                output += "%s, Entfernung %s, Dauer %s <br>" % (step["html_instructions"], step["distance"]["text"], step["duration"]["text"])
            # return the route string and the status
            return [output, status_ok]