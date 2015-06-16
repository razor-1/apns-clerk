# Author Aleksi Hoffman
# Based on apns-client implementation by Sardar Yumatov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


__title__ = 'apns-clerk'
__version__ = "0.2.0"
__author__ = "Aleksi Hoffman"
__contact__ = "aleksi@lekksi.com"
__license__ = "Apache 2.0"
__homepage__ = "https://bitbucket.org/aleksihoffman/apns-clerk"
__copyright__ = 'Copyright 2014 Aleksi Hoffman'


from apns_clerk.apns import APNs, Message
from apns_clerk.transport import Session
