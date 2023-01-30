"""
Native Python wrappers for PyMaterialX and PyOpenColorIO, providing helper
functions for transforming MaterialX colors between OpenColorIO color spaces.

By default, the OpenColorIO configuration packaged with MaterialX Python will
be used, but clients may instead pass their own custom configurations to these
methods.
"""
from __future__ import annotations
import MaterialX.colorspace
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
from MaterialX.PyMaterialXCore import ExceptionFoundCycle
from MaterialX.PyMaterialXCore import ExceptionOrphanedElement
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
import MaterialX.PyMaterialXCore
import os

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
    "ExceptionFoundCycle",
    "ExceptionOrphanedElement",
    "FILENAME_TYPE_STRING",
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
    "PortElement",
    "Property",
    "PropertyAssign",
    "PropertySet",
    "PropertySetAssign",
    "SURFACE_MATERIAL_NODE_STRING",
    "SURFACE_SHADER_TYPE_STRING",
    "StringResolver",
    "Token",
    "TreeIterator",
    "TypeDef",
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
    "createDocument",
    "createNamePath",
    "createValidName",
    "geomStringsMatch",
    "getColorSpaces",
    "getConnectedOutputs",
    "getDefaultOCIOConfig",
    "getGeometryBindings",
    "getShaderNodes",
    "getVersionIntegers",
    "getVersionString",
    "incrementName",
    "isValidName",
    "os",
    "parentNamePath",
    "prettyPrint",
    "replaceSubstrings",
    "splitNamePath",
    "splitString",
    "stringEndsWith",
    "targetStringsMatch",
    "transformColor"
]


def createDocument(*args, **kwargs) -> typing.Any:
    pass
def createNamePath(arg0: typing.List[str]) -> str:
    pass
def createValidName(name: str, replaceChar: str = '_') -> str:
    pass
def geomStringsMatch(arg0: str, arg1: str, arg2: bool) -> bool:
    pass
def getConnectedOutputs(arg0: MaterialX.PyMaterialXCore.Node) -> typing.List[MaterialX.PyMaterialXCore.Output]:
    pass
def getGeometryBindings(*args, **kwargs) -> typing.Any:
    pass
def getShaderNodes(materialNode: MaterialX.PyMaterialXCore.Node, nodeType: str = 'surfaceshader', target: str = '') -> typing.Set[MaterialX.PyMaterialXCore.Node]:
    pass
def getVersionIntegers() -> typing.Tuple[int, int, int]:
    pass
def getVersionString() -> str:
    pass
def incrementName(arg0: str) -> str:
    pass
def isValidName(arg0: str) -> bool:
    pass
def parentNamePath(arg0: str) -> str:
    pass
def prettyPrint(arg0: MaterialX.PyMaterialXCore.Element) -> str:
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
ARRAY_PREFERRED_SEPARATOR = ', '
ARRAY_VALID_SEPARATORS = ', '
DEFAULT_TYPE_STRING = 'color3'
DISPLACEMENT_SHADER_TYPE_STRING = 'displacementshader'
FILENAME_TYPE_STRING = 'filename'
GEOMNAME_TYPE_STRING = 'geomname'
LIGHT_SHADER_TYPE_STRING = 'lightshader'
MATERIAL_TYPE_STRING = 'material'
MULTI_OUTPUT_TYPE_STRING = 'multioutput'
NAME_PATH_SEPARATOR = '/'
NAME_PREFIX_SEPARATOR = ':'
NONE_TYPE_STRING = 'none'
SURFACE_MATERIAL_NODE_STRING = 'surfacematerial'
SURFACE_SHADER_TYPE_STRING = 'surfaceshader'
VALUE_STRING_FALSE = 'false'
VALUE_STRING_TRUE = 'true'
VOLUME_MATERIAL_NODE_STRING = 'volumematerial'
VOLUME_SHADER_TYPE_STRING = 'volumeshader'
_defaultConfig = None
_defaultConfigFilename = 'config/config.ocio'
_validateDefaultConfig = False
