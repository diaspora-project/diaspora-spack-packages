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
    url = "https://github.com/diaspora-project/diaspora-stream-octopus/archive/refs/tags/v0.1.0.tar.gz"
    git = "https://github.com/diaspora-project/diaspora-stream-octopus.git"

    maintainers("mdorier")

    version("main", branch="main")
    version("0.1.1", sha256="660b4dc91e3c3a176c4cca2776a5e8ec2b30fe6a7c6a4fca1657713b5b8c8a7e")
    version("0.1.0", sha256="a87d82f23ad3d5d68577ee0d243bfbd0f82d4089aa0a19e42b7cd6579a60ca13")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.21:", type=("build"))
    depends_on("pkg-config", type=("build"))
    depends_on("diaspora-stream-api@0.5.0:")
    depends_on("librdkafka")
    depends_on("uuid")

    def cmake_args(self):
        args = []
        return args
