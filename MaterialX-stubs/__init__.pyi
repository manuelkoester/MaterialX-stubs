from __future__ import annotations
import MaterialX
import typing
from MaterialX.PyMaterialXCore import Backdrop
from MaterialX.PyMaterialXCore import Collection
from MaterialX.PyMaterialXCore import Color3
from MaterialX.PyMaterialXCore import Color4
from MaterialX.PyMaterialXCore import CommentElement
from MaterialX.PyMaterialXCore import Document
from MaterialX.PyMaterialXCore import Edge
from MaterialX.PyMaterialXCore import Element
from MaterialX.PyMaterialXCore import ElementPredicate
from MaterialX.PyMaterialXCore import Exception
from MaterialX.PyMaterialXFormat import ExceptionFileMissing
from MaterialX.PyMaterialXCore import ExceptionFoundCycle
from MaterialX.PyMaterialXCore import ExceptionOrphanedElement
from MaterialX.PyMaterialXFormat import ExceptionParseError
from MaterialX.PyMaterialXFormat import FilePath
from MaterialX.PyMaterialXFormat import FileSearchPath
from MaterialX.PyMaterialXFormat import Format
from MaterialX.PyMaterialXCore import GenericElement
from MaterialX.PyMaterialXCore import GeomElement
from MaterialX.PyMaterialXCore import GeomInfo
from MaterialX.PyMaterialXCore import GeomProp
from MaterialX.PyMaterialXCore import GeomPropDef
from MaterialX.PyMaterialXCore import GraphElement
from MaterialX.PyMaterialXCore import GraphIterator
from MaterialX.PyMaterialXCore import Implementation
from MaterialX.PyMaterialXCore import InheritanceIterator
from MaterialX.PyMaterialXCore import Input
from MaterialX.PyMaterialXCore import InterfaceElement
from MaterialX.PyMaterialXCore import LinearUnitConverter
from MaterialX.PyMaterialXCore import Look
from MaterialX.PyMaterialXCore import LookGroup
from MaterialX.PyMaterialXCore import MaterialAssign
from MaterialX.PyMaterialXCore import Matrix33
from MaterialX.PyMaterialXCore import Matrix44
from MaterialX.PyMaterialXCore import MatrixBase
from MaterialX.PyMaterialXCore import Member
from MaterialX.PyMaterialXCore import Node
from MaterialX.PyMaterialXCore import NodeDef
from MaterialX.PyMaterialXCore import NodeGraph
from MaterialX.PyMaterialXCore import NodePredicate
from MaterialX.PyMaterialXCore import Output
from MaterialX.PyMaterialXCore import PortElement
from MaterialX.PyMaterialXCore import Property
from MaterialX.PyMaterialXCore import PropertyAssign
from MaterialX.PyMaterialXCore import PropertySet
from MaterialX.PyMaterialXCore import PropertySetAssign
from MaterialX.PyMaterialXCore import StringResolver
from MaterialX.PyMaterialXCore import Token
from MaterialX.PyMaterialXCore import TreeIterator
from MaterialX.PyMaterialXFormat import Type
from MaterialX.PyMaterialXCore import TypeDef
from MaterialX.PyMaterialXCore import TypedElement
from MaterialX.PyMaterialXCore import TypedValue_boolean
from MaterialX.PyMaterialXCore import TypedValue_booleanarray
from MaterialX.PyMaterialXCore import TypedValue_color3
from MaterialX.PyMaterialXCore import TypedValue_color4
from MaterialX.PyMaterialXCore import TypedValue_float
from MaterialX.PyMaterialXCore import TypedValue_floatarray
from MaterialX.PyMaterialXCore import TypedValue_integer
from MaterialX.PyMaterialXCore import TypedValue_integerarray
from MaterialX.PyMaterialXCore import TypedValue_matrix33
from MaterialX.PyMaterialXCore import TypedValue_matrix44
from MaterialX.PyMaterialXCore import TypedValue_string
from MaterialX.PyMaterialXCore import TypedValue_stringarray
from MaterialX.PyMaterialXCore import TypedValue_vector2
from MaterialX.PyMaterialXCore import TypedValue_vector3
from MaterialX.PyMaterialXCore import TypedValue_vector4
from MaterialX.PyMaterialXCore import Unit
from MaterialX.PyMaterialXCore import UnitConverter
from MaterialX.PyMaterialXCore import UnitConverterRegistry
from MaterialX.PyMaterialXCore import UnitDef
from MaterialX.PyMaterialXCore import UnitTypeDef
from MaterialX.PyMaterialXCore import Value
from MaterialX.PyMaterialXCore import ValueElement
from MaterialX.PyMaterialXCore import Variant
from MaterialX.PyMaterialXCore import VariantAssign
from MaterialX.PyMaterialXCore import VariantSet
from MaterialX.PyMaterialXCore import Vector2
from MaterialX.PyMaterialXCore import Vector3
from MaterialX.PyMaterialXCore import Vector4
from MaterialX.PyMaterialXCore import VectorBase
from MaterialX.PyMaterialXCore import Visibility
from MaterialX.PyMaterialXFormat import XmlReadOptions
from MaterialX.PyMaterialXFormat import XmlWriteOptions
import MaterialX.PyMaterialXFormat
import os
import sys
import warnings

__all__ = [
    "ARRAY_PREFERRED_SEPARATOR",
    "ARRAY_VALID_SEPARATORS",
    "Backdrop",
    "Collection",
    "Color3",
    "Color4",
    "CommentElement",
    "DEFAULT_TYPE_STRING",
    "DISPLACEMENT_SHADER_TYPE_STRING",
    "Document",
    "Edge",
    "Element",
    "ElementPredicate",
    "Exception",
    "ExceptionFileMissing",
    "ExceptionFoundCycle",
    "ExceptionOrphanedElement",
    "ExceptionParseError",
    "FILENAME_TYPE_STRING",
    "FilePath",
    "FileSearchPath",
    "Format",
    "FormatNative",
    "FormatPosix",
    "FormatWindows",
    "GEOMNAME_TYPE_STRING",
    "GenericElement",
    "GeomElement",
    "GeomInfo",
    "GeomProp",
    "GeomPropDef",
    "GraphElement",
    "GraphIterator",
    "Implementation",
    "InheritanceIterator",
    "Input",
    "InterfaceElement",
    "LIGHT_SHADER_TYPE_STRING",
    "LinearUnitConverter",
    "Look",
    "LookGroup",
    "MATERIALX_SEARCH_PATH_ENV_VAR",
    "MATERIAL_TYPE_STRING",
    "MULTI_OUTPUT_TYPE_STRING",
    "MaterialAssign",
    "Matrix33",
    "Matrix44",
    "MatrixBase",
    "Member",
    "NAME_PATH_SEPARATOR",
    "NAME_PREFIX_SEPARATOR",
    "NONE_TYPE_STRING",
    "Node",
    "NodeDef",
    "NodeGraph",
    "NodePredicate",
    "Output",
    "PATH_LIST_SEPARATOR",
    "PortElement",
    "Property",
    "PropertyAssign",
    "PropertySet",
    "PropertySetAssign",
    "PyMaterialXCore",
    "PyMaterialXFormat",
    "SURFACE_MATERIAL_NODE_STRING",
    "SURFACE_SHADER_TYPE_STRING",
    "StringResolver",
    "Token",
    "TreeIterator",
    "Type",
    "TypeAbsolute",
    "TypeDef",
    "TypeNetwork",
    "TypeRelative",
    "TypedElement",
    "TypedValue_boolean",
    "TypedValue_booleanarray",
    "TypedValue_color3",
    "TypedValue_color4",
    "TypedValue_float",
    "TypedValue_floatarray",
    "TypedValue_integer",
    "TypedValue_integerarray",
    "TypedValue_matrix33",
    "TypedValue_matrix44",
    "TypedValue_string",
    "TypedValue_stringarray",
    "TypedValue_vector2",
    "TypedValue_vector3",
    "TypedValue_vector4",
    "Unit",
    "UnitConverter",
    "UnitConverterRegistry",
    "UnitDef",
    "UnitTypeDef",
    "VALUE_STRING_FALSE",
    "VALUE_STRING_TRUE",
    "VOLUME_MATERIAL_NODE_STRING",
    "VOLUME_SHADER_TYPE_STRING",
    "Value",
    "ValueElement",
    "Variant",
    "VariantAssign",
    "VariantSet",
    "Vector2",
    "Vector3",
    "Vector4",
    "VectorBase",
    "Visibility",
    "XmlReadOptions",
    "XmlWriteOptions",
    "colorspace",
    "createDocument",
    "createNamePath",
    "createValidName",
    "createValueFromStrings",
    "datatype",
    "flattenFilenames",
    "geomStringsMatch",
    "getColorSpaces",
    "getConnectedOutputs",
    "getDefaultOCIOConfig",
    "getGeometryBindings",
    "getShaderNodes",
    "getSubdirectories",
    "getTypeString",
    "getValueString",
    "getVersionIntegers",
    "getVersionString",
    "incrementName",
    "isColorType",
    "isColorValue",
    "isValidName",
    "loadDocuments",
    "loadLibraries",
    "loadLibrary",
    "main",
    "os",
    "parentNamePath",
    "prependXInclude",
    "prettyPrint",
    "readFile",
    "readFromXmlFile",
    "readFromXmlFileBase",
    "readFromXmlString",
    "replaceSubstrings",
    "splitNamePath",
    "splitString",
    "stringEndsWith",
    "stringToValue",
    "sys",
    "targetStringsMatch",
    "transformColor",
    "typeToName",
    "valueToString",
    "warnings",
    "writeToXmlFile",
    "writeToXmlString"
]


def createDocument(*args, **kwargs) -> typing.Any:
    pass
def createNamePath(arg0: typing.List[str]) -> str:
    pass
def createValidName(name: str, replaceChar: str = '_') -> str:
    pass
def createValueFromStrings(*args, **kwargs) -> typing.Any:
    """
    Convert a MaterialX value and type strings to the corresponding
           Python value.  If the given conversion cannot be performed, then None
           is returned.

           Examples:
               createValueFromStrings('0.1', 'float') -> 0.1
               createValueFromStrings('0.1, 0.2, 0.3', 'color3') -> mx.Color3(0.1, 0.2, 0.3)
    """
def flattenFilenames(doc: PyMaterialXCore.Document, searchPath: PyMaterialXFormat.FileSearchPath = ..., customResolver: PyMaterialXCore.StringResolver = None) -> None:
    pass
def geomStringsMatch(arg0: str, arg1: str, arg2: bool) -> bool:
    pass
def getConnectedOutputs(arg0: PyMaterialXCore.Node) -> typing.List[PyMaterialXCore.Output]:
    pass
def getGeometryBindings(*args, **kwargs) -> typing.Any:
    pass
def getShaderNodes(materialNode: PyMaterialXCore.Node, nodeType: str = 'surfaceshader', target: str = '') -> typing.Set[PyMaterialXCore.Node]:
    pass
def getSubdirectories(arg0: typing.List[PyMaterialXFormat.FilePath], arg1: PyMaterialXFormat.FileSearchPath, arg2: typing.List[PyMaterialXFormat.FilePath]) -> None:
    pass
def getTypeString(*args, **kwargs) -> typing.Any:
    """
    Return the MaterialX type string associated with the given Python value
           If the type of the given Python value is not recognized by MaterialX,
           then None is returned.

           Examples:
               getTypeString(1.0) -> 'float'
               getTypeString(mx.Color3(1)) -> 'color3'
    """
def getValueString(*args, **kwargs) -> typing.Any:
    """
    Return the MaterialX value string associated with the given Python value
           If the type of the given Python value is not recognized by MaterialX,
           then None is returned

           Examples:
               getValueString(0.1) -> '0.1'
               getValueString(mx.Color3(0.1, 0.2, 0.3)) -> '0.1, 0.2, 0.3'
    """
def getVersionIntegers() -> typing.Tuple[int, int, int]:
    pass
def getVersionString() -> str:
    pass
def incrementName(arg0: str) -> str:
    pass
def isValidName(arg0: str) -> bool:
    pass
def loadDocuments(rootPath: PyMaterialXFormat.FilePath, searchPath: PyMaterialXFormat.FileSearchPath, skipFiles: typing.Set[str], includeFiles: typing.Set[str], documents: typing.List[PyMaterialXCore.Document], documentsPaths: typing.List[str], readOptions: PyMaterialXFormat.XmlReadOptions = None, errors: typing.List[str] = None) -> None:
    pass
def loadLibraries(libraryFolders: typing.List[PyMaterialXFormat.FilePath], searchPath: PyMaterialXFormat.FileSearchPath, doc: PyMaterialXCore.Document, excludeFiles: typing.Set[str] = set(), readOptions: PyMaterialXFormat.XmlReadOptions = None) -> typing.Set[str]:
    pass
def loadLibrary(file: PyMaterialXFormat.FilePath, doc: PyMaterialXCore.Document, searchPath: PyMaterialXFormat.FileSearchPath = ..., readOptions: PyMaterialXFormat.XmlReadOptions = None) -> None:
    pass
def parentNamePath(arg0: str) -> str:
    pass
def prependXInclude(arg0: PyMaterialXCore.Document, arg1: PyMaterialXFormat.FilePath) -> None:
    pass
def prettyPrint(arg0: PyMaterialXCore.Element) -> str:
    pass
def readFile(arg0: PyMaterialXFormat.FilePath) -> str:
    pass
def readFromXmlFileBase(doc: PyMaterialXCore.Document, filename: PyMaterialXFormat.FilePath, searchPath: PyMaterialXFormat.FileSearchPath = ..., readOptions: PyMaterialXFormat.XmlReadOptions = None) -> None:
    pass
def readFromXmlString(doc: PyMaterialXCore.Document, str: str, readOptions: PyMaterialXFormat.XmlReadOptions = None) -> None:
    pass
def replaceSubstrings(arg0: str, arg1: typing.Dict[str, str]) -> str:
    pass
def splitNamePath(arg0: str) -> typing.List[str]:
    pass
def splitString(arg0: str, arg1: str) -> typing.List[str]:
    pass
def stringEndsWith(arg0: str, arg1: str) -> bool:
    pass
def targetStringsMatch(arg0: str, arg1: str) -> bool:
    pass
def writeToXmlFile(doc: PyMaterialXCore.Document, filename: PyMaterialXFormat.FilePath, writeOptions: PyMaterialXFormat.XmlWriteOptions = None) -> None:
    pass
def writeToXmlString(doc: PyMaterialXCore.Document, writeOptions: PyMaterialXFormat.XmlWriteOptions = None) -> str:
    pass
ARRAY_PREFERRED_SEPARATOR = ', '
ARRAY_VALID_SEPARATORS = ', '
DEFAULT_TYPE_STRING = 'color3'
DISPLACEMENT_SHADER_TYPE_STRING = 'displacementshader'
FILENAME_TYPE_STRING = 'filename'
FormatNative: MaterialX.PyMaterialXFormat.Format # value = Format.FormatWindows
FormatPosix: MaterialX.PyMaterialXFormat.Format # value = Format.FormatPosix
FormatWindows: MaterialX.PyMaterialXFormat.Format # value = Format.FormatWindows
GEOMNAME_TYPE_STRING = 'geomname'
LIGHT_SHADER_TYPE_STRING = 'lightshader'
MATERIALX_SEARCH_PATH_ENV_VAR = 'MATERIALX_SEARCH_PATH'
MATERIAL_TYPE_STRING = 'material'
MULTI_OUTPUT_TYPE_STRING = 'multioutput'
NAME_PATH_SEPARATOR = '/'
NAME_PREFIX_SEPARATOR = ':'
NONE_TYPE_STRING = 'none'
PATH_LIST_SEPARATOR = ';'
SURFACE_MATERIAL_NODE_STRING = 'surfacematerial'
SURFACE_SHADER_TYPE_STRING = 'surfaceshader'
TypeAbsolute: MaterialX.PyMaterialXFormat.Type # value = Type.TypeAbsolute
TypeNetwork: MaterialX.PyMaterialXFormat.Type # value = Type.TypeNetwork
TypeRelative: MaterialX.PyMaterialXFormat.Type # value = Type.TypeRelative
VALUE_STRING_FALSE = 'false'
VALUE_STRING_TRUE = 'true'
VOLUME_MATERIAL_NODE_STRING = 'volumematerial'
VOLUME_SHADER_TYPE_STRING = 'volumeshader'
__version__ = '1.38.0'
