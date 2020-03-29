'''
Created on 28 mar 2020

@author: maxx
'''
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
from threading import Thread
import test_data
import ujson
import main
import time

PORT_FOR_TEST = 16321

global_test_ok = {"/VSSZZZ6JZ9R056308" : {"ask" :test_data.test_1_data, "answer" : test_data.test_1_result},
               "/VSSZZZ6JZ9R056309" : {"ask" :test_data.test_2, "answer" : test_data.test_2},
               "/VSSZZZ6JZ9R056310" : {"ask" :test_data.test_3, "answer" : test_data.test_3}}


# this is test mock http server to test our REST-service. 
# I cannot test all errors kinds with CARFAX test server. 
class MockServerRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Process an HTTP GET request and return a response with an HTTP 200 status.
        self.send_response(requests.codes.ok)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        if (self.path == "/timeout"):
            # to test timeout error (code 3)
            time.sleep(15)
            return
        elif (self.path == "/VSSZZZ6JZ9R056312"):
            # to test wrong JSON format (code 4)
            self.wfile.write(ujson.encode(test_data.test_error1).encode('utf8')[1:])
            return
        elif (self.path == "/VSSZZZ6JZ9R056313"):
            # to test JSON format without required fields (code 5)
            self.wfile.write(ujson.encode(test_data.test_error2).encode('utf8'))
            return
        
        self.wfile.write(ujson.encode(global_test_ok[self.path]["ask"]).encode('utf8'))


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        '''
        running once per test
        '''
        #setup and run mock http server
        self.httpd = HTTPServer(('localhost', PORT_FOR_TEST), MockServerRequestHandler)
        self.thr1 = Thread(target=self.httpd.serve_forever)
        self.thr1.start()
        
        #setup and run our Flask REST service
        main.URL_main_service = "http://localhost:{}/".format(PORT_FOR_TEST)
        main.app.config['TESTING'] = True
        main.app.config['WTF_CSRF_ENABLED'] = False
        main.app.config['DEBUG'] = False
        self.app = main.app.test_client()
        
    @classmethod
    def tearDownClass(self):
        '''
        running once per test
        '''
        #clearing all resources
        self.httpd.server_close()
        self.httpd.shutdown()
        self.thr1.join()

    def testAllOK(self):
        '''
        running tests with success HTTP 200
        '''
        for key, val in global_test_ok.items():
            response = self.app.get('/get_info_by_vin' + key, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            dat = ujson.decode(response.data)
            dat["records"].sort(key=lambda x: x["date"])
            val["answer"]["records"].sort(key=lambda x: x["date"])
            self.maxDiff = None
            self.assertListEqual(dat["records"], val["answer"]["records"])

    def testErrors(self):
        '''
        running tests with errors HTTP 500
        '''
        print("It's timeout test. You should to wait 10 seconds. Please be patient.")
        response = self.app.get('/get_info_by_vin/timeout', follow_redirects=True)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(ujson.decode(response.data)["code"], 3)
        
        response = self.app.get('/get_info_by_vin/VSSZZZ6JZ9R056312', follow_redirects=True)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(ujson.decode(response.data)["code"], 4)
        
        response = self.app.get('/get_info_by_vin/VSSZZZ6JZ9R056313', follow_redirects=True)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(ujson.decode(response.data)["code"], 5)
        
        main.URL_main_service = "http://localhost:{}/".format(PORT_FOR_TEST+1)
        response = self.app.get('/get_info_by_vin/VSSZZZ6JZ9R056313', follow_redirects=True)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(ujson.decode(response.data)["code"], 2)       
        main.URL_main_service = "http://localhost:{}/".format(PORT_FOR_TEST)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
