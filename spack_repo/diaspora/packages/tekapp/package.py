# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Tekapp(CMakePackage):
    """APS mini-app simulating tomographic reconstruction on streaming
    tomography data using a sliding window and the SIRT algorithm."""

    homepage = "https://github.com/diaspora-project/aps-mini-apps"
    git = "https://github.com/diaspora-project/aps-mini-apps.git"

    maintainers("mdorier")

    version("diaspora_stream_api", branch="diaspora_stream_api")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.20:", type="build")
    depends_on("flatbuffers", type=("build", "run"))
    depends_on("mpi")
    depends_on("hdf5+mpi")
    depends_on("fmt")
    depends_on("diaspora-stream-api@0.5.6:")

    extends("python")
    depends_on("python@3:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-tomopy@1.11.0:", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-dxchange", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-flatbuffers", type=("build", "run"))
    depends_on("py-pip", type=("build", "run"))
    depends_on("swig", type="build")

    def cmake_args(self):
        spec = self.spec
        return [
            self.define("CMAKE_CXX_COMPILER", spec["mpi"].mpicxx),
            self.define("CMAKE_C_COMPILER", spec["mpi"].mpicc),
        ]
