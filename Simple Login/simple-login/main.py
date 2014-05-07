#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
'''
Jason Slocum
5.6.14
DPW
Classes
'''

import webapp2 # use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): # function that starts everything
        self.response.write('Hello world!')
        # code goes here

    def additional_functions(self):
        pass
        # code goes here

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
