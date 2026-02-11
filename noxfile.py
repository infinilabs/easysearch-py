#  Copyright 2021-2026 INFINI Labs
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import nox

SOURCE_FILES = (
    "setup.py",
    "noxfile.py",
    "easysearch/",
    "test_easysearch/",
    "utils/",
)


@nox.session(python=["2.7", "3.4", "3.5", "3.6", "3.7", "3.8", "3.9"])
def test(session):
    session.install(".")
    session.install("-r", "dev-requirements.txt")

    session.run("python", "setup.py", "test")


@nox.session()
def blacken(session):
    session.install("black")

    session.run("black", "--target-version=py38", *SOURCE_FILES)
    session.run("python", "utils/license-headers.py", "fix", *SOURCE_FILES)

    lint(session)


@nox.session()
def lint(session):
    session.install("flake8", "black", "mypy")

    session.run("black", "--target-version=py38", "--check", *SOURCE_FILES)
    session.run("flake8", *SOURCE_FILES)
    session.run("python", "utils/license-headers.py", "check", *SOURCE_FILES)

    # Workaround to make '-r' to still work despite uninstalling aiohttp below.
    session.run("python", "-m", "pip", "install", "aiohttp")

    # Run mypy on the package and then the type examples separately for
    # the two different mypy use-cases, ourselves and our users.
    session.run("mypy", "--strict", "easysearch/")
    session.run("mypy", "--strict", "test_easysearch/test_types/sync_types.py")
    session.run("mypy", "--strict", "test_easysearch/test_types/async_types.py")

    # Make sure we don't require aiohttp to be installed for users to
    # receive type hint information from mypy.
    session.run("python", "-m", "pip", "uninstall", "--yes", "aiohttp")
    session.run("mypy", "--strict", "easysearch/")
    session.run("mypy", "--strict", "test_easysearch/test_types/sync_types.py")


@nox.session()
def docs(session):
    session.install(".")
    session.install(
        "-rdev-requirements.txt", "sphinx-rtd-theme", "sphinx-autodoc-typehints"
    )
    session.run("python", "-m", "pip", "install", "sphinx-autodoc-typehints")

    session.run("sphinx-build", "docs/sphinx/", "docs/sphinx/_build", "-b", "html")
