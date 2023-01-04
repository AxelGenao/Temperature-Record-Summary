from abc import ABC, abstractmethod
import json

class TemperatureRecordSummary(ABC):
    temperatureData = {}

    def template_method(self):

        self.readfile()
        self.findMin()
        self.findMax()
        self.findAverage()


        @abstractmethod
        def readfile(self):
           print("La clase Abstract dice: estoy haciendo el bulk del trabajo")

        def findMin(self):
            print("I find the min temp")

        def findMax(self):
            print("I find the max temp")
        
        def findAverage(self):
            print("I find the average temp")

class ReadJSonFile(TemperatureRecordSummary):
    
    def readfile(self):
        rawJson = open("data.json")
        content = json.load(rawJson)
        print(content[0]['meassure'])

def client_code(abstract_class: TemperatureRecordSummary):

    abstract_class.template_method()

client_code(ReadJSonFile())

class ReadFlatFile(TemperatureRecordSummary):

    def readfile(self):
        rawFlat = open("data.Flat")
        content = json.load(rawFlat)
        print(content[0]['meassure'])

def client_code(abstract_class: TemperatureRecordSummary):

    abstract_class.template_method()

client_code(ReadFlatFile())

class ReadXMLFile(TemperatureRecordSummary):

    def readfile(self):
        rawXML = open("data.XML")
        content = json.load(rawXML)
        print(content[0]['meassure'])

def client_code(abstract_class: TemperatureRecordSummary):

    abstract_class.template_method()

client_code(ReadFlatFile())