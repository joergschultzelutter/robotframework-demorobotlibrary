#!/usr/local/bin/python3
#
# A simple Robot Framework library example in Python
# Author: Joerg Schultze-Lutter, 2022
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from robot.api.deco import library, keyword, not_keyword
from datetime import datetime
import logging

logging.basicConfig(
	level=logging.DEBUG, format="%(asctime)s %(module)s -%(levelname)s- %(message)s"
)
logger = logging.getLogger(__name__)

__version__ = "0.1.0"
__author__ = "Joerg Schultze-Lutter"

# Our demo class
@library(scope="GLOBAL", auto_keywords=False)
class DemoRobotLibrary:
	# Default parameter settings
	DEFAULT_NAME = None
	DEFAULT_LANGUAGE = "en"

	# Class-internal parameters
	__demo_name = None
	__demo_language = None

	# Constructor
	def __init__(
		self,
		demo_name: str = DEFAULT_NAME,
		demo_language: str = DEFAULT_LANGUAGE,
	):
		self.__demo_name = demo_name
		self.__demo_language = demo_language

	# Python "Getter"
	@property
	def demo_name(self):
		return self.__demo_name

	@property
	def demo_language(self):
		return self.__demo_language

	# Python "Setter"
	@demo_name.setter
	def demo_name(self, demo_name: str):
		if not demo_name:
			raise ValueError("No 'name' value has been specified")
		self.__demo_name = demo_name

	@demo_language.setter
	def demo_language(self, demo_language: str):
		if not demo_language:
			raise ValueError("No 'language' value has been specified")
		demo_language = demo_language.lower()
		if demo_language not in ['de','en']:
			raise ValueError("Invalid value for 'language' was specified")
		self.__demo_language = demo_language

	# Robot "Getter" Keywords
	@keyword("Get My Name")
	def get_demo_name(self):
		return self.demo_name

	@keyword("Get My Language")
	def get_demo_language(self):
		return self.demo_language

	# Robot "Setter" Keywords
	@keyword("Set My Name")
	def set_demo_name(self, name: str = None):
		logger.debug(msg="Setting Demo 'name'")
		self.demo_name = name

	@keyword("Set My Language")
	def set_demo_language(self, language: str = None):
		logger.debug(msg="Setting Demo 'language'")
		self.demo_language = language

	@not_keyword
	def get_daytime_salutation(self,language: str):
		retval = None

		a = datetime.now().hour
		if a < 6 or a > 23:
				retval = "Gute Nacht" if language == "de" else "Good Night"
		elif a >= 6 and a <= 11:
				retval = "Guten Morgen" if language == "de" else "Good Day"
		elif a >=12 and a <= 17:
				retval = "Guten Nachmittag" if language == "de" else "Good Afternoon"
		elif a >=17 and a <= 22:
				retval = "Guten Abend" if language == "de" else "Good Evening"
		else:
				retval = "Guten Tag" if language == "de" else "Good Day"
		
		return retval
		
	@keyword("Get My Salutation")
	def get_the_salutation_text(self, name: str, language: str=None):
		logger.debug(msg="Get the salutation text")
	
		# Get our language. The language code can be taken from either this keyword or from the class.
		# At least one language code needs to be set_demo_language
		if not self.demo_language and not language:
			raise ValueError ("No language specified")

		lang = language if language else self.demo_language

		localized_salutation = self.get_daytime_salutation(language=lang) 
		return_value = f"{localized_salutation} {name}!"
	
		return return_value

  
if __name__ == "__main__":
	pass
