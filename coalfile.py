from coal import CoalFile
from util import git_clone, download, unzip, default_cmake_build, cp
from os import path

class GLADFile(CoalFile):
    url = "https://github.com/Dav1dde/glad.git"
    exports = ["include", "libs"]
    options = {
        "profile": "core" # default is core, see glad repository for more valid options
    }
    def prepare(self):
        git_clone(self.url, 'master', 'src')
    def build(self):
        default_cmake_build('src/', 'build/', '-DGLAD_PROFILE="%s"' % self.options["profile"])
    def package(self):
        cp('build/include', 'include')
        cp('build/*.a', 'libs/')
        cp('build/*.lib', 'libs/')
    def info(self, generator):
        pass
