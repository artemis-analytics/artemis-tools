# Copyright © Her Majesty the Queen in Right of Canada, as represented
# by the Minister of Statistics Canada, 2019.
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
from setuptools import setup, find_packages


def main():
    # Define all Cython extensions here - by default, link to arrow and disable warnings

    setup(
        name="artemis-tools",
        version="0.1.0",
        author="Ryan White",
        author_email="ryan.white4@canada.ca",
        packages=find_packages(),
        install_requires=[],
        description="Analytical Tools for the Artemis ecosystem",
    )


if __name__ == "__main__":
    main()
