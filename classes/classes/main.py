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
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        about_button = Button()
        about_button.label = "about us"
        about_button.show_label()
        contact_button = Button()
        contact_button.label = "contact us"

class Button(object):
    def __init__(self):
        self.label = '' # public attribute
        self.__size = 60
        self.color = '0x000000'
        self.click()
        #self.on_roll_over("hello!!")

    def click(self):
        print "I've been clicked"

    def on_roll_over(self, message):
        print "You've rolled over my button"

    def show_label(self):
        print "my label is" + self.label


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
