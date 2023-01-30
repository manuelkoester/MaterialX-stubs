"""Module containing Python bindings for the MaterialXFormat library"""
from __future__ import annotations
import MaterialX.PyMaterialXFormat
import typing
import MaterialX.PyMaterialXCore

__all__ = [
    "ExceptionFileMissing",
    "ExceptionParseError",
    "FilePath",
    "FileSearchPath",
    "Format",
    "FormatNative",
    "FormatPosix",
    "FormatWindows",
    "MATERIALX_SEARCH_PATH_ENV_VAR",
    "PATH_LIST_SEPARATOR",
    "Type",
    "TypeAbsolute",
    "TypeNetwork",
    "TypeRelative",
    "XmlReadOptions",
    "XmlWriteOptions",
    "flattenFilenames",
    "getSubdirectories",
    "loadDocuments",
    "loadLibraries",
    "loadLibrary",
    "prependXInclude",
    "readFile",
    "readFromXmlFileBase",
    "readFromXmlString",
    "writeToXmlFile",
    "writeToXmlString"
]


class ExceptionFileMissing(Exception, BaseException):
    pass
class ExceptionParseError(Exception, BaseException):
    pass
class FilePath():
    def __eq__(self, arg0: FilePath) -> bool: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg0: str) -> None: ...
    def __ne__(self, arg0: FilePath) -> bool: ...
    def __truediv__(self, arg0: FilePath) -> FilePath: ...
    def addExtension(self, arg0: str) -> None: ...
    def asString(self, format: Format = Format.FormatWindows) -> str: ...
    def createDirectory(self) -> None: ...
    def exists(self) -> bool: ...
    def getBaseName(self) -> str: ...
    @staticmethod
    def getCurrentPath() -> FilePath: ...
    def getExtension(self) -> str: ...
    def getFilesInDirectory(self, arg0: str) -> typing.List[FilePath]: ...
    @staticmethod
    def getModulePath() -> FilePath: ...
    def getParentPath(self) -> FilePath: ...
    def getSubDirectories(self) -> typing.List[FilePath]: ...
    def isAbsolute(self) -> bool: ...
    def isDirectory(self) -> bool: ...
    def isEmpty(self) -> bool: ...
    def removeExtension(self) -> None: ...
    def size(self) -> int: ...
    pass
class FileSearchPath():
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, searchPath: str, sep: str = ';') -> None: ...
    @typing.overload
    def append(self, arg0: FilePath) -> None: ...
    @typing.overload
    def append(self, arg0: FileSearchPath) -> None: ...
    def asString(self, sep: str = ';') -> str: ...
    def clear(self) -> None: ...
    def find(self, arg0: FilePath) -> FilePath: ...
    def isEmpty(self) -> bool: ...
    def prepend(self, arg0: FilePath) -> None: ...
    def size(self) -> int: ...
    pass
class Format():
    """
    Members:

      FormatWindows

      FormatPosix

      FormatNative
    """
    def __index__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    FormatNative: MaterialX.PyMaterialXFormat.Format # value = Format.FormatWindows
    FormatPosix: MaterialX.PyMaterialXFormat.Format # value = Format.FormatPosix
    FormatWindows: MaterialX.PyMaterialXFormat.Format # value = Format.FormatWindows
    __members__: dict # value = {'FormatWindows': Format.FormatWindows, 'FormatPosix': Format.FormatPosix, 'FormatNative': Format.FormatWindows}
    pass
class Type():
    """
    Members:

      TypeRelative

      TypeAbsolute

      TypeNetwork
    """
    def __index__(self) -> int: ...
    def __init__(self, arg0: int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    TypeAbsolute: MaterialX.PyMaterialXFormat.Type # value = Type.TypeAbsolute
    TypeNetwork: MaterialX.PyMaterialXFormat.Type # value = Type.TypeNetwork
    TypeRelative: MaterialX.PyMaterialXFormat.Type # value = Type.TypeRelative
    __members__: dict # value = {'TypeRelative': Type.TypeRelative, 'TypeAbsolute': Type.TypeAbsolute, 'TypeNetwork': Type.TypeNetwork}
    pass
class XmlReadOptions():
    def __init__(self) -> None: ...
    @property
    def parentXIncludes(self) -> typing.List[str]:
        """
        :type: typing.List[str]
        """
    @parentXIncludes.setter
    def parentXIncludes(self, arg0: typing.List[str]) -> None:
        pass
    @property
    def readComments(self) -> bool:
        """
        :type: bool
        """
    @readComments.setter
    def readComments(self, arg0: bool) -> None:
        pass
    @property
    def readXIncludeFunction(self) -> std::function<void __cdecl:
        """
        :type: std::function<void __cdecl
        """
    pass
class XmlWriteOptions():
    def __init__(self) -> None: ...
    @property
    def elementPredicate(self) -> MaterialX.PyMaterialXCore.ElementPredicate:
        """
        :type: MaterialX.PyMaterialXCore.ElementPredicate
        """
    @elementPredicate.setter
    def elementPredicate(self, arg0: MaterialX.PyMaterialXCore.ElementPredicate) -> None:
        pass
    @property
    def writeXIncludeEnable(self) -> bool:
        """
        :type: bool
        """
    @writeXIncludeEnable.setter
    def writeXIncludeEnable(self, arg0: bool) -> None:
        pass
    pass
def flattenFilenames(doc: MaterialX.PyMaterialXCore.Document, searchPath: FileSearchPath = ..., customResolver: MaterialX.PyMaterialXCore.StringResolver = None) -> None:
    pass
def getSubdirectories(arg0: typing.List[FilePath], arg1: FileSearchPath, arg2: typing.List[FilePath]) -> None:
    pass
def loadDocuments(rootPath: FilePath, searchPath: FileSearchPath, skipFiles: typing.Set[str], includeFiles: typing.Set[str], documents: typing.List[MaterialX.PyMaterialXCore.Document], documentsPaths: typing.List[str], readOptions: XmlReadOptions = None, errors: typing.List[str] = None) -> None:
    pass
def loadLibraries(libraryFolders: typing.List[FilePath], searchPath: FileSearchPath, doc: MaterialX.PyMaterialXCore.Document, excludeFiles: typing.Set[str] = set(), readOptions: XmlReadOptions = None) -> typing.Set[str]:
    pass
def loadLibrary(file: FilePath, doc: MaterialX.PyMaterialXCore.Document, searchPath: FileSearchPath = ..., readOptions: XmlReadOptions = None) -> None:
    pass
def prependXInclude(arg0: MaterialX.PyMaterialXCore.Document, arg1: FilePath) -> None:
    pass
def readFile(arg0: FilePath) -> str:
    pass
def readFromXmlFileBase(doc: MaterialX.PyMaterialXCore.Document, filename: FilePath, searchPath: FileSearchPath = ..., readOptions: XmlReadOptions = None) -> None:
    pass
def readFromXmlString(doc: MaterialX.PyMaterialXCore.Document, str: str, readOptions: XmlReadOptions = None) -> None:
    pass
def writeToXmlFile(doc: MaterialX.PyMaterialXCore.Document, filename: FilePath, writeOptions: XmlWriteOptions = None) -> None:
    pass
def writeToXmlString(doc: MaterialX.PyMaterialXCore.Document, writeOptions: XmlWriteOptions = None) -> str:
    pass
FormatNative: MaterialX.PyMaterialXFormat.Format # value = Format.FormatWindows
FormatPosix: MaterialX.PyMaterialXFormat.Format # value = Format.FormatPosix
FormatWindows: MaterialX.PyMaterialXFormat.Format # value = Format.FormatWindows
MATERIALX_SEARCH_PATH_ENV_VAR = 'MATERIALX_SEARCH_PATH'
PATH_LIST_SEPARATOR = ';'
TypeAbsolute: MaterialX.PyMaterialXFormat.Type # value = Type.TypeAbsolute
TypeNetwork: MaterialX.PyMaterialXFormat.Type # value = Type.TypeNetwork
TypeRelative: MaterialX.PyMaterialXFormat.Type # value = Type.TypeRelative
