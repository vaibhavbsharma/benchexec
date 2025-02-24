"""
BenchExec is a framework for reliable benchmarking.
This file is part of BenchExec.
Copyright (C) 2007-2019  Dirk Beyer
All rights reserved.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import benchexec.util as util
import benchexec.tools.template
import benchexec.result as result

class Tool(benchexec.tools.template.BaseTool):
    """
    Tool info for Dartagnan (https://github.com/hernanponcedeleon/Dat3M).
    """

    REQUIRED_PATHS = [
        "svcomp/target",
        "dartagnan/target",
        "cat",
        "lib",
        "smack",
    ]

    def executable(self):
        return util.find_executable("./Dartagnan-SVCOMP.sh")

    def name(self):
        return "Dartagnan"
    
    def cmdline(self, executable, options, tasks, propertyfile=None, rlimits={}):
        return [executable] + options + tasks

    def version(self, executable):
        return self._version_from_tool(executable)
    
    def determine_result(self, returncode, returnsignal, output, isTimeout):
        status = result.RESULT_ERROR
        if output:
            result_str = output[-1].strip()
            if "FAIL" in result_str:
                status = result.RESULT_FALSE_PROP
            elif "PASS" in result_str:
                status = result.RESULT_TRUE_PROP
            elif "UNKNOWN" in result_str:
                status = result.RESULT_UNKNOWN
        return status

    def program_files(self, executable):
        return [executable] + self.REQUIRED_PATHS

