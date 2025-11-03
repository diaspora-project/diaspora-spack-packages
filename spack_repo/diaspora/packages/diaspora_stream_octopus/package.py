# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install diaspora-stream-octopus
#
# You can edit this file again by typing:
#
#     spack edit diaspora-stream-octopus
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class DiasporaStreamOctopus(CMakePackage):
    """Kafka-based backend for the Diaspora Streaming API."""

    homepage = "https://github.com/mdiaspora-project/diaspora-stream-octopus"
    url = "https://github.com/diaspora-project/diaspora-stream-octopus.git"
    git = "https://github.com/diaspora-project/diaspora-stream-octopus.git"

    maintainers("mdorier")

    version("main", branch="main")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.21:", type=("build"))
    depends_on("pkg-config", type=("build"))
    depends_on("diaspora-stream-api@0.4.0:")
    depends_on("librdkafka")
    depends_on("uuid")

    def cmake_args(self):
        args = []
        return args
